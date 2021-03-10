import pandas as pd
import math

df = pd.read_csv("/Users/liutianrui/bpsCoordinates.csv")
# print(df.head(5))

for i in range(len(df)): 
    ori_latitude=df.iloc[i, 7]
    frac,whole=math.modf(ori_latitude)
    if (abs(0.250-abs(frac))<=abs(0.750-abs(frac))):
        new_float=0.250
        if (whole<0):
            new_num=whole-new_float
        else:
            new_num=whole+new_float
    else:
        new_float=0.750
        if (whole<0):
            new_num=whole-new_float
        else:
            new_num=whole+new_float
    df["New Latitude"][i]=new_num

    ori_longitude=df.iloc[i, 8]
    frac1,whole1=math.modf(ori_longitude)
    if (abs(0.250-abs(frac1))<=abs(0.750-abs(frac1))):
        new_float1=0.250
        if (whole1<0):
            new_num1=whole1-new_float1
        else:
            new_num1=whole1+new_float1
    else:
        new_float1=0.750
        if (whole1<0):
            new_num1=whole1-new_float1
        else:
            new_num1=whole1+new_float1
    df["New Longitude"][i]=new_num1
    
df.to_csv("/Users/liutianrui/bpsCoordinates.csv")
