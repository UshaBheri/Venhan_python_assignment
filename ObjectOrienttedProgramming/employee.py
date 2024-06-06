class Employee:
    number_of_employees = 0

    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
        Employee.number_of_employees += 1

    @classmethod
    def get_num_of_employee(cls):
        total_employees =  cls.number_of_employees
        print("Total employees: {}".format(total_employees))
    
    @staticmethod
    def validate_employee_id(employee_id):
         return employee_id.isdigit()
    
employee1 = Employee("101","Usha")
employee2 = Employee("102","Laya")

Employee.get_num_of_employee()

print("Valid employee: {}".format(Employee.validate_employee_id("10ab")))

# output: Total employees: 2
#         Valid employee: False





