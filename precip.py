import pandas as pd
import math

path="/Users/liutianrui/Downloads/merged_2014_adult 2.csv"
df = pd.read_csv(path)
for i in range(len(df)):
    if df.iloc[i, 25]>0:
        migyr=int(df.iloc[i, 25])
        precipyr=migyr-1
        str_precipyr=str(precipyr)
        df["migrprecip"][i]=df[str("precip"+str_precipyr)][i]
    
    elif df.iloc[i, 38]>0:  
        migyr_18=int(df.iloc[i, 38])
        migyr_19=int(df.iloc[i, 38])+1
        migyr_20=int(df.iloc[i, 38])+2
        migyr_21=int(df.iloc[i, 38])+3
        migyr_22=int(df.iloc[i, 38])+4
        migyr_23=int(df.iloc[i, 38])+5
        migyr_24=int(df.iloc[i, 38])+6
        migyr_25=int(df.iloc[i, 38])+7
        precipyr_18=migyr_18-1
        precipyr_19=migyr_19-1
        precipyr_20=migyr_20-1
        precipyr_21=migyr_21-1
        precipyr_22=migyr_22-1
        precipyr_23=migyr_23-1
        precipyr_24=migyr_24-1
        precipyr_25=migyr_25-1
        str_precipyr18=str(precipyr_18)
        str_precipyr19=str(precipyr_19)
        str_precipyr20=str(precipyr_20)
        str_precipyr21=str(precipyr_21)
        str_precipyr22=str(precipyr_22)
        str_precipyr23=str(precipyr_23)
        str_precipyr24=str(precipyr_24)
        str_precipyr25=str(precipyr_25)
        if 1946<=precipyr_18<=2014:
            df["precip18"][i]=df[str("precip"+str_precipyr18)][i]
        if 1946<=precipyr_19<=2014:
            df["precip19"][i]=df[str("precip"+str_precipyr19)][i]
        if 1946<=precipyr_20<=2014:
            df["precip20"][i]=df[str("precip"+str_precipyr20)][i]
        if 1946<=precipyr_21<=2014:
            df["precip21"][i]=df[str("precip"+str_precipyr21)][i]
        if 1946<=precipyr_22<=2014:
            df["precip22"][i]=df[str("precip"+str_precipyr22)][i]
        if 1946<=precipyr_23<=2014:
            df["precip23"][i]=df[str("precip"+str_precipyr23)][i]
        if 1946<=precipyr_24<=2014:
            df["precip24"][i]=df[str("precip"+str_precipyr24)][i]
        if 1946<=precipyr_25<=2014:
            df["precip25"][i]=df[str("precip"+str_precipyr25)][i]
df.to_csv("/Users/liutianrui/Downloads/merged_2014_adult.csv")






