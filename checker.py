from datetime import datetime
from selenium import webdriver
from time import sleep
from pytz import timezone
import signal

fd = open('data.csv', 'a+')
url = 'http://www.maxmind.com'
driver = webdriver.PhantomJS()
driver.get(url)

sleep(15)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
a = 0
if 'Chat with us!' in html:
  a = 1

t = datetime.now(timezone('US/Eastern'))
tm = t.time()
d = t.date()

p = 0
if (tm.hour >= 8 and tm.hour < 21 and d.weekday() < 5):
  p = 1

na = 0
if (a==0 and p==1):
  na = 1

row = str(t.date().isoformat()) + "," + str(tm.isoformat()) + "," + str(a) + "," + str(p) + "," + str(na) + "\n"

fd.write(row)
fd.close()

driver.service.process.send_signal(signal.SIGTERM)
driver.quit()
