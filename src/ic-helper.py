import csv

patients = []

class patientData:
    def __init__(self):
        pass
    def time(timeData):
        return timeData
    def day(dayData):
        return dayData
    def grv(grvData):
        return grvData
    def pid(idData):
        return idData
    def risk(riskData):
        return riskData
    def weight(weightData):
        return weightData
    def feed(feedData):
        return feedData
    def issues(issuesData):
        return issuesData

#for p in range(0,5):
 #   newPatient = patientData()
  #  newPatient.time=0
   # newPatient.grv=10
    #newPatient.id=p
    #patients.append(newPatient)

def populateFromCsv(file, patient):
    s = 0
    e = 0
    counter = 0
    #CSV reader
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        temp = []
        for row in reader:
            temp.append(row)
        patient.risk = temp[0][1]
        #get the weight from string
        patient.weight = temp[0][4]
        #loop through each character

        patient.weight = temp[0][4][s:e]
        #convert to float
        print(temp)

newPatient = patientData()
patients.append(newPatient)
populateFromCsv("..\\res\\PATIENT DATA - PATIENT A1.csv", patients[0])







