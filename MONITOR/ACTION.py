import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
# Import the function
from MONITOR.test_stop_status_30 import *
from MONITOR.payment_element import *





async def evrey_5_minute():
    test_stop_status_30()
    asyncio.run(check_element())













async def job_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(evrey_5_minute, 'interval', minutes=5)
    scheduler.start()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        # Run the asyncio loop
        asyncio.run(job_scheduler())
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")