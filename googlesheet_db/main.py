import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import data_collector
import googlesheet_db

if __name__ == '__main__':
    with open('config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        PATH_TO_JSON = config['PATH_TO_JSON']
        WORKBOOK_NAME = config['WORKBOOK_NAME']
        SHEET_NAME = config['SHEET_NAME']
        API_SCOPE = config['API_SCOPE']
        EMAIL = config['EMAIL']

    api = googlesheet_db.ApiSetting()
    credentials = api.api_scope(API_SCOPE)
    gs_handler = googlesheet_db.GoogleSpreadsheetHandler()
    gspread_client = gs_handler.authorize(credentials)

    # create
    gs_handler.create_workbook(gspread_client, WORKBOOK_NAME)
    gs_handler.create_worksheets(gspread_client, WORKBOOK_NAME, SHEET_NAME)    

    