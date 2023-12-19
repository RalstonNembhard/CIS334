import mysql.connector
from mysql.connector import Error

class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="hospital_portal",
                 user='root',
                 password='password'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def addPatient(self, patient_name, age, admission_date, discharge_date):
        ''' Method to insert a new patient into the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (patient_name, age, admission_date, discharge_date))
            self.connection.commit()
            return
    def updatePatientDetails(self, patient_id,patient_name, age, admission_date, discharge_date):
        ''' Method to insert a new patient into the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query="call EditPatient(%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (patient_id,patient_name, age, admission_date, discharge_date))
            self.connection.commit()
            return

    def getAllPatients(self):
        ''' Method to get all patients from the patients table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM patients"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def scheduleAppointment(self, patient_id, doctor_id, appointment_date, appointment_time):
        ''' Method to schedule an appointment '''
        
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()            
            query = "CALL ScheduleAppointment(%s, %s, %s, %s)"
            self.cursor.execute(query, (patient_id, doctor_id, appointment_date, appointment_time))
            self.connection.commit()
            return
        
          

    def viewAppointments(self,patient_id=None):
        ''' Method to view all appointments '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            if patient_id is None:
                query = "CALL GetAppointments(NULL)"
                self.cursor.execute(query)
            else:
                query = "CALL GetAppointments(%s)"
                self.cursor.execute(query, (patient_id,))           
            records = self.cursor.fetchall()
            return records 
               
    ####Delete Patient
    def deletePatient(self, patient_id):
        ''' Method to delete a patient '''                    
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query="call deletePatient(%s)"            
            self.cursor.execute(query, (patient_id,))
            self.connection.commit()
            return           
    ####Delete Patient 
            
    def dischargePatient(self, patient_id, discharge_date):
        ''' Method to discharge a patient '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query="call DischargePatient(%s, %s)"            
            self.cursor.execute(query, (patient_id, discharge_date))
            self.connection.commit()
            return    
    #### View All Doctors
    
    def viewAllDoctors(self):
        ''' Method to view all doctors '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM doctors"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
    
    def viewRecords(self):
        ''' Method to view all doctors '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM appointment_doctors_patients"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
