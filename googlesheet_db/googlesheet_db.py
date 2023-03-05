import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import yaml
import re

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

    def api_scope(self, apiscope_list: list, path_to_json: str):
        # create api list
        api_scope = apiscope_list
        # connect to json key
        try:
            credentials_path = os.path.join(os.path.expanduser('~'), path_to_json)
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

    def create_workbook(self, gspread_client ,workbookname , email):
        try:
            if self.check_workbooks(gspread_client, workbookname):
                print('worksbook exists')
                pass
            else:
                if workbookname not in [sh.title for sh in gspread_client.openall()]:
                    sh = gspread_client.create(workbookname)
                    sh.share(email, perm_type='user', role='writer')

                print('new workbook created, please check email')
        except Exception as e:
            print(f"Failed to create workbook {str(e)}")
            pass

    def check_worksheets(self, gspread_client, workbookname, sheetname):
        try:

            # worksheet_list = [<Worksheet 'Sheet1' id:0>, <Worksheet 'coffee_shop_sheet' id:683566400>]
            sh = gspread_client.open(workbookname)
            worksheet_list = sh.worksheets()
            sheet_names = []
            for worksheet in worksheet_list:
                sheet_name = re.search(r"'(.+)'", str(worksheet)).group(1)
                sheet_names.append(sheet_name)

            if sheetname in sheet_names:
                return True
            else:
                return False
        except Exception as e:
            print(f"Failed to check worksheet: {str(e)}")
            pass

    def create_worksheets(self, gspread_client, workbookname, sheetname):

        try:
            if self.check_worksheets(gspread_client, workbookname, sheetname):
                print('worksheet exists')
                pass
            else:
                sh = gspread_client.open(workbookname)
                worksheet = sh.add_worksheet(title=sheetname, rows=100, cols=20)
                print('new sheet created')
        except Exception as e:
            print(f"Failed to create worksheet: {str(e)}")
            pass

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
    credentials = api.api_scope(API_SCOPE, PATH_TO_JSON)
    gs_handler = GoogleSpreadsheetHandler()
    gspread_client = gs_handler.authorize(credentials)

    # create
    gs_handler.create_workbook(gspread_client, WORKBOOK_NAME, EMAIL)
    gs_handler.create_worksheets(gspread_client, WORKBOOK_NAME, SHEET_NAME)