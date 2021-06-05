from os import name, path
import csv
import json
data = {}
companies = []


# longitude
# latitude
def exec(csvFilePath):
    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for index, rows in enumerate(csvReader):
            itemToAppend = {}
            if "^" not in rows["symbol"]:
               itemToAppend["symbol"] = rows["symbol"]
               itemToAppend["country"] = rows["Country"]

               if rows["Sector"]:
                   itemToAppend["sector"] = rows["Sector"]

               name = rows["name"].split(" ")
               if len(name) == 1:
                   itemToAppend["name"] = name[0]

               elif len(name) >= 4:
                   itemToAppend["name"] = name[0] + " " + name[1] + " " + name[2]


               else:
                   itemToAppend["name"] = name[0] + " " + name[1]


               companies.append(itemToAppend)

        # print(companies)
        seen_titles = set()
        new_list = []
        for company in companies:
            # print(company)
            if company["name"] not in seen_titles:
                new_list.append(company)
                seen_titles.add(company["name"])


        #     if company not in seen_titles:
        #         print(company)
                # new_list.append(company)
                # seen_titles.add(company.name)

        # print(len(new_list))




                # schools.append(itemToAppend)
        jsonString = json.dumps(new_list,  indent=2)
        jsonFile = open("complete_companies.json", "w")

        jsonFile.write(jsonString)
        jsonFile.close()













# school_data.csv

exec('company_list.csv')


