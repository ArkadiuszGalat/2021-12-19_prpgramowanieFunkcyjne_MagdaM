#%%
import matplotlib.pyplot as plt

x_values = list(range(1,10))
y_values = [x**2 for x in x_values]
fig, ax = plt.subplots()
ax.plot(x_values, y_values, c ="red", linewidth=3, )
ax.set_title("kwadraty", fontsize = 20)
ax.set_xlabel('liczby', fontsize=16)
ax.set_ylabel('kwadraty liczb', fontsize=16)
plt.show()

#ax.plot(x, x**2, label='quadratic')
# %%
