from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Specialty(db.Model):
    __tablename__ = 'specialty'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    doctors = db.relationship('Doctor', backref='specialty', lazy=True)


class Doctor(db.Model):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialty.id'))
    availability = db.Column(db.String(50), nullable=False)
    licence_number = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # NEW: connects the doctor's profile to the account used for login.
    # Authentication information stays in User; doctor information stays here.
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), unique=True, nullable=True)

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)


class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

    # NEW: connects the patient profile to the login account.
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), unique=True, nullable=True)

    appointments = db.relationship('Appointment', backref='patient', lazy=True)


class Appointment(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    appointment_schedule = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(100), nullable=False, default='Pending')
    consultation_fee = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(12), nullable=False)

    # Existing column is called password in your database.
    # It contains a HASH, never the original password.
    password = db.Column(db.String(255), nullable=False)

    # NEW: one simple role field for Task 9.
    # Allowed values: patient, doctor, admin.
    role = db.Column(db.String(20), nullable=False, default='patient')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # NEW: profile relationships.
    patient_profile = db.relationship('Patient', backref='user', uselist=False, foreign_keys='Patient.user_id')
    doctor_profile = db.relationship('Doctor', backref='user', uselist=False, foreign_keys='Doctor.user_id')

