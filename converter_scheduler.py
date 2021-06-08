# Schedule Library imported
import schedule
import time
import exchange_rate_main as erm

# Task scheduling

# Every day at 12am or 00:00 time bedtime() is called.
# schedule.every().day.at("00:00").do(erm.exchange_rate_usd)

schedule.every(2).minutes.do(erm.exchange_rate_usd)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)