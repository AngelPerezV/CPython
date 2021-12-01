#hello world
def hello():
    print ("hello world")
hello()

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar
import time


my_date = datetime.today().date()
print(my_date)

print(my_date.replace(day=1) - timedelta(1))
# fisrt date previous month
last_month_day = my_date.replace(day=1) - relativedelta(months=1)  
print(last_month_day)