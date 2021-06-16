# http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryDetailList?serviceKey=paA73p6ie7l%2BT%2B7%2F%2FBPJ4BIOZ7tDKBOrN8ccEXweaj9RjIjBbCNrs3MRX09rmWnphSIuaLFK4Cvs%2BN3Ge58wZQ%3D%3D&pageNo=1&numOfRows=10&MobileOS=ETC&MobileApp=AppTest&title=%EC%9D%B4%ED%83%9C%EC%9B%90%EA%B1%B0%EB%A6%AC


from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus,unquote
import xml.etree.ElementTree as ET
from pandas import Series, DataFrame
# from urllib2 import Request, urlopen
# from urllib import urlencode, quote_plus

# API_key = unquote('paA73p6ie7l%2BT%2B7%2F%2FBPJ4BIOZ7tDKBOrN8ccEXweaj9RjIjBbCNrs3MRX09rmWnphSIuaLFK4Cvs%2BN3Ge58wZQ%3D%3D')
API_key = unquote('paA73p6ie7l+T+7//BPJ4BIOZ7tDKBOrN8ccEXweaj9RjIjBbCNrs3MRX09rmWnphSIuaLFK4Cvs+N3Ge58wZQ==')

url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('MobileOS') : 'ETC', quote_plus('MobileApp') : 'AppTest', quote_plus('arrange') : 'A' })
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('MobileOS') : 'ETC', quote_plus('MobileApp') : 'AppTest', quote_plus('title') : '%EC%9D%B4%ED%83%9C%EC%9B%90%EA%B1%B0%EB%A6%AC' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read().decode('utf-8')
root = ET.fromstring(response_body)
# print(response_body)

image_url = root.find('body').find('items').find('item').find('galWebImageUrl').text
print(image_url)

raw_data = {'url': [image_url]}
data = DataFrame(raw_data)
print(data)
data.to_excel('url_data.xlsx')




# def Read():
#     request = Request(url + queryParams)
#     request.get_method = lambda: 'GET'
#     response_body = urlopen(request).read().decode('utf-8')
#     root = ET.fromstring(response_body)

# def image(): #Search
#     # Read() #API Read
#     for image_url in root.find('body').find('items').find('item').find('galWebImageUrl'):
#         print(image_url.tag, ':', image_url.text)
#     # image_url = root.find('body').find('items').find('item').find('galWebImageUrl').text()
#     # print(image_url)


# for a in root.find('body').find('items').find('item').find('galTitle').text:
#     print(a)


# if __name__ == "__main__":
#     image()





##### 미세먼지데이터 #####
# from urllib.request import Request, urlopen
# from urllib.parse import urlencode, quote_plus,unquote
# import xml.etree.ElementTree as ET

# txt_Output = True #txt?��?���? 출력?�� 것인�?? True : ?�� | False : ?��?��?��
# cmd_Output = True #python?�� 바로 출력?�� 것인�?? True : ?�� | False : ?��?��?��

# #File Set
# if txt_Output == True :
#     Out_file = open("Output.txt", 'w')
#     Out_file.write(u"Write Start\n")
#     Out_file.close()

# #API Set 1
# # API_key = unquote('paA73p6ie7l%2BT%2B7%2F%2FBPJ4BIOZ7tDKBOrN8ccEXweaj9RjIjBbCNrs3MRX09rmWnphSIuaLFK4Cvs%2BN3Ge58wZQ%3D%3D')
# API_key = unquote('paA73p6ie7l+T+7//BPJ4BIOZ7tDKBOrN8ccEXweaj9RjIjBbCNrs3MRX09rmWnphSIuaLFK4Cvs+N3Ge58wZQ==')
# url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('itemCode') : 'PM10', quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })

# #API Call(For dustcheck)
# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read().decode('utf-8')
# root = ET.fromstring(response_body)
# # print(response_body)


# def Read(): #API Read
#     request = Request(url + queryParams)
#     request.get_method = lambda: 'GET'
#     response_body = urlopen(request).read().decode('utf-8')
#     root = ET.fromstring(response_body)
#     # print(response_body)

# def dustcheck(city): #Search
#     Read() #API Read
#     dustinfo = root.find('body').find('items').find('item').find(city)
#     if txt_Output == True :
#         Out_file = open("Output.txt", 'a')
#         Out_file.write(city + u"\n" + dustinfo.text)
#     if cmd_Output == True :
#         print(city + ' : ' + dustinfo.text + u' ug/m3')

#     if 0 < int(dustinfo.text) <= 30: #좋음
#         if cmd_Output == True :
#             print(city + u" : 좋음\n")
#         if txt_Output == True :
#             Out_file.write(u" -> Good\n")
#     elif 30 < int(dustinfo.text) <= 80:  #보통
#         if cmd_Output == True :
#             print(city + u" : 보통\n")
#         if txt_Output == True :
#             Out_file.write(u" -> Nomal\n")
#     elif 80 < int(dustinfo.text) <= 150:  #?��?��
#         if cmd_Output == True :
#             print(city + u" : ?��?��\n")
#         if txt_Output == True :
#             Out_file.write(u" -> Bad\n")
#     elif 150 < int(dustinfo.text):  #매우 ?��?��
#         if cmd_Output == True :
#             print(city + u" : 매우 ?��?��\n")
#         if txt_Output == True :
#             Out_file.write(u" -> Very Bad\n")

#     if txt_Output == True :
#         Out_file.close()

# if __name__ == "__main__":
#     dustcheck('daejeon')


# from urllib import Request
# from urllib.parse import urlencode, quote_plus
# # from urllib import urlencode, quote_plus
# from urllib.request import urlopen

# url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '?��비스?��', quote_plus('serviceKey') : '-', quote_plus('returnType') : 'xml', quote_plus('numOfRows') : '100', quote_plus('pageNo') : '1', quote_plus('searchDate') : '2020-11-14', quote_plus('InformCode') : 'PM10' })

# request = urllib.request.Request(url + queryParams)
# # request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print(response_body)




