#%%
#wyniki głosowania w postaci słowników
import collections
city1  ={'yes':250, 'no':138, None:17}
city2  ={'yes':192, 'no':232, None:19}
count_c1 = collections.Counter(city1)
count_c2 = collections.Counter(city2)
print(count_c1)
print(count_c2)
total = count_c1+count_c2
print(total)
print(total['yes'])
print(f'Głosów na tak było: {total["yes"]}')
