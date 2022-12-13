from datetime import datetime
from datetime import date
import json


class Trackemployee:
    tasks = []
    emp_list = []

    def __init__(self):

        print("employee tracking system")
        print("""click 1 --->registration\nclick 2---> Login""")
        inp = int(input())
        if inp == 1:
            self.signupfun()
        else:
            self.loginfun()

    def signupfun(self):
        emp_id = int(input("employee id :"))
        emp_name = input("employee name :")
        vals = {
            "emp_id": emp_id,
            "emp_name": emp_name
        }
        self.emp_list.append(vals)
        print(self.emp_list)
        self.__init__()

    def loginfun(self):
        emp_id_log = int(input("Enter Your Emp Id :"))

        for val in self.emp_list:
            if val["emp_id"] == emp_id_log:
                self.tasks = []
                print("Login Sucessfull")
                b = datetime.now().isoformat().replace("T", " ")[0:16]
                val.update({
                    'login_time': b, })
                inp1 = int(input("Press 1 To Create a task \nPress 2 Logout :"))
                if inp1 == 1:
                    self.addtaskfun(val)
                else:
                    self.emp_logout(val)

    def addtaskfun(self, val):
        task_title = input("Title of the task :")
        task_description = input("Detailed explanation of the task :")
        start_time = datetime.now().isoformat().replace("T", " ")[0:16]
        vals = {
            "task_title": task_title,
            "task_description": task_description,
            "start_time": start_time,

        }
        print("Task create Sucessfully")
        self.endtaskfun(vals, val)

    def endtaskfun(self, vals, val):

        task_success = input("Task Completed?\n True/False :")
        end_time = datetime.now().isoformat().replace("T", " ")[0:16]

        vals.update({
            "end_time": end_time,
            "task_success": task_success,
        })
        self.tasks.append(vals)

        inp3 = int(input("Press 1 to Add New task / Press 2 to  Logout "))
        if inp3 == 1:
            self.addtaskfun(val)
        elif inp3 == 2:
            self.emp_logout(val)

    def emp_logout(self, val):
        a = datetime.now().isoformat().replace("T", " ")[0:16]
        val.update({
            'logout_time': a,
            'tasks': self.tasks,
        })
        print("Logout Successful")
        for i in self.emp_list:
            if i == val:
                data=i['emp_name']
                # dict_str=json.dumps(i,indent=1)
                # filename=f'{data}.json'
                # file=open(filename,"w")
                # file.write(dict_str)
                # self.__init__()
                with open(f'{data}.json', 'w') as fp:
                    json.dump(i, fp,indent=1)
                self.__init__()
                

Trackemployee()
