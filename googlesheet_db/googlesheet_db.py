import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


API_SCOPE1 = 'https://www.googleapis.com/auth/spreadsheets'
API_SCOPE2 = 'https://www.googleapis.com/auth/drive'
PATH_TO_JSON = '/Users/nkohei/Workspace/Tweetbot/auth/teak-spot-379405-85d7b008753b.json'
SHEET_NAME = 'test_sheetdb'

# create api list
api_scope = [API_SCOPE1, API_SCOPE2]

# connect to json key
credentials_path = os.path.join(os.path.expanduser('~'),
                PATH_TO_JSON)
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, api_scope)

# authorise
gspread_client = gspread.authorize(credentials)

# 
spread_sheet_name = "test_sheetdb"

# 一つ目のシートを開く
sheet = gspread_client.open(spread_sheet_name).sheet1

# D 列の 22行目の情報を表示
print(sheet.acell('D12').value)

# A 列の 1行目の内容を更新する
sheet.update_acell('A11', 'Hello, Sheets API')