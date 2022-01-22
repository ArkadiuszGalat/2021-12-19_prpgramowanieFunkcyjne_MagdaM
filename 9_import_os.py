#%%
import os
print(os.getcwd())
print(os.listdir())
#%%
pliki_na_m = sorted([name for name in os.listdir() if name.startswith('m')])
print(pliki_na_m)
pliki_na_m = [name for name in os.listdir() if name[0]=='m']
print(pliki_na_m)
