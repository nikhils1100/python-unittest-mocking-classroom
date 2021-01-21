import importlib, importlib.util

def module_from_file(module_name, file_path):
    '''
    Imports a user module(file) from a different directory
    '''
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Importing the db_connect module which was made in the 1st problem of python assignments
db_connect_module = module_from_file('1_db_connect', '/home/nik/datagrokr/learning/python_assignment/1_db_connect.py')

class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        db_connect = db_connect_module.db_connect('root','','employees')
        query = 'SELECT max(s.salary) FROM employees as e INNER JOIN salaries as s on e.emp_no = s.emp_no'

        result = db_connect.getRows(query)
        # As getRows() is a generator function
        result = iter(result)

        # As result is in form of tuple
        return next(result)[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        db_connect = db_connect_module.db_connect('root','','employees')
        query = 'SELECT min(s.salary) FROM employees as e INNER JOIN salaries as s on e.emp_no = s.emp_no'

        result = db_connect.getRows(query)
        # As getRows() is a generator function
        result = iter(result)

        # As result is in form of tuple 
        return next(result)[0]

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)