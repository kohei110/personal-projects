import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


API_SCOPE1 = 'https://www.googleapis.com/auth/spreadsheets'
API_SCOPE2 = 'https://www.googleapis.com/auth/drive'
PATH_TO_JSON = '/Users/nkohei/Workspace/personal-projects/auth/teak-spot-379405-85d7b008753b.json'
SHEET_NAME = 'test_sheetdb'

class ApiSetting:
    def __init__(self) -> None:
        pass

    def api_scope(self, apiscope_list: list):
        # create api list
        api_scope = apiscope_list

        # connect to json key
        credentials_path = os.path.join(os.path.expanduser('~'), PATH_TO_JSON)
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, api_scope)
        return credentials

class GoogleSpreadsheetHandler:
    def __init__(self)->None:
        pass

    def authorize(self, credential):
    # authorise
        gspread_client = gspread.authorize(credential)
        return gspread_client
    
    def create_workbook(self, workbookname):
        print(gspread_client.openall())

    # def createNewSheetIfNotExist(title):
    #     if title not in [sh.title for sh in gc.openall()]:
    #         gc.create(title)
    #     print([sh.title for sh in gc.openall()])

credential = ApiSetting().api_scope([API_SCOPE1, API_SCOPE2])
gspread_client = GoogleSpreadsheetHandler().authorize(credential)
GoogleSpreadsheetHandler().create_workbook('test_sheetdb')

# spread_sheet_name = SHEET_NAME

# # open sheet
# sheet = gspread_client.open(spread_sheet_name).sheet1

# # D 列の 22行目の情報を表示
# print(sheet.acell('D12').value)

# # A 列の 1行目の内容を更新する
# sheet.update_acell('A11', 'Hello, Sheets API')