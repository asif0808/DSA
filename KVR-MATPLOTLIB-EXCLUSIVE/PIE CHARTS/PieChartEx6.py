#PieChartEx6.py
from matplotlib import pyplot as plt
plt.title("Expenditure",color="red",fontweight="bold",fontsize=20)
exprs=[4000,5400,2800,1400]
expnames=["Rent","Food","Clothing","Savings"]
cols=['rosybrown', 'moccasin', 'lightyellow', 'darkseagreen']
plt.pie(exprs,labels=expnames,explode=[0.1,0,0,0],colors=cols,startangle=0,autopct='%0.0f%%',
        wedgeprops={'linewidth':4,'edgecolor':"red"})
plt.show()