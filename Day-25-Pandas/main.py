import csv

import pandas
# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

# data = pd.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# #get data in columns
# print(data["condition"])
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data["temp"].max()])

#get data in row
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9 / 5 + 32
#
# # print(monday_temp_f)
# data_dict = {
#     "students": ["mohan", "krishna", "baratam"],
#     "score": [76, 56, 65]
# }
# # Create a dataframe from scratch
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv", index=False)

data = pandas.read_csv('Squirrel_Count.csv')
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('Squirrel_Coolor_count.csv')


