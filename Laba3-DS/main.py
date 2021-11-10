import numpy as np
import pandas as pd

frame=pd.read_csv("olympics.csv")
print(frame)

frame = pd.read_csv("olympics.csv", index_col = 0, skiprows = 1)
print(frame)

frame.info()

frame.dtypes

frame1 = frame.append(pd.DataFrame([], columns=frame.columns, index=['Armenia\xa0(ARM)']))
print(frame)

frame1 = frame.fillna(0, inplace=True) 
print(frame)

frame = frame.rename(columns={'01 !':"Gold", "02 !":"Silver", "03 !":"Bronze"})
print(frame)

frame_drop = frame.drop("Totals", axis=0)
print(frame_drop)

print(frame[frame["Gold"] > 0])

print("Count Gold: ", len(frame.loc[frame["Gold"] > 0]))

print(frame.loc[frame["Gold"] == frame["Gold"].max()].index[0])

print(frame.loc[(frame["Gold"]>0)&(frame["Silver"]>0)])

print("Чи є в таблиці Україна? ", "Ukraine\xa0(UKR)" in frame.index)