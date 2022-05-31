import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

output = {
    "ID": [],
    "Color": []
}
for i in range(10):
    output["ID"].append(data["Unique Squirrel ID"].sample().values)
    output["Color"].append(data["Primary Fur Color"].sample().values)


output_data = pandas.DataFrame(output)
output_data.to_excel("output.xlsx", index=False)
