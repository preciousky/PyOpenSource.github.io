import csv

dalian = ['大连']
daxinganlingdiqu = ['大兴安岭地区']
changchun = ['长春']
for i in range(12,23):
    filename = 'aqiData2018_1_2_'+ str(i)+'.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        places = list(reader)
    for place in places:
        if(place[0] == '大连'):
            dalian.append(place[1])
        if(place[0] == '大兴安岭地区'):
            daxinganlingdiqu.append(place[1])
        if(place[0] == '长春'):
            print(place[1])
            changchun.append(place[1])

datas = [dalian, daxinganlingdiqu, changchun]


print(datas)
with open('cityToShow.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)