# [1] 파이썬에서 시각화.txt 할수 있는 객체 모듈 가져오기
    # import : 현재 파일 외부에 있는 함수 또는 객체 가져오기 위한 키워드
    # as : 객체 또는 함수의 별칭 * 함수 또는 객체 이름이 길거나 복잡할때

import matplotlib.pyplot as plt

# - 다양한 시각화.txt(차트) 옵션을 추가

plt.title('chart 1 ') # [3] 차트 제목

YDATA = [ 5 , 2 , 7 , 1 ] # [4] Y축 데이터

plt.plot(YDATA) # [5] 선차트에 y축 데이터 대입

#[2] 시각화.txt(차트) 실행

plt.show()


plt.title('chart 2')

XDATA = [ 10,20,30,40 ] # X축 데이터
YDATA = [ 50,2,9,16 ] # Y축 데이터
plt.plot(XDATA ,  YDATA) # X축과 Y축 데이터를 선차트에 대입
plt.show()


# (3) 제품명 판매량 시각화.txt
plt.title('chart3')
XDATA = [ 'cola', 'cider' , 'fanta' , 'americano' ]
YDATA = [ 102 , 130, 96 , 200 ]
plt.plot( XDATA,YDATA , label = 'sales')
plt.xlabel('product')
plt.ylabel('sales')
plt.grid()
plt.legend()
plt.show()