# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# # put the weather data into a list called weather_data
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# Day 25 of 100 days of code Dr Angela Yu
import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data)) # pandas.core.frame.DataFrame
# print(type(data['temp']))  # pandas.core.series.Series

# data_dict = data.to_dict() # convert dataframe to dictionary
# print(data_dict)

# temp_list = data['temp'].to_list() # convert dataframe to list
# print(temp_list)

# temp_list = data['temp'].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data['temp'].mean()) # pandas method to calculate mean

# print(data['temp'].max())  # pandas method to calculate max

# print(data["condition"])  # pandas method to get a column
# print(data.condition)  # pandas method to get a column

# print(data[data.day == "Monday"])  # pandas method to get a row
# print(data[data.temp == data.temp.max()])  # pandas method to get a row

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# How many grey/black/Cinnamon squirrels are there in Central Park? make a new csv file called squirrel_count.csv
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(squirrel_data)
grey_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print(grey_squirrels)
print(black_squirrels)
print(cinnamon_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels, black_squirrels, cinnamon_squirrels]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("squirrel_count.csv")
