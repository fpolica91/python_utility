from os import path
import csv
import json
import requests
data = {}
schools = []
GOOGLE_API_KEY = "YOUR API KEY"

# longitude
# latitude
def exec(csvFilePath):
    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for index, school in enumerate(csvReader):
            if school["longitude"] == "0" or school["latitude"] == "0":
                print("upating the school information...", school['name'], index)
                address = school["street"] + " " + school["city"] + " " + school["state"]
                response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&lang=en&key=' + GOOGLE_API_KEY)
                data = response.json()
                if len(data) > 0:
                    geometry = data["results"][0]["geometry"]

                    latitude = geometry['location']['lat']
                    longitude = geometry['location']['lng']
                    school['latitude'] = latitude
                    school['longitude'] = longitude

            schools.append(school)












    print(schools)



            # print('school', school)





exec('schools.csv')

# /Users/fabriciopolicarpo/Desktop/Lincoln/parser_python/schools_city_address.csv
with open('formatted.csv', 'w', newline='', encoding='utf-8') as f:
    print("updating the csv")
    writer = csv.writer(f)
    outputFile = open("formatted.csv", 'w') #load csv file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(schools[0].keys())  # header row
    for row in schools:
        output.writerow(row.values())
