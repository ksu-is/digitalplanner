import calendar

class DigitalPlanner:
    def __init__(self):
        self.calendar = calendar.Calendar()
        self.tasks = {}
    
    def add_task(self, date, task):
        if date not in self.tasks:
            self.tasks[date] = []
        self.tasks[date].append(task)



