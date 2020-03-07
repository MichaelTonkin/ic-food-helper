import csv

patients = []

class patientData:
    def __init__(self):
        self.grvTime = queue() #a queue combining time and grv in each entry
        self.issues = [None] #array accounts for issues at the end of each day
        self.issuesCounter = 0 #used to take account of what day we are on
        #constant variables
        self.pid = None #the patient's id that we will refer to them by
        self.weight = None

#class: queue
#description: establishes the data type queue and its functions. A queue is a fifo data structure.
#To use simeply establish a variable as an instance of this class.
class queue:
    def __init__(self):
        self.q = []
        pass
    #function: enqueue
    #description: insert a new item to the back of the queue
    #parameters: data - the item to be enqueued (inserted)
    def enqueue(self, data):
        print(data)
        self.q.append(data)
    #function: dequeue
    #description: remove the item at the front of the queue
    def dequeue(self):
        self.q.pop(0)
    #function: front
    #description: return the item at the front of the queue
    def front(self):
        return self.q[0]


#function: string_to_float
#description: when given any string, will search for a float in that string.
#parameters: inputString - the string which is to be converted to a float
def string_to_float(inputString):
    for x in inputString.split():
        try:
            number = (float(x))
        except ValueError:
            pass
    return number

def populateFromCsv(file, patient, pid):
    counter = 0
    #CSV reader
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        temp = []
        for row in reader:
            temp.append(row)

            #get and set the time and grv
            #ignore the first three rows as they contain redundant info
            if counter < 4:
                counter += 1
            else:
                patient.grvTime.enqueue([row[0], row[1], row[3]])

            #get and set the weight
            patient.weight = string_to_float(temp[0][4])
            #set the patient's id
            patient.pid = pid

        #give each queue a buffer on the final day, so that all days consist of 24 hours, instead of day 5 consisting of 23.
        patient.grvTime.enqueue(['', '', ''])


#function: add_patient
#description: declares a new patient and calls the function to populate it with data
#parameters: string file - the file to extract data from for this patient
#string pid - the patient's id to be refered to
def add_patient(file, pid):
    newPatient = patientData()
    patients.append(newPatient)
    populateFromCsv(file, patients[len(patients) - 1], pid)

#function: check_feeding_stopped
#description: checks a patient's issues list to see if they have had their feeding stopped
#parameters: List iss - the issues list from the patient we want to check
def check_feeding_stopped(iss):
    feeding_stopped_once = False
    for x in range(0, len(iss) - 1):
        if iss[x] == "FEEDING STOPPED" and feeding_stopped_once is True:
            return True
        if iss[x] == "FEEDING STOPPED":
            feeding_stopped_once = True

    return False

#call function to create and populate new patients
add_patient("..\\res\\PATIENT DATA - PATIENT A1.csv", "A1")
add_patient("..\\res\\PATIENT DATA - PATIENT A2.csv", "A2")
add_patient("..\\res\\PATIENT DATA - PATIENT A3.csv", "A3")
add_patient("..\\res\\PATIENT DATA - PATIENT B1.csv", "B1")
add_patient("..\\res\\PATIENT DATA - PATIENT B2.csv", "B2")
add_patient("..\\res\\PATIENT DATA - PATIENT B3.csv", "B3")
add_patient("..\\res\\PATIENT DATA - PATIENT B4.csv", "B4")
add_patient("..\\res\\PATIENT DATA - PATIENT B5.csv", "B5")
add_patient("..\\res\\PATIENT DATA - PATIENT B6.csv", "B6")
add_patient("..\\res\\PATIENT DATA - PATIENT B7.csv", "B7")

#function: crit_grv
#description: calculates the value for the critical grv level
#parameters: patientData patient - the patient for whom we are calculating the critical grv for
def crit_grv(patient):
   grv = patient.weight * 5
   return grv

def update_issues_status(patient, value):
    patient.issues[len(patient.issues) - 1] = value
    patient.grvTime.dequeue()

def process_input(patient):
    #set critical grv
    critGrv = crit_grv(patient)

    while patient.grvTime.front() != None:
        currentData = patient.grvTime.front()
        grv = currentData[2]

        #increment the issues counter if the day changes and end function
        if (currentData[0] != "" or currentData[1] == ""):
            print("Patient " + str(patient.pid) + " - Issues = " + str(patient.issues))
            patient.issues.append("NONE")
            patient.issuesCounter += 1
            patient.grvTime.dequeue()
            break

        #check if we have a grv value
        if(grv != ""): #if we have a grv value in this row

            if(float(grv) > critGrv or (patient.weight > 40 and float(grv) > 250)): #if grv is greater than the critical grv level
                #loop to check if any of our issues today contain "feeding stopped"
                #so that we can more correctly update with "see dietician"
                if check_feeding_stopped(patient.issues):
                    update_issues_status(patient, "SEE DIETICIAN")
                else:
                    update_issues_status(patient, "FEEDING STOPPED")
            else: #else update issue with none and goto next row
                update_issues_status(patient, "NONE")

        else: #goto next row
            patient.grvTime.dequeue()


for x in range(1, 6):
    print("DAY " + str(x))
    process_input(patients[0])
    process_input(patients[1])
    process_input(patients[2])
    process_input(patients[3])
    process_input(patients[4])
    process_input(patients[5])
    process_input(patients[6])
    process_input(patients[7])
    process_input(patients[8])
    process_input(patients[9])