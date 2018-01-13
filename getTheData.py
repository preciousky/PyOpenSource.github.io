import requests ,bs4
import csv


places = []
datas = [['city','aqi','class','date','time(XX:00)']]

filename = 'cityList.csv'
with open(filename) as f:
    reader = csv.reader(f)
    places = list(reader)


for place in places:
    print(place)
    url = 'http://www.air-level.com/air/'+place[1]
    print(url)
    req = requests.get(url)
    req.encoding = 'UTF#8'
    # print(req.text)

    soup = bs4.BeautifulSoup(req.text,'lxml')
    aqi_class = soup.find(attrs = {'class':'aqi-bg'}).text
    date_time = soup.find(attrs = {'class':'label label-info'}).text
    print(aqi_class)
    aqi_class = aqi_class.split()
    date_time = date_time.split()
    year = date_time[0][0:date_time[0].index('年')]
    month = date_time[0][date_time[0].index('年')+2:date_time[0].index('月')]
    day= date_time[0][date_time[0].index('月')+2:date_time[0].index('日')]
    time = date_time[1][0:2]
    datas.append([place[0],int(aqi_class[0]),aqi_class[1],year+'_'+month+'_'+day,time])
    filename = 'aqiData'+ year + '_' + month + '_' + day + '_' + time +'.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)