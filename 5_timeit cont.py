#%%
import timeit
code2 = """numbers=[]
for i in range(10):
    numbers.append(i)
"""

code1 = '''numbers=[x for x in range(10)]'''

t1 = (timeit.timeit(code1, number =100000))
t2 = (timeit.timeit(code2, number =100000))
results = {'code1':t1, 'code2':t2}
print(results)
new_results = sorted(results.items(), key=lambda x: x[1])
#bezpośrednio na dict nie mozemy użyć funkcji "sorted", dlatego metodą .items() zamieniamy ją na listę tupli. x to kolejne tuple i sortujemy po drugim elemencie tupli czyli czasie.
print(new_results)
print(new_results[0][0])
print(f't1 = {t1}')
print(f't2 = {t2}')
#%%