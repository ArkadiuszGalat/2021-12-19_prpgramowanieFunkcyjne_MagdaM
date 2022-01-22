#%%
import datetime
day1 = input('Podaj pierwszą datę w formacie rrrr-mm-dd: ')
day2 = input('Podaj drugą datę w formacie rrrr-mm-dd: ')

day1list = day1.split('-')
day2list = day2.split('-')

print (day1list)
date1 = datetime.date(int(day1list[0]),int(day1list[1]),int(day1list[2]))
date2 = datetime.date(int(day2list[0]),int(day2list[1]),int(day2list[2]))
print(date1)
print(date2)
print(f'Żyjesz już na tym świecie {(date2-date1).days} dni.')
#%%
import datetime
day1 = datetime.date(1971,9,12)
day2 = datetime.date.today()
print(day1)
print(f'Żyjesz {(day2 - day1).days} dni!')
#%%
import datetime
dzień = datetime.datetime.today() + datetime.timedelta(hours=4)
print(dzień)
dzień = datetime.datetime.today() + datetime.timedelta(days=7)
print(dzień)
dzień = datetime.datetime.today() + datetime.timedelta(days=31)
print(dzień)
dzień = datetime.datetime.today() + datetime.timedelta(hours=30)
print(dzień)
dzień = datetime.datetime.today() + datetime.timedelta(minutes=25)
print(dzień)