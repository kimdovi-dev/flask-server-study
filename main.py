import pandas as pd


def sidebar(data):
    
    #주문정보에서 존재하는 년도만 추출
    year = list(data['paymentcomplete_year'].drop_duplicates().sort_values())
    #year 리스트 제일 앞에 Year 추가 - selectbox 만들시 [ year, 2018, 2019] 형태로 만들기 위해
    year.insert(0, 'Year')
    
    quarter = list(data['paymentcomplete_Q'].drop_duplicates().sort_values())
    quarter.insert(0, 'Quarter')
    
    month = list(data['paymentcomplete_month'].drop_duplicates().sort_values())
    month.insert(0, 'Month')
    
    belong = list(data['belong'].drop_duplicates().sort_values())
    belong.insert(0, 'Belong')
        
    # 각 값들의 변화를 감지 위해서 return
    return year, month, quarter, belong


## sidebar
def main() :
     #주문, 고객정보 데이터 로드
    data = pd.read_csv('data/20230111_join_order_customer.csv', encoding='cp949')
     #BI에 필요한 칼럼으로 데이터 구성
    data = data[['orderSheetId','memberNo', 'originTotalProductPrice', 'region', '카데고리(대)', 
                        '카데고리(중)', 'brand','paymentcomplete_year',
                        'paymentcomplete_Q', 'paymentcomplete_month', 'siteType', 'memberStatus',
                        'gender','membershipLevel', 'belong', 'name']]
    sidebarVal = sidebar(data)
    return [sidebarVal]