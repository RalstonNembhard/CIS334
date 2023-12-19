create database hospital_portal;
use hospital_portal;
create table patients (
	patient_id int not null unique auto_increment primary key,
    patient_name varchar(45) not null,
    age int not null,
    admission_date date,
    discharge_date date
    );
    
    create table doctors(
	doctor_id int not null unique auto_increment primary key,
	doctor_name varchar(45),
	email varchar(45),
	phone varchar(25)
    );
create table appointments(
	appointment_id int not null unique auto_increment primary key,
    patient_id int not null,
    doctor_id int not null,
    appointment_date date not null,
    appointment_time decimal not null,
     foreign key (doctor_id)  references doctors(doctor_id),	
     foreign key (patient_id) references patients(patient_id)	
		on delete cascade
	);
    
INSERT INTO patients (patient_name, age, admission_date, discharge_date) VALUES
("Mark Wilson", "37","2023-10-25","2023-11-25"),
("Luke Wellington","78","2023-10-2","2023-10-30"),
("Leslie Agustine","33","2023-10-1","2023-10-10"),
("Ansley Martine","28","2023-11-1","2023-11-5"),
("Earl Baldwin","77","2023-10-29","2023-11-1"),
("Trudy Golde","14","2023-10-5","2023-11-3")
;
insert into doctors(doctor_name,email,phone) values 
("Heather Carter","h.carter@email.com", "555-301-2201"),
("Gary John","g.john@email.com", "555-321-5565"),
("Terry Vargas","t.vargas@email.com", "555-456-5231")
;

insert into appointments(patient_id, doctor_id, appointment_date,appointment_time) values 
("1","2", "2023-11-10","2"),
("4","1", "2023-9-12","5"),
("3","2", "2023-12-20","12"),
("2","2", "2023-12-8","2"),
("6","1", "2023-12-10","5"),
("5","2", "2023-12-30","12");




-- Procedure to schedule appointments

DELIMITER //

create procedure ScheduleAppointment(
    in shPatient_id int,
    in shDoctor_id int,
    in shAppointment_date date,
    in shAppointment_time time
)
BEGIN
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time)
    VALUES (shPatient_id, shDoctor_id, shAppointment_date, shAppointment_time);
END //

DELIMITER ;

-- Procedure to delete patients

create procedure deletePatient(IN delpatient_id INT)
delete FROM Patients WHERE patient_id = delpatient_id;


-- Procedure to  display appointments

DELIMITER //
create procedure GetAppointments(
    IN  viewPatient_id int
)
BEGIN
    IF viewPatient_id is null then
        -- return all appointments if patient ID entered is NULL
        select
            patients.patient_id,
            patients.patient_name,
            doctors.doctor_id,
            doctors.doctor_name,
            appointments.appointment_date,
            appointments.appointment_time
        from
            appointments
        join
            patients on appointments.patient_id = patients.patient_id
        join
            doctors on appointments.doctor_id = doctors.doctor_id;
    else
        --  return appointment for patient Id entered
        select
            patients.patient_id,
            patients.patient_name,
            doctors.doctor_id,
            doctors.doctor_name,
            appointments.appointment_date,
            appointments.appointment_time
		from
            appointments
        join
            patients on appointments.patient_id = patients.patient_id
        join
            doctors on appointments.doctor_id = doctors.doctor_id
        where
            appointments.patient_id = viewPatient_id;
    END IF;
END //
DELIMITER ;

-- Procedure to edit patient information

DELIMITER //

CREATE PROCEDURE EditPatient(
    IN editPatient_id INT,
    IN editPatient_name VARCHAR(45),
    IN editAge INT,
    IN editAdmission_date DATE,
    IN editDischarge_date DATE
)
BEGIN
	set editAge = IF(editAge = 0, NULL, editAge);
    
	update patients
       set
       patient_name = IFNULL(editPatient_name, patient_name),
        
        age = IFNULL(EditAge, age),
        admission_date = IFNULL(editAdmission_date, admission_date),
        discharge_date = IFNULL(editDischarge_date, discharge_date)
    where patient_id = editPatient_id;
END //

DELIMITER ;

-- Procedure to dischharge patients

DELIMITER //
create procedure  DischargePatient(
    in uPatient_id int,
    in uDischarge_date date
)
begin
    update patients
    set discharge_date = Udischarge_date
    where patient_id = uPatient_id;
end //

DELIMITER ;

create view appointment_doctors_patients AS
select
    ap.appointment_id,
    ap.appointment_date,
    ap.appointment_time,
    doc.doctor_id,
    doc.doctor_name,
    doc.email AS doctor_email,
    doc.phone AS doctor_phone,
    pa.patient_id,
    pa.patient_name,
    pa.age,
    pa.admission_date,
    pa.discharge_date
from
    patients pa
left JOIN appointments ap ON pa.patient_id = ap.patient_id
left JOIN doctors doc ON ap.doctor_id = doc.doctor_id;





