#http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2635055300

from urllib.request import urlopen
from bs4 import BeautifulSoup

target = \
    urlopen("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2635055300").read().decode('utf-8')

# print(target)

soup = BeautifulSoup(target, 'html.parser')
# print(soup)

print('---------------------------------')
# first_temp = soup.find('temp')
# print(first_temp)
#
# all_tmp = soup.find_all('temp')
# print(all_tmp)
#
# data_temp = soup.find('data', {'seq' : '17'})
# print(data_temp)

dataList = soup.select('data')
# print(dataList)

data_first = dataList[0]
print(data_first)