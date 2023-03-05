import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class collection:
    def __init__(self) -> None:
        pass

    def get_sample(self) -> pd.DataFrame:
        df_sample = sns.load_dataset("penguins")
        return df_sample
    
    ## add more detailed api or crawl logic later

if __name__ == '__main__':
    data_collector = collection()
    df_sample = data_collector.get_sample()
    print(df_sample)