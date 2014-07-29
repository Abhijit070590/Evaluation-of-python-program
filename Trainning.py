'''
@author :-Abhijit and Uday
'''
from sklearn.svm import SVR
from threading import Timer
import os, re, shutil, subprocess, tarfile, xlrd
import shlex

def read_leadingint(somestr):
    m = re.match(r"(\d+)", somestr)
    return int(m.group(0)) if (m != None) else None

SVR_RBF = None
Y_RBF = None
EVALUATION_DIR = '/home/abhijit/SE'

class Student(object):
    '''
    student details
    '''
    def __init__(self):
        self.email = ''
        self.rollno = ''
        self.marks = {}
        self.problems = []
        self.comments = ''
        
class Test(object):
    '''capture test module instruction'''
    def __init__(self):        
        self.name =''
        self.marks = 0
        self.function = ''
        self.benchmark_time = 0.0
        
class Problem(object):
    '''
    Captures each problem in the evaluation as an instance of this class
    '''
    def __init__(self):
        self.serial_no = 0
        self.title = ''
        self.no_of_files = 0
        self.no_of_testcases = 0
        self.total_marks = 0
        self.file_names = []
        self.testcases = []
        self.cc = 0
        self.mi = 0
        self.lloc = 0
        self.pylint_rating = 0
        self.ntests = 0
        self.nfailures = 0
        self.nerrors = 0
        self.marksperstest = {}
        
