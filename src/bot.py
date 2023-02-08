import schedule
import time
import subprocess

def job():
    subprocess.call(['python', 'src/model.py'])

# US market closes 9am NZST
schedule.every().day.at("09:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)