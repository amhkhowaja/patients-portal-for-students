"""Patient API Controller"""

from flask import Flask , request
from patient_db import PatientDB


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """
    def get_patients(self):
        try:
            patients = self.patient_db.select_all_patients()
            if patients is not None:
                return ({"status": "success", "patients": patients}), 200
            else:
                return ({"status": "error", "message": "Failed to retrieve patients"}), 400
        except Exception as e:
            return ({"status": "error", "message": str(e)}), 500
    pass
    def create_patient(self):
        try:
            patient_id = self.patient_db.insert_patient(request.json)
        
            return ({"status": "success", "message": "Patient created successfully", "patient_id": patient_id}), 201
        except:
            return ({"status": "error", "message": "Failed to create patient"}), 500
        pass
   
    def get_patient(self, patient_id):
        try:
            patient = self.patient_db.select_patient(patient_id)
            if patient is not None:
                return ({"status": "success", "patient": patient}), 200
            else:
                return ({"status": "error", "message": "Patient not found"}), 404
        except Exception as e:
            return ({"status": "error", "message": str(e)}), 500
        pass

    def update_patient(self, patient_id):
        try:
            success = self.patient_db.update_patient(patient_id, request.json)
            if success:
                return ({"status": "success", "message": "Patient updated successfully"}), 200
            else:
                return ({"status": "error", "message": "Failed to update patient"}), 404
        except Exception as e:
            return ({"status": "error", "message": str(e)}), 500
        pass

    def delete_patient(self, patient_id):
        try:
            success = self.patient_db.delete_patient(patient_id)
            if success:
                return ({"status": "row deleted", "message": "Patient deleted successfully"}), 200
            else:
                return ({"status": "error", "message": "Patient not found"}), 404
        except Exception as e:
            return ({"status": "error", "message": str(e)}), 500
        pass

    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
