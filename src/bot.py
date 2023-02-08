import schedule
import time
import subprocess

def job():
    subprocess.call(['python', 'src/model.py'])

#schedule.every().day.at("09:00").do(job)
schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)