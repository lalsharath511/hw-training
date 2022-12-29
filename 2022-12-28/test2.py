from datetime import datetime
import json

class TrackEmployee:
 
    def __init__(self):
        self.log={}
        self.task_list=[]
    def login(self, emp_id, emp_name): 
        login_time = datetime.now().isoformat().replace("T", " ")[0:16]
        self.log.update({
            "emp_id": emp_id,
            "emp_name": emp_name,
            "login_time": login_time,
              })
    def add_task(self, task_title, task_description,):
        tasks = {
            "task_title": task_title,
            "task_description": task_description,
            "start_time": datetime.now().isoformat().replace("T", " ")[0:16],

        }
        self.task_list.append(tasks)  
    def end_task(self, task_title, task_success):
        for a in self.task_list:
            if a["task_title"]==task_title:
                a.update({
                "end_time": datetime.now().isoformat().replace("T", " ")[0:16],
                "task_success": task_success,
                })
    def emp_logout(self):
        self.log.update({
            'logout_time': datetime.now().isoformat().replace("T", " ")[0:16],
            'tasks': self.task_list,
        })
        file_name = self.log['emp_name']
        with open(f'{file_name}.json', 'w') as fp:
            json.dump(self.log, fp, indent=1)
        print("Logout Successful")
        

        
    