#PieChartEx3.py--plt.pic(values,labels,explode,shadow)
from matplotlib import pyplot as plt
sports=[10,5,5,10,10]
spnames=["Football","Hockey","Cricket","Basketball","Badminton"]
plt.pie(sports,labels=spnames,explode=[0.1,0,0,0,0],shadow=True)
plt.show()
