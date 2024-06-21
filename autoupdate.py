import os
import subprocess
import time
import threading
from datetime import datetime, timedelta

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def job():
    script_dir = os.getcwd()
    directory = os.path.join(script_dir, "yournamescript") #rename to your github repo (example: backappallscripts / autoupdategit)

    if os.path.exists(directory):
        log("Directory exists. Attempting to pull latest changes.")
        result = subprocess.run(["git", "-C", directory, "pull"], capture_output=True, text=True)
        if result.returncode == 0:
            log("Successfully pulled the latest changes.")
        else:
            log(f"Failed to pull the latest changes. Error: {result.stderr}")
    else:
        log("Directory does not exist. Cloning the repository.")
        repo_url = "git@github.com:sekalYT/backappallscripts.git"
        result = subprocess.run(["git", "clone", repo_url, directory], capture_output=True, text=True)
        if result.returncode == 0:
            log(f"Successfully cloned the repository to: {directory}")
        else:
            log(f"Failed to clone the repository. Error: {result.stderr}")

def calculate_sleep_time():
    now = datetime.now()
    next_run = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return (next_run - now).total_seconds()

def countdown(next_run):
    while True:
        now = datetime.now()
        remaining_time = next_run - now
        if remaining_time.total_seconds() <= 0:
            break
        time.sleep(1)

def start_job_with_countdown():
    global next_run
    while True:
        sleep_time = calculate_sleep_time()
        next_run = datetime.now() + timedelta(seconds=sleep_time)
        log(f"Next job scheduled at: {next_run}")
        countdown_thread = threading.Thread(target=countdown, args=(next_run,))
        countdown_thread.start()
        time.sleep(sleep_time)
        job()

def command_listener():
    global next_run
    while True:
        command = input().strip().lower()
        if command == 'countdown':
            now = datetime.now()
            remaining_time = next_run - now
            log(f"Time until next update: {remaining_time}")
        elif command == 'forceupdate':
            log("Force update command received. Updating now.")
            job()

# Запуск задачи и слушателя команд в отдельных потоках
job_thread = threading.Thread(target=start_job_with_countdown)
listener_thread = threading.Thread(target=command_listener)

job_thread.start()
listener_thread.start()
