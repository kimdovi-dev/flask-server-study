from flask import Flask
from flask_cors import CORS
import requests
import pandas as pd
import io
import main as main

app = Flask(__name__)
CORS(app, origins="http://localhost:3000", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)


@app.route('/')
def datas():
  res = main.main()
  return res

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3003, debug=True)