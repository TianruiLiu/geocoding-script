import pandas as pd
import math

path="/Users/liutianrui/Downloads/survival.csv"
df = pd.read_csv(path)
df=df[df['duration']>0]
# df=df[int(df['duration'])]
df.reindex(df.index.repeat((df['duration'])))
print(df.head())
# for i in range(len(df)):  

#     total_precip=0
#     for h in range (44,113):
#         total_precip+=df.iloc[i, h]
#     # print(total_precip)
#     avg_precip=total_precip/69
#     # print(avg_precip)
#     cumulative_square_diff=0
#     for h in range (44,113):
#         cumulative_square_diff=(df.iloc[i, h]-avg_precip)*(df.iloc[i, h]-avg_precip)+cumulative_square_diff
#     standard_deviation=math.sqrt(cumulative_square_diff/69)
#     # print(standard_deviation)
#     for h in range (44,113):
#         df.iloc[i, h]=(df.iloc[i, h]-avg_precip)/standard_deviation
#     migyr=int(df.iloc[i, 26])
#     precipyr=migyr-1
#     if 1946<=precipyr<=2014:
#         str_precipyr=str(precipyr) 
#     #     # print(df[str("precip"+str_precipyr)][i])
#         h=precipyr-1902
#         # print(h)
#         # df.iloc[i,121]=df[str("precip"+str_precipyr)][i]
#         df.iloc[i,121]=df.iloc[i,h]
#     # print(df.iloc[i,121])
df.to_csv("/Users/liutianrui/Downloads/survival-data.csv")