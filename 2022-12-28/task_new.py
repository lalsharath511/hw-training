from datetime import datetime
from datetime import date
import json


class TrackEmployee:
    tasks = []
    emp_list = []

    def __init__(self):

        print("employee tracking system")
        print("""click 1 --->registration\nclick 2---> Login""")
        inp = int(input())
        if inp == 1:
            self.emp_signup()
        else:
            self.emp_login()

    def emp_signup(self):
        emp_id = int(input("employee id :"))
        emp_name = input("employee name :")
        vals = {
            "emp_id": emp_id,
            "emp_name": emp_name
        }
        self.emp_list.append(vals)
        self.__init__()

    def emp_login(self):
        emp_id_log = int(input("Enter Your Emp Id :"))

        for val in self.emp_list:
            if val["emp_id"] == emp_id_log:
                self.tasks = []
                print("Login Sucessfull")
                login_time = datetime.now().isoformat().replace("T", " ")[0:16]
                val.update({
                    'login_time': login_time, })
                inp1 = int(input("Press 1 To Create a task \n Press 2 Logout :"))
                if inp1 == 1:
                    self.add_task(val)
                else:
                    self.emp_logout(val)

    def add_task(self, val):
        task_title = input("Title of the task :")
        task_description = input("Detailed explanation of the task :")
        start_time = datetime.now().isoformat().replace("T", " ")[0:16]
        task_list = {
            "task_title": task_title,
            "task_description": task_description,
            "start_time": start_time,

        }
        print("Task create Sucessfully")
        self.end_task(task_list, val)

    def end_task(self, task_list, val):

        task_success = input("Task Completed?\n True/False :")
        end_time = datetime.now().isoformat().replace("T", " ")[0:16]

        task_list.update({
            "end_time": end_time,
            "task_success": task_success,
        })
        self.tasks.append(task_list)

        inp3 = int(input("Press 1 to Add New task / Press 2 to  Logout "))
        if inp3 == 1:
            self.add_task(val)
        elif inp3 == 2:
            self.emp_logout(val)

    def emp_logout(self, val):
        logout_time = datetime.now().isoformat().replace("T", " ")[0:16]
        val.update({
            'logout_time': logout_time,
            'tasks': self.tasks,
        })
        print("Logout Successful")
        for i in self.emp_list:
            if i == val:
                file_name = i['emp_name']
                with open(f'{file_name}.json', 'w') as fp:
                    json.dump(i, fp, indent=1)
                self.__init__()


TrackEmployee()
