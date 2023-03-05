import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import yaml

## Step1 enable API at GCP
## https://console.cloud.google.com/apis/api/sheets.googleapis.com/overview 
## https://console.cloud.google.com/apis/api/drive.googleapis.com/overview

## Step2 Create service account and get json key
## https://console.developers.google.com/iam-admin/serviceaccounts

## Step3 Get Service account from json key file and add it to as gspreadsheet share account
## SERVICE_ACCOUNT@PROJECT.iam.gserviceaccount.com

class ApiSetting:
    def __init__(self):
        pass

    def api_scope(self, apiscope_list: list):
        # create api list
        api_scope = apiscope_list
        # connect to json key
        try:
            credentials_path = os.path.join(os.path.expanduser('~'), PATH_TO_JSON)
            credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, api_scope)
            return credentials
        except Exception as e:
            print(f"Failed to get credentials: {str(e)}")
            return None


class GoogleSpreadsheetHandler:
    def __init__(self)->None:
        pass

    def authorize(self, credential):
        # authorise
        try:
            gspread_client = gspread.authorize(credential)
            return gspread_client
        except Exception as e:
            print(f"Failed to authorise: {str(e)}")
            return None

    def check_workbooks(self, gspread_client, workbookname):
        try:
            workbook_list = []
            for i in gspread_client.openall():
                workbook_list.append(i.title)

            if workbookname in workbook_list:
                return True
            else:
                return False
        except Exception as e:
            print(f"Failed to check workbook: {str(e)}")
            return None

    def create_workbook(self, gspread_client ,workbookname):
        try:
            if self.check_workbooks(gspread_client, workbookname):
                pass
            else:
                if workbookname not in [sh.title for sh in gspread_client.openall()]:
                    sh = gspread_client.create(workbookname)
                    sh.share(EMAIL, perm_type='user', role='writer')

                print('new workbook created, please check email')
        except Exception as e:
            print(f"Failed to create workbook {str(e)}")
            return None

    def check_worksheets(self,gspread_client, workbookname, sheetname):
        try:
            sh = gspread_client.open(workbookname)
            worksheet_list = sh.worksheets()
            if sheetname in worksheet_list:
                return True
            else:
                return False
        except Exception as e:
            print(f"Failed to check worksheet: {str(e)}")
            return None

    def creat_worksheet(self, gsspread_client, workbookname, sheetname):
        try:
            if self.check_worksheets(gsspread_client, workbookname, sheetname):
                pass
            else:
                sh = gspread_client.open(workbookname)
                worksheet = sh.add_worksheet(title=sheetname, rows=100, cols=20)
                print('new sheet created')
        except Exception as e:
            print(f"Failed to create worksheet: {str(e)}")
            return None

if __name__ == '__main__':
    with open('config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    PATH_TO_JSON = config['PATH_TO_JSON']
    WORKBOOK_NAME = config['WORKBOOK_NAME']
    SHEET_NAME = config['SHEET_NAME']
    API_SCOPE = config['API_SCOPE']
    EMAIL = config['EMAIL']

    # Usage example
    api = ApiSetting()
    credentials = api.api_scope(API_SCOPE)
    gs_handler = GoogleSpreadsheetHandler()
    gspread_client = gs_handler.authorize(credentials)

    # create
    gs_handler.create_workbook(gspread_client, WORKBOOK_NAME)


# # # open sheet
# # sheet = gspread_client.open(spread_sheet_name).sheet1
# # # D 列の 22行目の情報を表示
# # print(sheet.acell('D12').value)
# # # A 列の 1行目の内容を更新する
# # sheet.update_acell('A11', 'Hello, Sheets API')
