import re
from datetime import datetime

from flask import render_template, request, redirect, url_for, flash, session, jsonify
from pkg import app, csrf, mail
from pkg.models import db, Specialty, Doctor, Patient, Appointment, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message 


# --------------- GENERAL PAGES --------------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():

    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') == 'admin':
        return redirect(url_for('admin'))

    if session.get('role') == 'doctor':
        return redirect(url_for('doctor_dashboard'))

    if session.get('role') == 'patient':
        return redirect(url_for('user'))

    session.clear()
    flash('Invalid user role. Please login again.', 'error')
    return redirect(url_for('login'))

#-------------------------------------------------------------------------------------------


@app.route('/doctors')
def doctors():

    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'doctor':
        flash('You are not allowed to access the doctor page.', 'error')
        return redirect(url_for('dashboard'))

    doctors_list = Doctor.query.order_by(Doctor.first_name).all()
    specialties = Specialty.query.order_by(Specialty.name).all()

    doctor_account = Doctor.query.filter_by(
        user_id=session.get('useronline')
    ).first()

    return render_template(
        'doctor.html',
        doctors=doctors_list,
        specialties=specialties,
        appointments=[],
        doctor_account=doctor_account
    )

@app.route('/query/doctors')
def query_doctors():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    doctors_list = Doctor.query.all()
    specialties = Specialty.query.all()

    return render_template(
        'doctor.html',
        doctors=doctors_list,
        specialties=specialties,
        appointments=[],
        doctor_account=None
    )


@app.route('/query/cardiology')
def query_cardiology():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    specialty = Specialty.query.filter_by(name='Cardiology').first()

    if specialty:
        doctors_list = Doctor.query.filter_by(specialty_id=specialty.id).all()
    else:
        doctors_list = []

    return render_template(
        'doctor.html',
        doctors=doctors_list,
        specialties=Specialty.query.all(),
        appointments=[],
        doctor_account=None
    )
    
# ----------------------------------------------------------------------------------------


# ------------ ADMIN ------------

@app.route('/admin/')
def admin():
    
    if session.get('useronline') is None:
        return redirect(url_for('login'))

  
    if session.get('role') != 'admin':
        flash('You are not allowed to access the admin page.', 'error')
        return redirect(url_for('dashboard'))

    specialties = Specialty.query.order_by(Specialty.name).all()
    doctors_list = Doctor.query.order_by(Doctor.first_name).all()
    patients = Patient.query.order_by(Patient.first_name).all()
    appointments = Appointment.query.order_by(
        Appointment.appointment_schedule.desc()
    ).all()

    admin_user = User.query.get(session.get('useronline'))

    return render_template(
        'admin.html',
        specialties=specialties,
        doctors=doctors_list,
        patients=patients,
        appointments=appointments,
        admin_user=admin_user
    )
# --------------------------------------------------------------------------------------------

@app.route('/admin/doctors/add', methods=['GET', 'POST'])
def add_doctor():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        flash('You are not allowed to add doctors.', 'error')
        return redirect(url_for('dashboard'))

    specialties = Specialty.query.order_by(Specialty.name).all()

    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        phone = request.form.get('phone', '').strip()
        specialty_id = request.form.get('specialty_id')
        availability = request.form.get('availability', '').strip()
        licence_number = request.form.get('licence_number', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not first_name or not last_name or not email or not phone:
            flash('Please complete the basic doctor information.', 'error')
            return render_template('add_doctor.html', specialties=specialties)

        if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            flash('Please enter a valid email address.', 'error')
            return render_template('add_doctor.html', specialties=specialties)

        if User.query.filter_by(email=email).first():
            flash('That email is already registered.', 'error')
            return render_template('add_doctor.html', specialties=specialties)

        if not specialty_id or not availability or not licence_number:
            flash('Please complete all doctor fields.', 'error')
            return render_template('add_doctor.html', specialties=specialties)

        if len(password) < 8 or password != confirm_password:
            flash('Password must be 8 characters or more and must match.', 'error')
            return render_template('add_doctor.html', specialties=specialties)

    
        doctor_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=generate_password_hash(password),
            role='doctor'
        )

        db.session.add(doctor_user)
        db.session.flush()

        doctor = Doctor(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            specialty_id=int(specialty_id),
            availability=availability,
            licence_number=licence_number,
            user_id=doctor_user.user_id
        )

        db.session.add(doctor)
        db.session.commit()

        flash('Doctor added successfully.', 'success')
        return redirect(url_for('admin') + '#doctors')

    return render_template('add_doctor.html', specialties=specialties)


