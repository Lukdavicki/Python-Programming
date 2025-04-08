# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(round(avg_temp,2))
# # print(data["temp"].mean())
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = monday.temp[0]
# print(monday_temp)
import pandas

sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
sq_colorList = sq_data["Primary Fur Color"].to_list()
# print(sq_colorList)
grey = sq_colorList.count("Gray")
cinnamon = sq_colorList.count("Cinnamon")
black = sq_colorList.count("Black")
# print(f"{grey}, {cinnamon}, {black}")

sq_colorNumbers = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey, cinnamon, black]
}
data = pandas.DataFrame(sq_colorNumbers)
print(data)
data.to_csv("squirrel_count.csv")
