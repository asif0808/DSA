#PieChartEx4.py--plt.pic(values,labels,explode,shadow,colors,startangle)
from matplotlib import pyplot as plt
plt.title("Sports View")
sports=[10,5,5,10,10]
spnames=["Football","Hockey","Cricket","Basketball","Badminton"]
cols=["gold","hotpink","cyan","blue","purple"]
plt.pie(sports,labels=spnames,explode=[0.1,0,0,0,0],shadow=True,colors=cols,startangle=90)
plt.legend(title="Sports")
plt.show()
