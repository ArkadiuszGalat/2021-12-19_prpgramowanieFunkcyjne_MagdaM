#%%
#Numeric and mathematical values
#https://docs.python.org/3/library/statistics.html
import statistics
numbers = [5,56,117,345,901, 43, 234,34.5, 67,7, 456, 7,4]
print(round(statistics.mean(numbers),2))
print(round(statistics.median(numbers),2))

#%%
from statistics import NormalDist
IQ = NormalDist(mu=100, sigma=5)

#prawdopodobieństwo że osoba w populacji bedzie miała IQ 100 do 104
prob = round((IQ.cdf(104)-IQ.cdf(100)),4)
print(prob)
#cdf zwraca prawdopodobienstwo że jest 104 lub mniej