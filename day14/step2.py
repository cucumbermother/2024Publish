#[1] 맷플롭립 모듈

import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend

# [1] 선차트
    #  데이터 수집
x = ['Kim' , 'Lee', 'Park']
y1 = [ 10 , 56 , 93 ]
y2 = [ 57 , 82 , 63 ]
    # 차트 설정
plt.title( 'Member point' )
plt.plot(x , y1 , label = 'point1' , color = 'red' , linewidth = 3 , marker = 'o') # 첫번째 항목 추가
plt.plot(x , y2 , label = 'point2' , color = 'pink' , linewidth = 3 , marker = '*') # 두번째 항목 추가
plt.legend() # 범례 : 항목 label(이름)이 표시되는 구역 표시
plt.show()

# [2] 막대 차트

plt.title( 'bar chart' )
plt.bar( x , y1 , label = 'point1')
plt.bar( x , y2 , label = 'point2' )
plt.show()

# [3] 산점도 : x축과 y축 값의 관계 시각화 , x값과 y값이 만나는 지점(포인트) 표시
x = [ random.random() for _ in range(50)] # random.random() : 0 ~ 1 사이의 난수 생성
y = [ random.random() for _ in range(50)] # for _ in range(50) : 0부터 49 까지 반복하는 반복문
                                          # 0 부터 49Rkwl 1씩 증가하면서 (50회반복) 난수 생성
    # [ [ random.random() for _ in range(50)] ] : [ 표현식 for 반복변수 in 리스트/range() ] 안에서 for 활용 : 리스트 컴프리헨션
plt.scatter ( x , y )
plt.show()


# [4] 원형(파이) : 백분율( 한바퀴를 100% 기준 )
size = [ 82 , 100 ] # 182(100%) 100( % ) 52 ( % )
labels = ['M' , "W"]  # '남' '여'
plt.pie( size , labels = labels , autopct= '% .1f%%' )
plt.show()


# 실습 1 : 학생의 시험 성적 데이터를 시각화(선차트) 하기
s1 = [ 80 , 73 , 97 ,]  # 1학년때 중간고사, 기말고사 , 모의고사 점수
s2 = [ 92 , 100 , 98 ] # 2학년때 중간고사, 기말고사 , 모의고사 점수
s3 = [ 100 , 98 , 99 ] # 3학년때 중간고사, 기말고사 , 모의고사 점수

# 차트에서 한글 표현하는 방법 # 차트에 사용할 폰트 설정 코드

plt.rcParams['font.family'] = 'Malgun Gothic'
a = [ "중간고사" , "기말고사" , "모의고사" ]
plt.title('유나의 시험 성적 하트 ')
plt.plot( a , s1 ,  label = '1학년 성적' ,color = 'red' )
plt.plot( a , s2 , label = '2학년 성적' ,color = 'blue' )
plt.plot( a, s3 , label = '3학년 성적' , color = 'green' )
plt.legend()
plt.show()