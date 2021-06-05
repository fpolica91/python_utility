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
            itemToAppend['name'] = rows["name"]
            itemToAppend['street'] = rows['street']
            itemToAppend['city'] =  rows['city']
            itemToAppend['state'] = rows['state']
            itemToAppend['stateAbbreviation'] = rows['stateAbbreviation']
            itemToAppend['zip'] = rows['zip']
            itemToAppend['phoneNumber'] = rows['phoneNumber']
            itemToAppend['population'] = rows['population']
            itemToAppend['county'] = rows['county']
            itemToAppend['countyFIPS'] = rows['countyFIPS']
            itemToAppend['country'] = rows['country']
            itemToAppend['countryAbbreviation'] = rows['countryAbbreviation']
            itemToAppend['longitude'] = rows['longitude']
            itemToAppend['latitude'] = rows['latitude']
            itemToAppend['website'] =  rows['website'] # Comment out Here
            itemToAppend['level'] = rows['level']
            itemToAppend['enrollment'] = rows['enrollment']
            itemToAppend['startGrade'] = rows['startGrade']
            itemToAppend['endGrade'] = rows['endGrade']
            itemToAppend['districtId'] = rows['districtId']
            itemToAppend['districtName'] = rows['districtName']
            itemToAppend['teacherCount'] = rows['teacherCount']
            itemToAppend['totalSpentPerPupil'] = rows['totalSpentPerPupil']
            itemToAppend['displayName'] =  rows['displayName']
            itemToAppend['dataRecordYear'] =  rows['dataRecordYear']
            itemToAppend['ncesId'] = rows['nces ID']



            schools.append(itemToAppend)
        jsonString = json.dumps(schools)
        jsonFile = open("schools.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()















exec('formatted2.csv')
print(schools)




            # itemToAppend = {}
            # itemToAppend['name'] = rows['SCH NAME'].upper()
            # itemToAppend['street'] = rows['StreetAddress'].upper()
            # itemToAppend['city'] =  rows['City'].upper()
            # itemToAppend['state'] = stateFormatter(rows['STATENAME']) # rows['STATENAME'].capitalize()
            # itemToAppend['stateAbbreviation'] = rows['ST']
            # itemToAppend['zip'] = rows['ZipCode']
            # itemToAppend['phoneNumber'] = phoneNumber
            # itemToAppend['population'] = amountOfStudents + teachersAmount
            # itemToAppend['county'] = countyName
            # itemToAppend['countyFIPS'] = countyFIPS
            # itemToAppend['country'] = "United States of America"
            # itemToAppend['countryAbbreviation'] = "USA"
            # itemToAppend['longitude'] = longitude # Comment out Here
            # itemToAppend['latitude'] = latitude  # Comment out Here
            # itemToAppend['website'] = schoolWebsite  # Comment out Here
            # itemToAppend['level'] = schoolLevel
            # itemToAppend['enrollment'] = amountOfStudents
            # itemToAppend['startGrade'] = rows['SY 1819 GSLO']
            # itemToAppend['endGrade'] = rows['SY1819 GSHI']
            # itemToAppend['districtId'] = int(rows['LEAID'])
            # itemToAppend['districtName'] = rows['LEA NAME'].upper()
            # itemToAppend['teacherCount'] = teachersAmount
            # itemToAppend['totalSpentPerPupil'] = totalSpentPerPupil
            # itemToAppend['displayName'] = rows['SCH NAME']
            # itemToAppend['dataRecordYear'] = dataRecordYear
            # itemToAppend['ncesId'] = ncesId