class Evaluation(object):
    TITLE_LABEL = 'Title:'
    DATE_LABEL = 'Date:'
    PROBLEM_LABEL = 'Problem:'
    TEST_LABEL = 'Test:'
    FILES_LABEL = 'Files:'
    END_LABEL = 'End'
    TEST_DIR = 'Test'
    REF_DIR = 'ref'
    SUBMISSION_DIR = ''
    RUNTIME_BLOAT_FACTOR = 100.0
    TESTRESULTS_FILE = 'testresults'
    TESTGEN_DECORATORFILE = 'testgenDecorator.py'
    TESTRESULTS_IMPORTFILE = 'set_testresults_file.py'
    
    def __init__(self):
        self.problems = []
        self.title = ''
        self.date = ''
        
    def read_config_file(self,config_file):
        '''
        the config contain the information to read the tarfiles in a specific 
        format, what they are for, which problem they are satisfying etc.
        '''
        try:
            config = open(config_file, 'r')
            problem = None
            for line in config.readlines():
                line = line.strip()
                # Ignore blank lines
                components = line.split()
                if((line != '') and (components[0] != '#')):
                    if(components[0] == self.TITLE_LABEL):
                        self.title += components[1]
                    if(components[0] == self.DATE_LABEL):
                        self.date += components[1] 
                    if((components[0] == self.PROBLEM_LABEL)and(components[1] != self.END_LABEL)):
                        problem = Problem()
                        problem.serial_no += int(components[1])
                        problem.title += components[2]
                        problem.no_of_files += int(components[3])
                        problem.no_of_testcases += int(components[4])
                        problem.total_marks += int(components[5])
                    if(components[0] == self.FILES_LABEL):
                        problem.file_names.append(components[1])
                    if(components[0] == self.TEST_LABEL):
                        test = Test()
                        test.name += components[1]
                        test.marks += int(components[2])
                        test.function += components[3]
                        problem.testcases.append(test)
                    if((components[0] == self.PROBLEM_LABEL)and(components[1] == self.END_LABEL)):
                        self.problems.append(problem)
                        problem = None
                        break

            config.close()
        except IOError:
            raise NameError('Could not open file %s' % (config_file))
            
    def make_folder(self):
        if not os.path.exists('Test'):        
            os.mkdir('Test')
        for problem in self.problems:
            if not os.path.exists(problem.title):           
                os.mkdir(problem.title)
            
    def initialize_benchmarks(self):
        os.chdir('Ref')
        for problem in self.problems:
            for tests in problem.testcases:
                ntests, nfailures, nerrors, runtime, hadprints, haderrors = self.run_test(tests.name, True, 5)
                tests.benchmark_time = runtime
        os.chdir(os.pardir)
        os.chdir('Test')
        
    def extract_submitted_files(self,email,rollno):
        os.chdir(os.pardir)
        for file_name in os.listdir('.'):
            file_namel = file_name.lower()
            components = file_namel.split('.')
            if(components[-1]=='tgz'):
                student_email = components[:-1]
                student_email = '.'.join(student_email)
                
                if (student_email == email.lower()):
                    
                    tar = tarfile.open(file_name,'r:gz')
                    tar.extractall('Test')
        os.chdir('Test')
        str = ''
        for problem in self.problems:
            for file_name in problem.file_names:
                files = os.listdir('.')
                if file_name in files:
                    ap_file_name = rollno + file_name
                    shutil.copy(file_name,'../'+problem.title+'/'+ap_file_name)
                    str += 'Desired file has been submitted.'
                else:
                    str += 'Desired file was not submitted.'
        list = []
        for problem in self.problems:
            list += problem.file_names
        for files in os.listdir('.'):
            if files not in list:
                str += 'Extra files submitted' + files + '.'
        os.chdir(os.pardir)
        return str
        
    def get_code_complexities(self, code_file):
        report = open("report", "wb")
        subprocess.call(['radon', 'cc', code_file], stdout=report)
        report.close()
        report = open('report', 'r')
        cc = 0
        first_line = ''
        for line in report.readlines():
             line = line.strip()
             if (first_line == ''):
                 first_line = line
             if (first_line != code_file):
                 break
             if(line != code_file):                
                 attrs = line.split()
                 if(attrs[0] == 'ERROR:'):
                     break
                 else:
                     cc += int(attrs[1].split(':')[0])
        report.close()

        #os.remove('report')
        return cc
        
    def get_lloc(self, code_file):
        report = open("report", "wb")
        subprocess.call(['radon', 'raw', code_file], stdout=report)
        report.close()
        report = open('report', 'r')
        for line in report.readlines():
            attrs = line.split()
            if (attrs[0] == 'LLOC:'):
                report.close()
                os.remove('report')
                return int(attrs[1])
            else:
                return 0

    def get_maintainability_index(self, code_file):
        report = open("report", "wb")
        subprocess.call(['radon', 'mi', code_file], stdout=report)
        report.close()
        report = open('report', 'r')
        
        for line in report.readlines():
            attrs = line.split()
            if (attrs[0] == code_file and len(attrs) > 2):
                report.close()
                os.remove('report')
                return attrs[2]
            else:
                return str('C')

    def get_pylint_rating(self, code_file):
        report = open("report", "wb")
        subprocess.call(['pylint', code_file], stdout=report)
        report.close()
        report = open('report', 'r')
        prefix = 'Your code has been rated at '
        for line in report.readlines():
            if line.startswith(prefix):
                rating = line[len(prefix):].split()[0]
                report.close()
                os.remove('report')
                return float(rating.split('/')[0])
            else:
                return 0
        
    def run_with_timeout(self, testfile, seconds):
        testfile = testfile +'.py'
        command = 'python ' + testfile
        proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        kill_proc = lambda p: p.kill()
        timer = Timer(seconds, kill_proc, [proc])
        timer.start()
        out, err = proc.communicate()
        timer.cancel()
        
        return (len(out) == 0), (len(err) == 0)
        
    def run_test(self, testfile, in_ref, timelimit):
        if (not in_ref):
            shutil.copy(('../Ref/'+testfile +'.py'), os.getcwd())
            shutil.copy(('../Ref/'+self.TESTRESULTS_IMPORTFILE), os.getcwd())
            shutil.copy(('../Ref/' + self.TESTGEN_DECORATORFILE), os.getcwd())

        hadprints, haderrs = self.run_with_timeout(testfile, timelimit)
        print (testfile,hadprints, haderrs)
        #subprocess.call(['./' + testfile])
        print 'os.path.exists(self.TESTRESULTS_FILE)'+str(os.path.exists(self.TESTRESULTS_FILE))
        if (not os.path.exists(self.TESTRESULTS_FILE)):
            return (0, 0, 0, 0.0, hadprints, haderrs)

        resultsfile = open(self.TESTRESULTS_FILE)
        ntests = 0
        failures = 0
        errors = 0
        runtime = 0.0
        for line in resultsfile.readlines():
            line = line.strip()
            
            if (line != ''):
                attrs = line.split()
                if (len(attrs) > 4 and attrs[0] == 'Ran' and (attrs[2] == 'tests' or attrs[2] == 'test')
                    and attrs[3] == 'in'):
                    ntests = int(attrs[1])
                    runtime = float(attrs[4][:-1])
                elif (attrs[0] == 'FAILED'):
                    failat = line.find('failures=')
                    failures = read_leadingint(line[(failat+9):]) if (failat >= 0) else 0
                    errorat = line.find('errors=')
                    errors = read_leadingint(line[(errorat+7):]) if (errorat >= 0) else 0
                elif (line == 'OK'):
                    failures = 0
                    errors = 0
        
        #if (os.path.exists(self.TESTRESULTS_FILE)):
        os.remove(self.TESTRESULTS_FILE)

        return (ntests, failures, errors, runtime, hadprints, haderrs)

    def evaluate_answers(self,problem):
        overall_comments = 'Test Results for %s:\n'%(problem.title)
        problem_marks = 0
        for tests in problem.testcases:
            overall_comments += 'Testing :' + tests.name + 'benchmark time' + str(tests.benchmark_time)            
            timelimit = self.RUNTIME_BLOAT_FACTOR * tests.benchmark_time            
            ntests, failures, errors, runtime, hadprints, haderrors = self.run_test(tests.name, False, timelimit)
            overall_comments += 'Tests Run: %d, Failures: %d, Errors: %d, Runtime: %.4f\n'%(ntests, failures,
                                                                                            errors, runtime)
            if (runtime == 0):
                overall_comments += ('Test reported syntax / run-time errors and exceptions.\n' if (haderrors) else 
                                    'Test was aborted --- it exceeded time limit.\n')
            if (hadprints):
                overall_comments += 'There were unwanted prints during execution. Please remove such messages before you submit.\n'
                                    
            passed = ntests - failures - errors
            
            problem_marks += tests.marks*(passed + failures * 0.5)

        cc = 0
        lloc = 0
        mi = 0
        pylint_rating = 0
        
        overall_comments += 'Code Quality for %s:\n'%(problem.title)
        
        for files in problem.file_names:
            cc += self.get_code_complexities(files)
            lloc += self.get_lloc(files)
            mi += (ord('C')-ord(self.get_maintainability_index(files)))*16
            pylint_rating += self.get_pylint_rating(files)
        
        print (cc,lloc,mi,pylint_rating,problem_marks)
        return (cc*0.05,lloc*0.05,mi*0.05,pylint_rating*0.05,problem_marks*0.80, overall_comments)

    def clean_all(self):
        '''
        Clean up the test directory - remove all other files
        This is to prepare for testing the submission from the next student
        '''
        for dir_file in os.listdir('.'):
            if (dir_file != 'ref'):
                if os.path.isdir(dir_file):
                    shutil.rmtree(dir_file)
                else:
                    os.remove(dir_file)

