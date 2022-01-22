#%%
import os
import csv
import matplotlib.pyplot as plt
import datetime

filename = 'month.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header1 = next(reader)
    print(header1)
    nowa = list(enumerate(header1))
    print(nowa)
    for index, column_header1 in nowa:
        print(index, column_header1)

    highs=[]
    mins=[]
    dates=[]
    for row in reader:
        high=int(row[5])
        min=int(row[6])
        date = datetime.datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        mins.append(min)
        dates.append(date)
    print(highs)
    print(dates)
fig, ax = plt.subplots()
ax.plot(dates, highs, label = 'highs')
ax.plot(dates, mins, label = 'mins')
ax.set_title('Najwyzsze lipca')
ax.set_ylabel('Temperatura [F]')
fig.autofmt_xdate()
ax.legend()

plt.show()
#plt.savefig('temp.png')