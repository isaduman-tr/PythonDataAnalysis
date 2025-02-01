import numpy as np
data = np.loadtxt("Data1.txt",delimiter=" ")

rowSum = np.sum(data,axis=1)

outputData = np.column_stack((data,rowSum))

np.savetxt("outputData.txt",outputData,fmt="%d",delimiter=" ")
print("Kayıt işlemi tamamlandı")