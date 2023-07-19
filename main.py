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
    
    def display_calendar(self, year, month):
        cal = self.calendar.monthdayscalendar(year, month)
        header = calendar.month_name[month] + " " + str(year)
        print(f"{header.center(20)}")
        print("Mon Tue Wed Thu Fri Sat Sun")
        for week in cal:
            for day in week:
                if day == 0:
                    print("    ", end="")
                else:
                    tasks_indicator = " " if str(day) not in self.tasks else "*"
                    print(f"{day:2d}{tasks_indicator}", end=" ")
            print()
    
    def clear_tasks(self):
        self.tasks = {}


class Authentication:
    def __init__(self):
        self.users = {}

    def register(self):
        while True:
            username = input("Enter a username: ")
            if username in self.users:
                print("Username already exists. Please choose a different username.")
            else:
                password = input("Enter a password: ")
                self.users[username] = password
                print("Registration successful!")
                return
    
    def login(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if self.validate_credentials(username, password):
                print("Login successful!")
                return True
            else:
                print("Invalid username or password!")
                choice = input("Do you want to try again? (y/n): ")
                if choice.lower() != "y":
                    return False
                    



