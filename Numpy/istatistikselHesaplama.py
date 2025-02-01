import numpy as np

dizi = np.array([1,2,3,4,56])

minValue = np.min(dizi)
maxValue = np.max(dizi)
toplam = np.sum(dizi)
kumeToplam = np.cumsum(dizi)

print("En yüksek ve En düşük değerler : ",maxValue,"-",minValue)
print(kumeToplam)
