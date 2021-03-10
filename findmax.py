import pandas as pd
import math

df = pd.read_csv("/Users/liutianrui/bpsCoordinates.csv")

column=df["Longitude"]
max_value=column.max()
print(column.max())