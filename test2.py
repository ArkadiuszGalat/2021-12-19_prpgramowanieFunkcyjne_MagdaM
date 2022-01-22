#%%
import datetime
day1 = input('Podaj pierwszą datę w formacie rrrr-mm-dd: ')
day2 = input('Podaj drugą datę w formacie rrrr-mm-dd: ')

day1list = day1.split('-')
day2list = day2.split('-')

#print (day1list)
date1 = datetime.date(int(day1list[0]),int(day1list[1]),int(day1list[2]))
date2 = datetime.date(int(day2list[0]),int(day2list[1]),int(day2list[2]))
#jest funkcja 
# Conversely, the datetime.strptime() class method creates a datetime object from a string representing a date and time and a corresponding format string.
print(date1)
print(date2)
print(f'Żyjesz już na tym świecie {date2-date1} dni')
print(f'Żyjesz już na tym świecie {(date2-date1).days} dni')