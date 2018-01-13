import matplotlib.pyplot as plt
from pylab import *
import csv


filename = 'cityToShow.csv'
with open(filename) as f:
    reader = csv.reader(f)
    places = list(reader)

x = [12, 13, 14, 15, 16,17,18,19,20,21,22]

y0 = []
y1 = []
y2 = []


for i in range(1,12):
    y0.append(int(places[0][i]))
for i in range(1,12):
    y1.append(int(places[1][i]))
for i in range(1,12):
    y2.append(int(places[2][i]))

 
plt.figure()  
plt.plot(x,y0,label="$dalian$")  
plt.savefig("dalian.jpg")   
plt.plot(x,y1,label="$daxinganling$")  
plt.savefig("daxinganlingdiqu.jpg")   
plt.plot(x,y2,label="$changchun$") 
plt.savefig("changchun.jpg")   