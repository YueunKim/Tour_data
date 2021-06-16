
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# 1. URL 파라미터 분리하기.
# Service URL - 관광사진 갤러리 조회
xmlUrl = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList'

API_key = unquote('IB3QISfc1ZNgH+CPuMgUoMEgSvbuGsMig/eIFRGai1inB3AdCo4z2g5hCVdbd8dMwf6DYoFP3bnqO+s7Iplmww==')
queryParams = '?' + urlencode(    # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
    {
        quote_plus('ServiceKey') : API_key,    # 필수 항목 1 : 서비스키 (본인의 서비스키)
        quote_plus('MobileOS') : 'ETC',          # 필수 항목 2 : OS 구분 (IOS - 아이폰, AND - 안드로이드, WIN - 윈도우폰, ETC)
        quote_plus('MobileApp') : 'AppTest',         # 필수 항목 3 : 서비스명=어플명
        quote_plus('numOfRows') : '3104'            # 옵션 : 입력값은 데이터 참고문서 참고, 입력 안할시 10개의 데이터만 보여짐.
    }
)

response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
# xmlobj    # 디버깅용

rows = xmlobj.findAll('item')
# rows    # 디버깅용 - item 태그 단위로 구분
columns = rows[0].find_all()
# columns    # 디버깅용.
# columns[0].name    # 디버깅용.
# columns[0].text    # 디버깅용.

# 모든 행과 열의 값을 모아 매트릭스로 만들어보자.
rowList = []
nameList = []
columnList = []

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()
    
    columnsLen = len(columns)
    for j in range(0, columnsLen):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
        if i == 0:
            nameList.append(columns[j].name)
        # 컬럼값은 모든 행의 값을 저장해야한다.    
        eachColumn = columns[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)
    columnList = []    # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)
    
result = pd.DataFrame(rowList, columns=nameList)
result.to_excel('VSC_TourPhotos.xlsx')
result