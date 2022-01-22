#%%
import modul1

modul1.calc_average([1,2])

#%%
from modul1 import calc_max
calc_max([1,2,16,13])

#%%
import pakiet.modul_w_pakiecie
pakiet.modul_w_pakiecie.funkcja(100)

#%%
from pakiet.modul_w_pakiecie import funkcja
funkcja(1000)
#%% obliczanie ile będzie ziaren na 64 polu szachownicy
ziarna = 1
for i in range(1,64):
    ziarna = ziarna + funkcja(ziarna)
    print(f'{i+1} - {ziarna}')
