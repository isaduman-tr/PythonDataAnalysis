import numpy as np

dizi = np.array([1,2,3,4,5,6])
dizi1  = np.array([1,2,3,4,5])
dizi2 = np.array([6,7,8,9,10])
dizi3 = np.array([[1,2,3],[4,5,6]])
dizi4 = np.array([[7,8,9],[10,11,12]])
dizi5 = np.array([[8,9,10,11],[12,13,14,15]])


birlesik_dizi = np.concatenate((dizi1,dizi2))
birlesik_dizi2 = np.hstack((dizi3,dizi4))
birlesik_dizi3 = np.vstack((dizi3,dizi4))


bol = np.split(dizi,3)
bol2 = np.hsplit(dizi5,2)
bol3 = np.vsplit(dizi5,2)
# print(bol2)
# print(bol3)
# print(birlesik_dizi)
# print("-"*50)
# print(birlesik_dizi2)
# print("-"*50)
# print(birlesik_dizi3)
# print("-"*50)
