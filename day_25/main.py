# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

import pandas as pd
import numpy as np
# data = pd.read_csv("weather_data.csv")
# # print(type(data))  # <class 'pandas.core.frame.DataFrame'>
# # print(type(data["temp"]))  # <class 'pandas.core.series.Series'>
# data_dict = data.to_dict()
# print(data_dict)
# # 평균
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# print(np.mean(data["temp"].to_list()))
# print(data["temp"].mean())
#
# # 최댓값
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

# print(df)
# print(df.info())
# print(df["Primary Fur Color"].unique())
from collections import Counter
# B열의 모든 값 개수 조회
# print(type(Counter(df['Primary Fur Color'])))
# Counter(df['Primary Fur Color'])

import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = df["Primary Fur Color"].unique()

import numpy as np
color_list = np.delete(color_list, 0)

color_count_list = []
for color in color_list:
        color_count_list.append(len(df[df["Primary Fur Color"] == color]))

print(color_list)
print(color_count_list)

df = pd.DataFrame({"Fur Color": color_list, "Count": color_count_list})
df.to_csv("squirrel_count.csv")
