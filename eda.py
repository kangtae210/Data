# EDA로 데이터를 확인하고, 전처리를 하는 방법

# EDA : Exploratory Data Analysis(탐색적 데이터 분석)
# 수집한 데이터를 다양한 각도에서 관찰하고 이해하는 과정
# 데이터를 분석하기 전에 그래프나 통계적인 방법으로 자료를 직관적으로 바라보는 과정
# 데이터 전처리(Data Preprocessing)이란 분석에 적합하게 데이터를 가공하는 작업을 의미한다.

#1. pandas 라이브러리
import pandas as pd  #pandas 라이브러리를 pd로 가져옴

#2. CSV 파일 불러오기
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

#3. 행과 열의 갯수를 관찰하기
#print("train.csv sahpe =>",train.shape)
#print("test.csv sahpe =>",test.shape)


#4. 파이썬 데이터 확인하기 head(int n)와 tail(int n)
# 상, 하위 n개의 데이터를 출력하는 메서드
#train.head(10)
#train.tail(10)


#5. 결측치 확인하기 isnull() 메서드
# isnull() 메서드는 DataFrame에서 데이터가 비어있으면 True를 반환한다.
#check_null = train.isnull().sum()
#print(check_null)


# 6. info()는 DataFrame의 개략적인 정보를 출력하는 메서드이다.
print("*************** I N F O ***************")
train.info()       #반환하는 값은 없음!
print("*************** I N F O ***************")
test.info()


#7. dropna() 메서드는 결측치를 삭제한다.
#   fillna() 메서드는 데이터의 결측치를 인자값으로 채운다.
train.dropna()
test.fillna(0)





































































