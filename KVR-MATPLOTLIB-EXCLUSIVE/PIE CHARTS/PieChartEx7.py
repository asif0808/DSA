#PieChartEx7.py
from matplotlib import pyplot as plt
epn=int(input("Enter How Many Exp Names:"))
expnames=[]
for  i in range(1,epn+1):
    ename=input("Enter {} Exp Name:".format(i))
    expnames.append(ename)
print("*"*50)
expvalues=[]
for  i in range(1,epn+1):
    expval=input("Enter {} Exp Value:".format(i))
    expvalues.append(int(expval))
cols=['rosybrown', 'moccasin', 'lightyellow', 'darkseagreen']
plt.pie(expvalues,labels=expnames,explode=[0.1,0,0,0],colors=cols,startangle=0,autopct='%0.0f%%',
        wedgeprops={'linewidth':4,'edgecolor':"red"})
plt.show()