import os
import subprocess
import time
import threading
from datetime import datetime, timedelta


class Settings:
    def __init__(self):
        self.repo_url = "https://github.com/sekalYT/autorestart" #change URL to your REPO URL or SSH if your repo has a private visibility
        self.foldername = 'myscript' #name your work folder, default = myscript, your REPO downloads in "myscript" folder

#Attention!
#In this solution, your repo downloads automaticly in root folder OS 
#(Linux -> cd, Windows -> C:\Users\User\foldername) and other methods are NOT SUPPORTED

class Main():
    def __init__(self):
        self.next_run = None
        self.settings = Settings()

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

    def job(self):
        script_dir = os.getcwd()
        directory = os.path.join(script_dir, f"{self.settings.foldername}")

        if os.path.exists(directory):
            self.log("Directory exists. Attempting to pull latest changes.")
            result = subprocess.run(["git", "-C", directory, "pull"], capture_output=True, text=True)
            if result.returncode == 0:
                self.log("Successfully pulled the latest changes.")
            else:
                self.log(f"Failed to pull the latest changes. Error: {result.stderr}")
        else:
            self.log("Directory does not exist. Cloning the repository.")
            result = subprocess.run(["git", "clone", self.settings.repo_url, directory], capture_output=True, text=True)
            if result.returncode == 0:
                self.log(f"Successfully cloned the repository to: {directory}")
            else:
                self.log(f"Failed to clone the repository. Error: {result.stderr}")

    def calculate_sleep_time(self):
        now = datetime.now()
        next_run = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        return (next_run - now).total_seconds()

    def countdown(self, next_run):
        while True:
            now = datetime.now()
            remaining_time = next_run - now
            if remaining_time.total_seconds() <= 0:
                break
            time.sleep(1)

    def start_job_with_countdown(self):
        while True:
            sleep_time = self.calculate_sleep_time()
            self.next_run = datetime.now() + timedelta(seconds=sleep_time)
            self.log(f"Next job scheduled at: {self.next_run}")
            countdown_thread = threading.Thread(target=self.countdown, args=(self.next_run,))
            countdown_thread.start()
            time.sleep(sleep_time)
            self.job()

    def command_listener(self):
        while True:
            command = input().strip().lower()
            if command == 'countdown':
                now = datetime.now()
                remaining_time = self.next_run - now
                self.log(f"Time until next update: {remaining_time}")
            elif command == 'forceupdate':
                self.log("Force update command received. Updating now.")
                self.job()
            elif command == 'updatemyself':
                self.log("Checking updates autoupdatescript...")
                self.updatemyself()

    def run(self):
        job_thread = threading.Thread(target=self.start_job_with_countdown)
        listener_thread = threading.Thread(target=self.command_listener)

        job_thread.start()
        listener_thread.start()

if __name__ == "__main__":
    main = Main()
    main.run()