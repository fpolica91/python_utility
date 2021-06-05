from os import path
import csv
import json
data = {}
schools = []


# longitude
# latitude
def exec(csvFilePath):
    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for index, rows in enumerate(csvReader):
            itemToAppend = {}
            if len(rows["contact_1_email"]) > 0 and rows["contact_1_email"].startswith("https") == False and rows["contact_1_email"] != "#N/A":

                if len(rows["contact_1_name"]) > 0 and rows["contact_1_name"] != "#N/A":
                     itemToAppend['contact_name'] = rows["contact_1_name"]
                else:
                    itemToAppend['contact_name'] = "Staff Member"

                itemToAppend['contact_email'] = rows['contact_1_email']


                schools.append(itemToAppend)
        jsonString = json.dumps(schools,  indent=2)
        jsonFile = open("contact_info.json", "w")

        jsonFile.write(jsonString)
        jsonFile.close()













# school_data.csv

exec('school_data.csv')


