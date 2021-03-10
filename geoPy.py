import pandas as pd
from geopy import Nominatim
import io

geolocator = Nominatim(user_agent="example app")

df = pd.read_csv("/Users/liutianrui/Downloads/bpsData.csv")
print(df.head())

df["loc"] = df["kecnm14"].apply(geolocator.geocode)
df["point"]= df["loc"].apply(lambda loc: tuple(loc.point) if loc else None)

df[['lat', 'lon', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)
print(df.head())