@app.route('/admin/doctors/delete/<int:doctor_id>', methods=['POST'])
def delete_doctor(doctor_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        return redirect(url_for('dashboard'))

    doctor = Doctor.query.get_or_404(doctor_id)

    if doctor.appointments:
        flash('This doctor has appointments and cannot be deleted.', 'error')
        return redirect(url_for('admin') + '#doctors')

    doctor_user = doctor.user
    db.session.delete(doctor)

    if doctor_user:
        db.session.delete(doctor_user)

    db.session.commit()
    flash('Doctor deleted successfully.', 'success')
    return redirect(url_for('admin') + '#doctors')


@app.route('/admin/doctors/edit/<int:doctor_id>', methods=['GET', 'POST'])
def update_doctor(doctor_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        return redirect(url_for('dashboard'))

    doctor = Doctor.query.get_or_404(doctor_id)
    specialties = Specialty.query.order_by(Specialty.name).all()

    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        phone = request.form.get('phone', '').strip()
        specialty_id = request.form.get('specialty_id')
        availability = request.form.get('availability', '').strip()
        licence_number = request.form.get('licence_number', '').strip()
        new_password = request.form.get('password', '')

        if not first_name or not last_name or not email or not phone:
            flash('Please complete all required fields.', 'error')
            return render_template('edit_doctor.html', doctor=doctor, specialties=specialties)

        other_user = User.query.filter_by(email=email).first()

        if other_user and other_user.user_id != doctor.user_id:
            flash('That email is already being used.', 'error')
            return render_template('edit_doctor.html', doctor=doctor, specialties=specialties)

        doctor.first_name = first_name
        doctor.last_name = last_name
        doctor.email = email
        doctor.phone = phone
        doctor.specialty_id = int(specialty_id)
        doctor.availability = availability
        doctor.licence_number = licence_number

        if doctor.user:
            doctor.user.first_name = first_name
            doctor.user.last_name = last_name
            doctor.user.email = email
            doctor.user.phone = phone

            if new_password:
                doctor.user.password = generate_password_hash(new_password)

        db.session.commit()
        flash('Doctor updated successfully.', 'success')
        return redirect(url_for('admin') + '#doctors')

    return render_template('edit_doctor.html', doctor=doctor, specialties=specialties)


@app.route('/admin/specialties/add', methods=['POST'])
def add_specialty():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        return redirect(url_for('dashboard'))

    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()

    if not name:
        flash('Specialty name is required.', 'error')
        return redirect(url_for('admin') + '#specialties')

    if Specialty.query.filter_by(name=name).first():
        flash('That specialty already exists.', 'error')
        return redirect(url_for('admin') + '#specialties')

    specialty = Specialty(
        name=name,
        description=description or 'Medical specialty'
    )

    db.session.add(specialty)
    db.session.commit()

    flash('Specialty added successfully.', 'success')
    return redirect(url_for('admin') + '#specialties')


@app.route('/admin/specialties/edit/<int:specialty_id>', methods=['GET', 'POST'])
def edit_specialty(specialty_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        return redirect(url_for('dashboard'))

    specialty = Specialty.query.get_or_404(specialty_id)

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()

        if not name:
            flash('Specialty name is required.', 'error')
            return render_template('edit_specialty.html', specialty=specialty)

        other = Specialty.query.filter_by(name=name).first()

        if other and other.id != specialty.id:
            flash('That specialty already exists.', 'error')
            return render_template('edit_specialty.html', specialty=specialty)

        specialty.name = name
        specialty.description = description or 'Medical specialty'
        db.session.commit()

        flash('Specialty updated successfully.', 'success')
        return redirect(url_for('admin') + '#specialties')

    return render_template('edit_specialty.html', specialty=specialty)


@app.route('/admin/specialties/delete/<int:specialty_id>', methods=['POST'])
def delete_specialty(specialty_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        return redirect(url_for('dashboard'))

    specialty = Specialty.query.get_or_404(specialty_id)

    if specialty.doctors:
        flash('You cannot delete a specialty that has doctors.', 'error')
        return redirect(url_for('admin') + '#specialties')

    db.session.delete(specialty)
    db.session.commit()

    flash('Specialty deleted successfully.', 'success')
    return redirect(url_for('admin') + '#specialties')


@app.route('/admin/patients/<int:patient_id>')
def view_patient(patient_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        return redirect(url_for('dashboard'))

    patient = Patient.query.get_or_404(patient_id)
    appointments = Appointment.query.filter_by(
        patient_id=patient.id
    ).order_by(Appointment.appointment_schedule.desc()).all()

    return render_template(
        'patient_detail.html',
        patient=patient,
        appointments=appointments
    )
    
# ------------------------------------------------------------------------------------------------


# ------------- PATIENT ----------------

@app.route('/user')
def user():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'patient':
        return redirect(url_for('dashboard'))

    patient = Patient.query.filter_by(
        user_id=session.get('useronline')
    ).first()

    if patient is None:
        session.clear()
        flash('Patient account not found.', 'error')
        return redirect(url_for('login'))

    doctors_list = Doctor.query.order_by(Doctor.first_name).all()
    specialties = Specialty.query.order_by(Specialty.name).all()
    appointments = Appointment.query.filter_by(
        patient_id=patient.id
    ).order_by(Appointment.appointment_schedule.desc()).all()

    return render_template(
        'user.html',
        patient=patient,
        doctors=doctors_list,
        specialties=specialties,
        appointments=appointments
    )

# ################ using fetch api to send data to user.html

@app.post('/fetch/doctors/')
@csrf.exempt
def fetch_doctors_with_spec():
    if session.get('useronline') is None:
        return redirect(url_for('login'))
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        spec_id = data.get('spec_id')
        doctors = db.session.query(Doctor).filter_by(specialty_id=spec_id).all()
        result = [{'doc_fname':doc.first_name, 'doc_lname':doc.last_name, 'doc_spec':doc.specialty.name if doc.specialty.name else 'General Medicine'} for doc in doctors ]
        return jsonify(result)
    else:
        return redirect(url_for('user'))
        
    

@app.route('/patient/appointments/book', methods=['POST'])
def book_appointment():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'patient':
        return redirect(url_for('dashboard'))

    patient = Patient.query.filter_by(
        user_id=session.get('useronline')
    ).first()

    if patient is None:
        return redirect(url_for('login'))

    doctor_id = request.form.get('doctor_id')
    appointment_date = request.form.get('appointment_date', '')
    appointment_time = request.form.get('appointment_time', '')
    reason = request.form.get('reason', '').strip()

    if not doctor_id or not appointment_date or not appointment_time or not reason:
        flash('Please complete all appointment fields.', 'error')
        return redirect(url_for('user') + '#appointments')

    doctor = Doctor.query.get_or_404(int(doctor_id))

    try:
        appointment_schedule = datetime.strptime(
            appointment_date + ' ' + appointment_time,
            '%Y-%m-%d %H:%M'
        )
    except ValueError:
        flash('Please enter a valid date and time.', 'error')
        return redirect(url_for('user') + '#appointments')

    appointment = Appointment(
        patient_id=patient.id,
        doctor_id=doctor.id,
        appointment_schedule=appointment_schedule,
        reason=reason,
        status='Pending',
        consultation_fee=0
    )

    db.session.add(appointment)
    db.session.commit()

    flash('Appointment booked successfully.', 'success')
    return redirect(url_for('user') + '#history')


@app.route('/patient/appointments/<int:appointment_id>/cancel', methods=['POST'])
def cancel_appointment(appointment_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'patient':
        return redirect(url_for('dashboard'))

    patient = Patient.query.filter_by(
        user_id=session.get('useronline')
    ).first()
    appointment = Appointment.query.get_or_404(appointment_id)

    # A patient can only cancel their own appointment.
    if patient is None or appointment.patient_id != patient.id:
        flash('You are not allowed to change this appointment.', 'error')
        return redirect(url_for('user'))

    appointment.status = 'Cancelled'
    db.session.commit()

    flash('Appointment cancelled.', 'success')
    return redirect(url_for('user') + '#history')
# -------------------------------------------------------------------------------------------------


# ------------- DOCTOR ------------------

@app.route('/doctor/dashboard')
def doctor_dashboard():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'doctor':
        return redirect(url_for('dashboard'))

    doctor = Doctor.query.filter_by(
        user_id=session.get('useronline')
    ).first()

    if doctor is None:
        session.clear()
        flash('Doctor account not found.', 'error')
        return redirect(url_for('login'))

    doctors_list = Doctor.query.order_by(Doctor.first_name).all()
    specialties = Specialty.query.order_by(Specialty.name).all()
    appointments = Appointment.query.filter_by(
        doctor_id=doctor.id
    ).order_by(Appointment.appointment_schedule.desc()).all()

    return render_template(
        'doctor.html',
        doctor_account=doctor,
        doctors=doctors_list,
        specialties=specialties,
        appointments=appointments
    )


#########################where we use mail to send message

@app.route('/doctor/appointments/<int:appointment_id>/status', methods=['POST'])
def update_appointment_status(appointment_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    if session.get('role') != 'doctor':
        return redirect(url_for('dashboard'))

    doctor = Doctor.query.filter_by(
        user_id=session.get('useronline')
    ).first()
    appointment = Appointment.query.get_or_404(appointment_id)

    # A doctor can only update appointments assigned to them.
    if doctor is None or appointment.doctor_id != doctor.id:
        flash('You are not allowed to change this appointment.', 'error')
        return redirect(url_for('doctor_dashboard'))

    status = request.form.get('status', '')
    allowed_statuses = ['Pending', 'Confirmed', 'Completed', 'Cancelled']

    if status not in allowed_statuses:
        flash('Invalid appointment status.', 'error')
        return redirect(url_for('doctor_dashboard'))

    appointment.status = status 
    db.session.commit()
    
    try:
        if status == 'Confirmed':
            patient_email = appointment.patient.email
            msg = Message(subject='Appointment Confirmed', sender='roiernest01@gmail.com', recipients=[patient_email])
            #msg.body = 'The Doctor has confirmed your appointment'
            msg.html = '''<div style="background:blue; color:white; padding:30px; "> 
                <h1 style="background:white; padding:20px; color:blue;"> Hello Your appointment has been confirmed </h1>
                <img src="https://www.google.com/imgres?q=flower%20pics&imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F38055799%2Fpexels-photo-38055799.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-zoryana-lavruk-509082262-38055799.jpg%26fm%3Djpg&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Frose%2520flower%2F&docid=yzwLliA5Q5yiDM&tbnid=pg-2fzFbuC6YBM&vet=12ahUKEwjercbN3aqXAxW0VkEAHSHtGjkQnPAOegQIMRAA..i&w=3000&h=4000&hcb=2&ved=2ahUKEwjercbN3aqXAxW0VkEAHSHtGjkQnPAOegQIMRAA" width="200"  >
                <p style="border:1px solid white; padding:20px; ">Your Appointment has been confirmed by the Doctor.</p>
            </div>'''
            file_path = 'pkg/static/images/img1.jpg'
            with open(file_path, 'rb') as f:
                msg.attach('About.jpg', 'image/jpeg', f.read() )
            mail.send(msg)
    except:
        return redirect(url_for('doctor_dashboard') + '#appointments')
   

    flash('Appointment status updated.', 'success')
    return redirect(url_for('doctor_dashboard') + '#appointments')

# ------------------------------------------------------------------------------------------------

# ------------ APPOINTMENT DETAILS ---------------

@app.route('/appointments/<int:appointment_id>')
def appointment_detail(appointment_id):
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    appointment = Appointment.query.get_or_404(appointment_id)
    role = session.get('role')


    if role == 'patient':
        patient = Patient.query.filter_by(
            user_id=session.get('useronline')
        ).first()

        if patient is None or appointment.patient_id != patient.id:
            return redirect(url_for('user'))

  
    elif role == 'doctor':
        doctor = Doctor.query.filter_by(
            user_id=session.get('useronline')
        ).first()

        if doctor is None or appointment.doctor_id != doctor.id:
            return redirect(url_for('doctor_dashboard'))


    elif role != 'admin':
        return redirect(url_for('dashboard'))

    return render_template(
        'appointment_detail.html',
        appointment=appointment
    )

#--------------------------------------------------------------------------------------------------


# ---- LOGIN / SIGNUP / LOGOUT --------

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If already logged in, don't show the login page again.
    if session.get('useronline') is not None:
        return redirect(url_for('dashboard'))

    errors = {}
    email = ''

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not email:
            errors['email'] = 'Email is required.'

        if not password:
            errors['password'] = 'Password is required.'

        if not errors:
            user_account = User.query.filter_by(email=email).first()

            if user_account is None or not check_password_hash(
                user_account.password,
                password
            ):
                errors['password'] = 'Invalid email or password.'
            else:
                # Store only the user's ID and role in the session.
                session.clear()
                session['useronline'] = user_account.user_id
                session['role'] = user_account.role

                flash('Login successful.', 'success')
                return redirect(url_for('dashboard'))

    return render_template(
        'login.html',
        error=errors,
        email=email
    )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Public signup creates a patient account.
    errors = {}
    first_name = ''
    last_name = ''
    email = ''
    phone = ''

    if session.get('useronline') is not None:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        phone = request.form.get('phone', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not first_name:
            errors['first_name'] = 'First name is required.'

        if not last_name:
            errors['last_name'] = 'Last name is required.'

        if not email:
            errors['email'] = 'Email is required.'
        elif not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            errors['email'] = 'Please enter a valid email address.'
        elif User.query.filter_by(email=email).first():
            errors['email'] = 'This email is already registered.'

        if not phone:
            errors['phone'] = 'Phone number is required.'

        if len(password) < 8:
            errors['password'] = 'Password must be at least 8 characters.'

        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match.'

        if errors:
            return render_template(
                'signup.html',
                errors=errors,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone
            )

       
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=generate_password_hash(password),
            role='patient'
        )

        db.session.add(new_user)
        db.session.flush()

        new_patient = Patient(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            user_id=new_user.user_id
        )

        db.session.add(new_patient)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))

    return render_template(
        'signup.html',
        errors=errors,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone
    )


@app.route('/logout', methods=['POST'])
def logout():
    if session.get('useronline') is None:
        return redirect(url_for('login'))

    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))




