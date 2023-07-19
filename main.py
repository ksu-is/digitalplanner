import calendar

class DigitalPlanner:
    def __init__(self):
        self.calendar = calendar.Calendar()
        self.tasks = {}
    
    def add_task(self, date, task):
        if date not in self.tasks:
            self.tasks[date] = []
        self.tasks[date].append(task)
    
    def remove_task(self, date, task):
        if date in self.tasks:
            if task in self.tasks[date]:
                self.tasks[date].remove(task)
                if len(self.tasks[date]) == 0:
                    del self.tasks[date]
    
    def display_tasks(self, date):
        if date in self.tasks:
            print(f"Tasks for {date}:")
            for i, task in enumerate(self.tasks[date], 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found for this date.")
   
                       
                    