class Training:
    NUM_STUDENTS = 45
    STUDENTS = []

    def __init__(self):
        global EVALUATION_DIR
        os.chdir(EVALUATION_DIR)
        self.E = Evaluation()
        self.E.read_config_file('Midterm-config')
        self.y_list = []
        self.parent_list = []
        #self.E.initialize_benchmarks()
        
      # self.P = Evaluation()
      # self.P.read_config_file('Assignment1-config')
        
    def make_students(self):
        workbook = xlrd.open_workbook('2013-iMTech-Marks-Manual.xls')
        worksheet = workbook.sheet_by_name('Midterm')
        num_rows = worksheet.nrows - 1
        num_cels = worksheet.ncols - 1
        cur_row = 0
        for i in range(self.NUM_STUDENTS):
            cur_row +=1
            row = worksheet.row(cur_row)
            cur_cell = 0
            cur_cell += 1
            student = Student()
            student.rollno += worksheet.cell_value(cur_row,cur_cell)
            cur_cell += 2
            student.email += worksheet.cell_value(cur_row,cur_cell)
            cur_cell += 2 
            student.problems = self.E.problems
            for problem in self.E.problems:
                self.y_list.append(worksheet.cell_value(cur_row,cur_cell))
                cur_cell += 1
            self.STUDENTS.append(student)
            
    def evaluate_submission(self):
        os.chdir(self.E.date+'-'+self.E.title)
        self.E.make_folder()
        self.E.initialize_benchmarks()
        #print 'before'
        for student in self.STUDENTS:
            #print 'before extract all'
            print '------------------------------------------------------------------------'
            student.comments += self.E.extract_submitted_files(student.email,student.rollno)
            os.chdir('Test')
            print 'before 2'
            for problem in self.E.problems:                   
                i = self.E.problems.index(problem)
                print student.rollno
                print student.email
                print '******************************************************'
                print student.problems[i].title
                cc,lloc,mi,pylint_rating,marks,comment = self.E.evaluate_answers(problem)
                list = []
                list.append(cc)
                list.append(lloc)
                list.append(mi)
                list.append(pylint_rating)
                list.append(marks)
                self.parent_list.append(list)
                self.E.clean_all()
    
    def trainAndPredit(self):
        
