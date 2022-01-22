#%%
import os
#os.mkdir('months')

months_list=[f'{str(i).zfill(2)}_raport' for i in range(1,13)]
print(months_list)
for month in months_list:
    path = os.path.join('months', month)
    os.mkdir(path)