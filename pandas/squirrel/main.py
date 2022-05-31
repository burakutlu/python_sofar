import pandas
import openpyxl

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

output = {
    "ID": [data["Unique Squirrel ID"].head(10)],
    "Color": [data["Primary Fur Color"].head(10)]
}
for i in range(1, 10):
    output["ID"].append(data["Unique Squirrel ID"])
    output["Color"].append(data["Primary Fur Color"])

output_data = pandas.DataFrame(output)
output_data.to_excel("output.xlsx", index=False)
