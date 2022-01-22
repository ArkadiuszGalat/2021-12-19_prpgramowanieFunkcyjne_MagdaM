#%%
import timeit
code2 = """numbers=[]
for i in range(10):
    numbers.append(i)
"""

code1 = '''numbers=[x for x in range(10)]'''

t1 = (timeit.timeit(code1, number =100000))
t2 = (timeit.timeit(code2, number =100000))
if t1 < t2:
    print(code1)
else:
    print(code2)
print(f't1 = {t1}')
print(f't2 = {t2}')
