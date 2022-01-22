#%%
#https://docs.python.org/3/library/collections.html
import collections
lista = ['yes', "yes", 'no', 'no', 'yes', True]
counter = collections.Counter(lista)
print(counter)