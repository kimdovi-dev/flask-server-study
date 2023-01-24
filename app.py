from flask import Flask, request
from flask_cors import CORS
import requests
import pandas as pd
import io
import main as main
import sales_per_region_graph as sales

app = Flask(__name__)
CORS(app, origins="http://localhost:3000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

#주문, 고객정보 데이터 로드
data = pd.read_csv('data/20230111_join_order_customer.csv', encoding='cp949')
#BI에 필요한 칼럼으로 데이터 구성
data = data[['orderSheetId','memberNo', 'originTotalProductPrice', 'region', '카데고리(대)', 
                    '카데고리(중)', 'brand','paymentcomplete_year',
                    'paymentcomplete_Q', 'paymentcomplete_month', 'siteType', 'memberStatus',
                    'gender','membershipLevel', 'belong', 'name']]

@app.route('/filter')
def selectOption():
  selectYear = request.args.get('year')
  selectQ = request.args.get('quarter')
  selectMonth = request.args.get('month')
  selectBelong = request.args.get('belong')
  sales.region(selectYear, selectQ, selectMonth, selectBelong, data)
  resultRegion = sales.region(selectYear,selectQ, selectMonth, selectBelong,data)
  return ''

### data fetch에 필요한 데이터 가공 
@app.route('/')
def index():
  res = main.main(data)
  return res

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3003, debug=True)