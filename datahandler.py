import pandas as pd

df = pd.DataFrame()

class datahandler:
    def removeDuplicates(self,dataframe,subset):
        df = dataframe
        return df.drop_duplicates(subset=subset, keep="first", inplace=False)