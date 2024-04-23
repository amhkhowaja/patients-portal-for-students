"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""



import uuid
from datetime import datetime
from config import GENDERS, WARD_NUMBERS, ROOM_NUMBERS
from api_controller import PatientAPIController  # Updated import statement

class Patient:
    def __init__(self, name, gender, age):
        self.id = str(uuid.uuid4())  
        self.name = name
        self.gender = gender
        self.age = age
        self.checkin = datetime.now()
        self.checkout = None
        self.room = None
        self.ward = None




    def set_room(self, room):
        if room in ROOM_NUMBERS.values():
            self.room = room
        else:
            raise ValueError("Invalid room number")

    def set_ward(self, ward):
        if ward in WARD_NUMBERS:
            self.ward = ward
        else:
            raise ValueError("Invalid ward number")

    def get_id(self):
        return self.id

    def get_name(self): 
        return self.name

    def commit(self):
        api_controller = PatientAPIController()
        api_controller.create_patient({
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "checkin": str(self.checkin),
            "checkout": str(self.checkout),
            "room": self.room,
            "ward": self.ward
        })

        
    
    def commit(self):
       
        existing_patient = Patient.query.filter_by(room=self.room, ward=self.ward).first()
        if existing_patient:
            existing_patient.name = self.name
            existing_patient.age = self.age
            db.session.commit()
        else:
            db.session.add(self)
            db.session.commit()
