import matplotlib as mpl
mpl.use('QT4AGG')
import matplotlib.pyplot as plt
import datetime as dt

start = dt.datetime.now()
end = start + dt.timedelta(minutes=15)
delta = dt.timedelta(seconds=1)
dates = mpl.dates.drange(start, end, delta)

import random
import math

temp = 60
def gen_temp(sa):
    global temp
    if sa == 0:
        return temp
    add = False
    if sa == 1:
        add = True
    if temp >= 75:
        add = False
    elif temp <= 50:
        add = True
    if add:
        temp = temp + 1
    else:
        temp = temp - 1
    return temp


temps = [ gen_temp(random.randint(-1, 1)) for i in range(900)]


fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot_date(dates, temps, '-')

date_fmt = mpl.dates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(date_fmt)

min_loc = mpl.dates.MinuteLocator()
ax.xaxis.set_major_locator(min_loc)

plt.ylim((40, 90))
plt.grid(True)
plt.xlabel('Time/seconds')
plt.ylabel('Temperature/Centigrade')
plt.title('Boiler#1 Sensor#10 Temperature Figure')
plt.show()