#==============================================================================
#         for student in self.STUDENTS:
#             list = []
#             for i in range(len(self.E.problems)-1):
#                 list.append(student.problems[i].cc)
#                 list.append(student.problems[i].lloc)
#                 list.append(student.problems[i].mi)
#                 list.append(student.problems[i].pylint_rating)
#                 list.append(student.marks[self.E.problems[i].title])
#             parent_list.append(list)
#==============================================================================
        
        global SVR_RBF
        SVR_RBF = SVR(kernel = 'rbf',probability = True, C = 1e3, gamma = 0.1)
        global Y_RBF
        Y_RBF = SVR_RBF.fit(self.parent_list,self.y_list)

   
class Predict:
    NUM_STUDENTS=12
    STUDENTS=[]
    
    def __init__(self):
        global EVALUATION_DIR
        os.chdir(EVALUATION_DIR)
        self.E = Evaluation()
        self.predict_list = []
        self.E.read_config_file('Midterm-config')
        self.marks_list = []
        self.y_list = []
        
      # self.P = Evaluation()
      # self.P.read_config_file('Assignment1-config')
        
    def make_students(self):
        workbook = xlrd.open_workbook('2013-iMTech-Marks-Manual.xls')
        worksheet = workbook.sheet_by_name('Midterm')
        num_rows = worksheet.nrows - 1
        num_cels = worksheet.ncols - 1
        cur_row = 45
        for i in range(self.NUM_STUDENTS):
            cur_row +=1
            row = worksheet.row(cur_row)
            cur_cell = 0
            cur_cell += 1
            student = Student()
            student.rollno += worksheet.cell_value(cur_row,cur_cell)
            cur_cell += 2
            student.email += worksheet.cell_value(cur_row,cur_cell)
            cur_cell += 2 
            student.problems = self.E.problems
            for problem in self.E.problems:
                self.marks_list.append(worksheet.cell_value(cur_row,cur_cell))
                cur_cell += 1
            self.STUDENTS.append(student)
        print self.marks_list
            
    def evaluate_submission(self):
        os.chdir(self.E.date+'-'+self.E.title)
        self.E.make_folder()
        self.E.initialize_benchmarks()
        for student in self.STUDENTS:
            student.comments += self.E.extract_submitted_files(student.email,student.rollno)
            os.chdir('Test')
            for problem in self.E.problems:   
                i = self.E.problems.index(problem)
                print student.rollno
                print student.email
                print '******************************************************'
                print student.problems[i].title
                cc,lloc,mi,pylint_rating,marks,comment = self.E.evaluate_answers(problem)
                list = []
                list.append(cc)
                list.append(lloc)
                list.append(mi)
                list.append(pylint_rating)
                list.append(marks)
                self.predict_list.append(list)
            self.E.clean_all()
    
    def trainAndPredit(self):
        parent_list = []
        for student in self.STUDENTS:
            list = []
            for i in range(len(self.E.problems)-1):
                list.append(student.problems[i].cc)
                list.append(student.problems[i].lloc)
                list.append(student.problems[i].mi)
                list.append(student.problems[i].pylint_rating)
                list.append(student.marks[self.E.problems[i].title])
            parent_list.append(list)
        global Y_RBF
        self.y_list = Y_RBF.predict(self.predict_list)
        print self.y_list
            
    def compare(self):
        marks_mean = 0
        marks_sum = 0
        for i in self.marks_list:
            marks_sum += i
        marks_mean += marks_sum/len(self.marks_list)   
        p_list = [i*i - marks_mean for i in self.marks_list]
        marks_variance = sum(p_list)/len(p_list)
        print 'The mean and variance of the manual marks are respectively' 
        print marks_mean
        print marks_variance
        y_sum = sum([i for i in self.y_list])
        y_mean = y_sum/len(self.y_list)
        y_variance = sum([i*i - y_mean for i in self.y_list])/len(self.y_list)
        print 'The mean and variance of the generated marks are respectively'
        print y_mean
        print y_variance
        
if __name__ == "__main__":
    t = Training()
    t.make_students()
    t.evaluate_submission()
    t.trainAndPredit()
    print '.........................predicting...............................'
    p = Predict()
    p.make_students()
    p.evaluate_submission()
    p.trainAndPredit()
    p.compare()