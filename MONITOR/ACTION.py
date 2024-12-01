import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

# Import the function
from MONITOR.test_stop_status_30 import *
from MONITOR.test_paymentv4_connect import test_paymentv4_connect_book, test_paymentv4_connect_tiles
from MONITOR.test_error_insufficient import test_error_insufficient








async def evrey_5_minute():
    test_stop_status_30()

async def payment_connection():
    test_paymentv4_connect_tiles()
    test_paymentv4_connect_book()

async def insufficent():
    test_error_insufficient()













async def job_scheduler():
    scheduler = AsyncIOScheduler()


    scheduler.add_job(evrey_5_minute, 'interval', minutes=4)
    scheduler.add_job(payment_connection, 'interval', minutes=10)
    scheduler.add_job(insufficent, 'cron', hour='7,12,17', minute=0)






    scheduler.start()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        # Run the asyncio loop
        asyncio.run(job_scheduler())
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")