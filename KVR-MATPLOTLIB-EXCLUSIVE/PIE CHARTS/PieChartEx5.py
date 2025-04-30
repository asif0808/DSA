#PieChartEx5.py--plt.pic(values,labels,explode,shadow,colors,startangle,wedgeprop)
from matplotlib import pyplot as plt
plt.title("Games View",color="green",fontweight="bold",fontsize=20)
sports=[10,5,5,10,10]
spnames=["FootBall","Hockey","Cricket","Basketball","Badminton"]
cols=["gold","green","hotpink","cyan","blue"]
plt.pie(sports,labels=spnames,explode=[0.1,0,0,0,0],colors=cols,startangle=90,autopct='%0.2f%%',
        wedgeprops={'linewidth':4,'edgecolor':"grey"})
plt.show()