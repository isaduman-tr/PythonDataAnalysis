import numpy as np
dizi1 = np.array([1,2,3,4,5])
dizi2 = np.array([1,1,2,1,1])

toplam = np.add(dizi1,dizi2)
fark = np.subtract(dizi1,dizi2)
carp = np.multiply(dizi1,dizi2)
bol = np.divide(dizi1,dizi2)
ussunual = np.power(dizi1,2)
karekok = np.sqrt(dizi1)
ortalama = np.mean(dizi1)
varyans = np.var(dizi2)
standartsapma = np.std(dizi2)


print(varyans)