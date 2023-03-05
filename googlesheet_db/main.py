import yaml
import pandas as pd
import data_collector
import googlesheet_db

if __name__ == '__main__':

    with open('googlesheet_db/config.yml', 'r') as f:
        config = yaml.safe_load(f)
        PATH_TO_JSON = config['PATH_TO_JSON']
        WORKBOOK_NAME = config['WORKBOOK_NAME']
        SHEET_NAME = config['SHEET_NAME']
        API_SCOPE = config['API_SCOPE']
        EMAIL = config['EMAIL']

    # print(WORKBOOK_NAME)
    api = googlesheet_db.ApiSetting()
    credentials = api.api_scope(API_SCOPE,PATH_TO_JSON)
    gs_handler = googlesheet_db.GoogleSpreadsheetHandler()
    gspread_client = gs_handler.authorize(credentials)

    # create
    gs_handler.create_workbook(gspread_client, WORKBOOK_NAME, EMAIL)
    gs_handler.create_worksheets(gspread_client, WORKBOOK_NAME, SHEET_NAME)

    # open sheet
    workbook = gspread_client.open(WORKBOOK_NAME)
    worksheet = workbook.worksheet(SHEET_NAME)

    # data collection
    collector = data_collector.collection()
    df_sample = collector.get_sample()
    df_sample = df_sample.astype(str) #need to convert to text before passing to Google sheet
    worksheet.update([df_sample.columns.values.tolist()] + df_sample.values.tolist())