from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import requests
import pandas as pd
import io

app = Flask(__name__)
api = Api(app)
CORS(app, origins="http://localhost:3000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

class main(Resource):  
  ...
  ...
  def get(self):
    result_msg, result_data = CSVReaderToJson()
    return {'resultMsg': result_msg, 'message': result_data}

def CSVReaderToJson():
  result_data = []
  result_msg = 'FAIL'
  try:
    csv_url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
    url_req = requests.get(csv_url).content
    csv_data = pd.read_csv(io.StringIO(url_req.decode('utf-8')))
    row_count = csv_data.shape[0]
    column_count = csv_data.shape[1]
    column_names = csv_data.columns.tolist()
    final_row_data = []
    for index, rows in csv_data.iterrows():
      final_row_data.append(rows.to_dict())
    result_data = {'rows': row_count, 'cols': column_count, 'columnNames': column_names, 'rowData':final_row_data}
    result_msg = 'SUCCESS'
    print('Done')
  except:
    result_data.append({'message':'Unable to process request'})
  return result_msg, result_data



api.add_resource(main, '/')
app.run(host="0.0.0.0", port=3003, debug=True)