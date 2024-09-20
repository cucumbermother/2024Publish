# 실습2 : csv 와 맷플롭립 활용
# 주제 : '삼성전자' 의 최근 30일간 주가를 시각화
import csv
import matplotlib.pyplot as plt
# [1] 데이터 수집
    # 1. '한국거래소' 접속 https://www.krx.co.kr/main/main.jsp
    # 2. 상단 메뉴에 '정보 데이터 시스템' 클릭 http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd
    # 3. 일자별 조회 : 1개월 조회
    # csv 파일로 다운로드 받기

# [2] 데이터를 리스트로 가져오기
파일객체 = open('data_1258_20240920.csv', 'r')    # 1. 파일 읽기모드 객체
import csv
읽어온내용 = csv.reader(파일객체)# 2. csv 파일 읽기 # import csv 필수
삼성전자주가목록 = list( 읽어온내용 ) # 3. 읽어온 데이터를 리스트 타입으로 변환
# print(삼성전자주가목록)

종가목록 = []
날짜목록 = []
for 행 in 삼성전자주가목록[1:]:
    # print(행)
    # print(행[1]) # 두번째 열에 '종가'
    # 종가를 시각화
    종가목록.append( int(행[ 1 ])) # 종가를 정수타입으로 변환후 리스트에 담아주기
    날짜목록.append( 행[0].split('/')[1] + '/' + 행[0].split('/')[2])

# 리스트 뒤집기
종가목록.reverse()
날짜목록.reverse()

plt.title('line chart')
plt.plot( 날짜목록,종가목록,color = "blue" )
plt.show()

# [3] 반복문을 이용한 2차원 리스트 호출하기