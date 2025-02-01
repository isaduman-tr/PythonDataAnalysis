import numpy as np

dizi = np.array([10,20,30,40,50,60,70,80,90])
dizi1 = np.array([100,110,120,130,140,150,160,170,180])

# boolenMask = dizi >= 50
secilmis = (dizi > 50) & (dizi < 90)

# print(boolenMask)
print("50 ve 90 arasındaki sayılar : ",dizi[secilmis])

