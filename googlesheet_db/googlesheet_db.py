import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


API_SCOPE1 = 'https://www.googleapis.com/auth/spreadsheets'
API_SCOPE2 = 'https://www.googleapis.com/auth/drive'
PATH_TO_JSON = '/Users/nkohei/Workspace/personal-projects/auth/teak-spot-379405-85d7b008753b.json'
SHEET_NAME = 'test_sheetdb_123'
EMAIL = 'kohei.nishitani@gmail.com'

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

    def check_workbooks(self, gspread_client, workbookname):
        workbook_list = []
        for i in gspread_client.openall():
            workbook_list.append(i.title)
        # print(workbook_list)
        if workbookname in workbook_list:
            return True
        else:
            return False

    def create_workbook(self, gspread_client ,workbookname):
        if self.check_workbooks(gspread_client, workbookname):
            pass
        else:
            if workbookname not in [sh.title for sh in gspread_client.openall()]:
                sh = gspread_client.create(workbookname)
                sh.share(EMAIL, perm_type='user', role='writer')

            print('new workbook created, please check email')



# Usage example
api = ApiSetting()
credentials = api.api_scope([API_SCOPE1,API_SCOPE2])
gs_handler = GoogleSpreadsheetHandler()
gspread_client = gs_handler.authorize(credentials)
gs_handler.create_workbook(gspread_client, SHEET_NAME)

#checking
# gs_handler.check_workbooks(gspread_client, SHEET_NAME)

# # # open sheet
# # sheet = gspread_client.open(spread_sheet_name).sheet1

# # # D 列の 22行目の情報を表示
# # print(sheet.acell('D12').value)

# # # A 列の 1行目の内容を更新する
# # sheet.update_acell('A11', 'Hello, Sheets API')