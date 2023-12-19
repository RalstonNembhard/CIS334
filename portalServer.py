
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
from datetime import date
import cgi

class HospitalPortalHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_POST(self):
        try:
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                patient_id = form.getvalue("patient_id") 
                patient_name = form.getvalue("patient_name")
                age = int(form.getvalue("patient_age"))
                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")
                
                
                self.database.addPatient(patient_name, age, admission_date,discharge_date)
                print("Patient added:", patient_name, patient_id, age, admission_date)
                
                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a> |\
                                  <a href='/viewPatients'>View Patients</a> |\
                                  <a href='/dischargePatient'>Discharge Patient</a> |\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been added</h3>")
                self.wfile.write(b"<div><a href='/addPatient'>Add Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
                #
                return
            ######## Update Patient Details
            if self.path == '/updatePatientDetails':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                patient_id = form.getvalue("patient_id") 
                patient_name = form.getvalue("patient_name")

                if form.getvalue("patient_age") is not None:
                    age = int(form.getvalue("patient_age"))
                else:
                    age = 0

                admission_date = form.getvalue("admission_date")
                discharge_date = form.getvalue("discharge_date")
               
                self.database.updatePatientDetails(patient_id,patient_name, age, admission_date,discharge_date)
                print("Patient added:", patient_name, patient_id, age, admission_date)
                
                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a> |\
                                  <a href='/viewPatients'>View Patients</a> |\
                                  <a href='/dischargePatient'>Discharge Patient</a> |\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                 <a href='/viewRecords'>View All Records</a>\
                                 </div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been Updated</h3>")
                self.wfile.write(b"<div><a href='/updatePatientDetails'>Update Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
                return
                
            
            ######## Update Patient Details
        
            #New===Add Appointment
            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                patient_id = int(form.getvalue("patient_id"))
                doctor_id = int(form.getvalue("doctor_id"))
                appointment_date = form.getvalue("appointment_date")
                appointment_time = form.getvalue("appointment_time")

                # Call the Database Method to schedule an appointment
                self.database.scheduleAppointment(patient_id, doctor_id, appointment_date, appointment_time)

                print("Appointment Scheduled:", patient_id, doctor_id, appointment_date, appointment_time)
                
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                <a href='/addPatient'>Add Patient</a>|\
                                <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                <a href='/viewAppointments'>View Appointments</a>|\
                                <a href='/dischargePatient'>Discharge Patient</a>\
                                <a href='/deletePatient'>Delete Patient</a>\
                                <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                <a href='/viewAllDoctors'>View All Doctors</a>\
                                <a href='/viewRecords'>View All Records</a> </div>")
                self.wfile.write(b"<hr><h2>Appointment Scheduled</h2>")
                self.wfile.write(b"<div><a href='/scheduleAppointment'>Schedule Another Appointment</a></div>")
                self.wfile.write(b"</center></body></html>")
                return
            ####New===Add Appointment
            ####Delete Patient
            if self.path == '/deletePatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                patient_id = form.getvalue("patient_id") #?
                
                # Call the Database Method to delete patient.

                self.database.deletePatient(patient_id)
                print("Patient Deleted:", patient_id)
                
                self.wfile.write(b"<html><head><title> Hospital Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/viewPatients'>View Patients</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a>\
                                  <a href='/viewRecords'>View All Records</a> </div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been Deleted</h3>")
                self.wfile.write(b"<div><a href='/deletePatient'>Delete Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
                
                return
            
            ####Delete Patient
            #### View Appointments
            if self.path == '/viewAppointments':                              

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                patient_id = form.getvalue("patient_id")

                records = self.database.viewAppointments(patient_id)
                data = records
                self.wfile.write(b"<html><head><title>Hospital's Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addPatient'>Add Patient</a> | \
                             <a href='/scheduleAppointment'>Schedule Appointment</a> | \
                             <a href='/viewAppointments'>View Appointments</a> | \
                             <a href='/dischargePatient'>Discharge Patient</a> | \
                             <a href='/deletePatient'>Delete Patient</a>\
                             <a href='/updatePatientDetails'>Update Patient Details</a> | \
                             <a href='/viewAllDoctors'>View All Doctors</a>\
                             <a href='/viewRecords'>View All Records</a>   </div>")
                self.wfile.write(b"<hr><h2>Viewing Appointments</h2>")
            
                self.wfile.write(b"<table border=2>\
                                <tr><th>Patient's ID</th>\
                                    <th>Patient's Name</th>\
                                    <th>Doctor's ID</th>\
                                    <th>Doctor's Name</th>\
                                    <th>Appointment Date</th>\
                                    <th>Appointment Time</th></tr>")
            
                for row in data:
                    self.wfile.write(b'<tr><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[5]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            #### View Appointments
            
            ####Discharge Patient

            if self.path == '/dischargePatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                patient_id = form.getvalue("patient_id") 
                discharge_date = form.getvalue("discharge_date")
               
                self.database.dischargePatient(patient_id, discharge_date)
                print("Patient Discharged:", patient_id)
                
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a> \
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a>\
                                  <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Patient has been Discharged</h3>")
                self.wfile.write(b"<div><a href='/dischargePatient'>Discharge Another Patient</a></div>")
                self.wfile.write(b"</center></body></html>")
                
                return
                ####Discharge Patient


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

        return            
            
            
    def do_GET(self):
        
        try:
            # I have implemented for you the getAllPatients
            if self.path == '/':
                data=[]
                records = self.database.getAllPatients()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a> \
                                  <a href='/viewRecords'>View All Records</a> </div>")
                self.wfile.write(b"<hr><h2>All Patients</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Patient ID </th>\
                                        <th> Patient Name</th>\
                                        <th> Age </th>\
                                        <th> Admission Date </th>\
                                        <th> Discharge Date </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            ##View all patients

            #### View All Doctors
            if self.path == '/viewAllDoctors':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.viewAllDoctors()
                data = records
                self.wfile.write(b"<html><head><title>Hospital's Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addPatient'>Add Patient</a> | \
                             <a href='/scheduleAppointment'>Schedule Appointment</a> | \
                             <a href='/viewAppointments'>View Appointments</a> | \
                             <a href='/dischargePatient'>Discharge Patient</a> | \
                             <a href='/deletePatient'>Delete Patient</a> | \
                             <a href='/updatePatientDetails'>Update Patient Details</a> | \
                             <a href='/viewAllDoctors'>View All Doctors</a>\
                             <a href='/viewRecords'>View All Records</a>    </div>")
                self.wfile.write(b"<hr><h2>Viewing All Doctors</h2>")

                self.wfile.write(b"<table border=2>\
                                <tr><th>Doctor ID</th>\
                                    <th>Doctor Name</th>\
                                    <th>Email</th>\
                                    <th>Phone </th></tr>")

                for row in data:
                    self.wfile.write(b'<tr><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            #### View All Doctors

            ##addPatient Implemented : complete Code in do_Post /addPatient, Read comment in do_Post
            if self.path == '/addPatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a> \
                                 <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                 <a href='/viewAllDoctors'>View All Doctors</a>\
                                 <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr><h2>Add New Patient</h2>")

                self.wfile.write(b"<form action='/addPatient' method='post'>")
                self.wfile.write(b'<label for="patient_name">Patient Name:</label>\
                      <input type="text" id="patient_name" name="patient_name"/><br><br>\
                      <label for="patient_age">Age:</label>\
                      <input type="number" id="patient_age" name="patient_age"><br><br>\
                      <label for="admission_date">Admission Date:</label>\
                      <input type="date"id="admission_date" name="admission_date"><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date"id="discharge_date" name="discharge_date"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')
                
                self.wfile.write(b"</center></body></html>")
                return
            
            ####Update Patient Details
            if self.path == '/updatePatientDetails':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a> \
                                 <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                 <a href='/viewAllDoctors'>View All Doctors</a>\
                                 <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr><h2>Update Patient Details Information</h2>")

                self.wfile.write(b"<form action='/updatePatientDetails' method='post'>")
                self.wfile.write(b'<label for="patient_id">Patient ID:</label>\
                      <input type="text" id="patient_id" name="patient_id"/><br><br>\
                      <label for="patient_name">Patient Name:</label>\
                      <input type="text" id="patient_name" name="patient_name"/><br><br>          \
                      <label for="patient_age">Age:</label>\
                      <input type="number" id="patient_age" name="patient_age"><br><br>\
                      <label for="admission_date">Admission Date:</label>\
                      <input type="date"id="admission_date" name="admission_date"><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date"id="discharge_date" name="discharge_date"><br><br>\
                      <input type="submit" value="Update">\
                      </form>')
                
                self.wfile.write(b"</center></body></html>")
                return
            ####Update Patient Details

            ### View Appointments
            if self.path == '/viewAppointments':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()               
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a>\
                                  <a href='/viewRecords'>View All Records</a> </div>")
                self.wfile.write(b"<hr><h2>Viewing Appointments</h2>")
                ###
                self.wfile.write(b"<form action='/viewAppointments' method='post'>")
                self.wfile.write(b'<label for="patient_id">Enter Patient ID or Blank for all Appointments :</label>\
                      <input type="text" id="patient_id" name="patient_id"/><br><br>\
                      <input type="submit" value="View">\
                      </form>')

                self.wfile.write(b"</body></html>")
                return    
            ### View appointmemts


            ### View Records
            if self.path == '/viewRecords':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                records = self.database.viewRecords()
                data = records
                self.wfile.write(b"<html><head><title>Hospital's Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div><a href='/'>Home</a> | \
                             <a href='/addPatient'>Add Patient</a> | \
                             <a href='/scheduleAppointment'>Schedule Appointment</a> | \
                             <a href='/viewAppointments'>View Appointments</a> | \
                             <a href='/dischargePatient'>Discharge Patient</a> | \
                             <a href='/deletePatient'>Delete Patient</a> | \
                             <a href='/updatePatientDetails'>Update Patient Details</a> | \
                             <a href='/viewAllDoctors'>View All Doctors</a>\
                             <a href='/viewRecords'>View All Records</a> </div>")
                self.wfile.write(b"<hr><h2>Viewing All Records</h2>")

                self.wfile.write(b"<table border=2>\
                                <tr><th>Appointment D</th>\
                                    <th>Appointment Date</th>\
                                    <th>Appointment Time</th>\
                                    <th>Doctor's ID </th>\
                                    <th>Doctor's Name </th>\
                                    <th>Doctor's Email </th>\
                                    <th>Doctor's Phone </th>\
                                    <th>Patient Id </th>\
                                    <th>Patient's Name </th>\
                                    <th>Patient's Age </th>\
                                    <th>Admission Date </th>\
                                    <th>Discharge Date </th>\
                                    </tr>")

                for row in data:
                    self.wfile.write(b'<tr><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[5]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[6]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[7]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[8]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[9]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[10]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[11]).encode())                                    
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            ### View Records




            ### Schedule appointmemts
            if self.path == '/scheduleAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a>\
                                 <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr><h2>Schedule Appointiment</h2>")
                
                self.wfile.write(b"<form action='/scheduleAppointment' method='post'>")
                self.wfile.write(b'<label for="patient_id">Patient ID:</label>\
                      <input type="text" id="patient_id" name="patient_id"/><br><br>\
                      <label for="patient_age">Doctor ID:</label>\
                      <input type="number" id="doctor_id" name="doctor_id"><br><br>\
                      <label for="appointment_date">Appoinement Date:</label>\
                      <input type="date"id="appointment_date" name="appointment_date"><br><br>\
                      <label for="appointment_time_date">Appointment Time:</label>\
                      <input type="time"id="appointment_time" name="appointment_time"><br><br>\
                      <input type="submit" value="Schedule">\
                      </form>')                                         
                               
                self.wfile.write(b"</center></body></html>")
                return
            
                #scheduleAppointment
            if self.path == '/viewAppointment':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a></div>")
                self.wfile.write(b"<hr><h2>View Appointiment</h2>")

                self.wfile.write(b"</center></body></html>")
                return
            
                ###discharge Patients
            if self.path == '/dischargePatient':
                discharge_date = date.today().strftime('%Y-%m-%d')
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>\
                                  <a href='/deletePatient'>Delete Patient</a>\
                                  <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                  <a href='/viewAllDoctors'>View All Doctors</a>\
                                  <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr><h2>Discharge Patient</h2>")
                self.wfile.write(b"<form action='/dischargePatient' method='post'>")
                self.wfile.write(b'<label for="patient_id">Enter ID of Patient to Discharge:</label>\
                      <input type="text" id="patient_id" name="patient_id"/><br><br>\
                      <label for="discharge_date">Discharge Date:</label>\
                      <input type="date"id="discharge_date" name="discharge_date"><br><br>\
                      <input type="submit" value="Discharge">\
                      </form>')

            ####Delete Patient
            if self.path == '/deletePatient':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Hospital's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Hospital's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addPatient'>Add Patient</a>|\
                                  <a href='/scheduleAppointment'>Schedule Appointment</a>|\
                                  <a href='/viewAppointments'>View Appointments</a>|\
                                  <a href='/dischargePatient'>Discharge Patient</a>| \
                                  <a href='/deletePatient'>Delete Patient</a>| \
                                 <a href='/updatePatientDetails'>Update Patient Details</a> | \
                                 <a href='/viewAllDoctors'>View All Doctors</a>\
                                 <a href='/viewRecords'>View All Records</a></div>")
                self.wfile.write(b"<hr><h2>Delete Patient</h2>")

                self.wfile.write(b"<form action='/deletePatient' method='post'>")
                self.wfile.write(b'<label for="patient_id">Enter ID of Patient to Delete :</label>\
                      <input type="text" id="patient_id" name="patient_id"/><br><br>\
                      <input type="submit" value="Delete">\
                      </form>')
                
                self.wfile.write(b"</center></body></html>")
                return
            ####Delete Patient 


        except IOError:
                self.wfile.write(b"</center></body></html>")
                return
          
            

def run(server_class=HTTPServer, handler_class=HospitalPortalHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()
