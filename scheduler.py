import schedule
import time

from rabbitmq_send_message import queue_broker


send_queue = queue_broker()

schedule.every(15).minutes.do(send_queue.send_message,'rss_reader', 'tech')

def run_scheduled_jobs():
    send_queue.send_message('rss_reader', 'tech')
    while True:
        print('schedule running')
        schedule.run_pending()
        time.sleep(20)
