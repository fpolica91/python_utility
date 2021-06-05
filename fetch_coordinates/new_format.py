from os import path
import csv
import json
data = {}
schools = []
def exec(csvFilePath):
    with open(csvFilePath, encoding='utf-8') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for index, rows in enumerate(csvReader):

            itemToAppend = {}
            itemToAppend['name'] = rows["name"]
            itemToAppend['state'] = rows['state']
            itemToAppend['stateAbbreviation'] = rows['stateAbbreviation']

            if rows['pupil_teacher_ratio'] == '–' or rows['pupil_teacher_ratio'] == '†' or rows['pupil_teacher_ratio'] == '‡':
                itemToAppend['pupilTeacherRatio'] = None
            else:
                itemToAppend['pupilTeacherRatio'] = rows['pupil_teacher_ratio']
            itemToAppend['displayName'] =  rows['displayName']
            itemToAppend['ncesId'] = rows['ncesId']
            itemToAppend["schoolType"] = rows["schoolType"]
            # itemToAppend["agencyType"] = rows["agencyType"]
            if rows["agencyType"]:
                to_arr = rows["agencyType"].split("-")
                itemToAppend["agencyType"] = to_arr[1]

            if rows["schoolType"]:
                to_arr = rows["schoolType"].split("-")
                itemToAppend["schoolType"] = to_arr[1]


            if rows["charter"] == "2-No":
                 itemToAppend["isCharter"] = False

            if rows["charter"] == "1-Yes":
                itemToAppend["isCharter"] = True

            if rows["magnet"] == "2-No":
                 itemToAppend["isMagnet"] = False

            if rows["magnet"] == "1-Yes":
                itemToAppend["isMagnet"] = True




            if rows['total_students'] == '–' or rows['total_students'] == '†' or rows['total_students'] == '‡':
                itemToAppend['totalStudents'] = None
            else:
                itemToAppend['totalStudents'] = rows['total_students']

            # itemToAppend["FRL_eligible"] = rows["FRL_eligible"]

            if rows['FRL_eligible'] == '–' or rows['FRL_eligible'] == '†' or rows['FRL_eligible'] == '‡':
                itemToAppend['frlEligible'] = None
            else:
                itemToAppend['frlEligible'] = rows['FRL_eligible']

            if rows['amer_indian_alaska_native'] == '–' or rows['amer_indian_alaska_native'] == '†' or rows['amer_indian_alaska_native'] == '‡':
                itemToAppend['americanIndianAlaskaNative'] = None
            else:
                itemToAppend['americanIndianAlaskaNative'] = rows['asian_pacific_islander']

            if rows['asian_pacific_islander'] == '–' or rows['asian_pacific_islander'] == '†' or rows['asian_pacific_islander'] == '‡':
                itemToAppend['asianPacificIslander'] = None
            else:
                itemToAppend['asianPacificIslander'] = rows['asian_pacific_islander']

            if rows['hispanic_latinx'] == '–' or rows['hispanic_latinx'] == '†' or rows['hispanic_latinx'] == '‡':
                itemToAppend['hispanicLatinx'] = None
            else:
                itemToAppend['hispanicLatinx'] = rows['hispanic_latinx']

            if rows['white'] == '–' or rows['white'] == '†' or rows['white'] == '‡':
                itemToAppend['white'] = None
            else:
                itemToAppend['white'] = rows['white']

            if rows['hawaii_pacific_isl'] == '–' or rows['hawaii_pacific_isl'] == '†' or rows['hawaii_pacific_isl'] == '‡':
                itemToAppend['hawaianPacificIslander'] = None
            else:
                itemToAppend['hawaianPacificIslander'] = rows['hawaii_pacific_isl']

            if rows['multi_racial'] == '–' or rows['multi_racial'] == '†' or rows['multi_racial'] == '‡':
                itemToAppend['multiRacial'] = None
            else:
                itemToAppend['multiRacial'] = rows['multi_racial']

            if rows['total_race_eth'] == '–' or rows['total_race_eth'] == '†' or rows['total_race_eth'] == '‡':
                itemToAppend['totalRaceEthnicity'] = None
            else:
                itemToAppend['totalRaceEthnicity'] = rows['total_race_eth']

            itemToAppend['agencyId'] = rows['agency_id']
            if rows['black'] == '–' or rows['black'] == '†' or rows['black'] == '‡':
                itemToAppend['black'] = None
            else:
                itemToAppend['black'] = rows['black']






            schools.append(itemToAppend)
        jsonString = json.dumps(schools)
        jsonFile = open("formatted_new.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()















exec('new_data.csv')

