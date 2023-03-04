import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# 利用する API を指定する
api_scope = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']

# 先ほどダウンロードした json パスを指定する
credentials_path = os.path.join(os.path.expanduser('~'),
                '/Users/nkohei/Workspace/Tweetbot/auth/teak-spot-379405-85d7b008753b.json')

# json から Credentials 情報を取得
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, api_scope)

# 認可されたクライアントを得る
gspread_client = gspread.authorize(credentials)

# スプレッドシートの名前を指定する（日本語も使えます）
spread_sheet_name = "test_sheetdb"

# 一つ目のシートを開く
sheet = gspread_client.open(spread_sheet_name).sheet1

# D 列の 22行目の情報を表示
print(sheet.acell('D12').value)

# A 列の 1行目の内容を更新する
sheet.update_acell('A11', 'Hello, Sheets API')