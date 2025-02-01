import numpy as np

dizi = np.array([1,2,3,4,5,6])

yeniDizi = dizi.reshape((2,3)) #2 satır 3 sütunluk hale gelir

matris = np.array([[1,2],[3,4],[5,6]])

tekBoyut = matris.reshape(-1)

otosutun = dizi.reshape(2,-1)


print(yeniDizi)
print("-"*50)
print(tekBoyut)
print("-"*50)
print(otosutun)