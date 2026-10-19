from flask import render_template, request, make_response, redirect, session, url_for
from pkg import app, csrf
from pkg.forms import RegisterForm
from pkg.contact import ContactForm
from pkg.models import db 
#from pkg.models import user
from sqlalchemy import text, select, func


@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate' 
    return response
    


@app.route('/')
def home():
    firstname = '   <script> alert ("alexander the great")</script>     '
    employees = ["Janet", "Sam", "Gbolahan", "Lola"]
    nums = [1,2,3,4,5]
    team = {"CEO":"Alhaji Dangote", "secretary": "Mayor Olu", "President":"Prof Yemi", "Chairman":"Bola Tinubu"}
    return render_template("index.html" ,score=80, nums=nums, age="You are 38 years old", fname=firstname, list=employees, team=team )

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         email = request.form.get('email')   
#         pwd = request.form['password']
#         return f"{email} Thank you for logging in your password is {pwd} "
#     else:
#      return render_template("login.html")
 
 
@app.get('/login/')
def login():
     return render_template("login.html")
 
@app.post('/process/')
def process():
    email = request.form.get('email')
    pwd = request.form.get('password')
    return f"Thank you {email} for using our app"

@app.route('/post/')
def post():
    return render_template("post.html")


##using dynamic route to get username from url and attaching it to page
@app.route("/user/<username>/")
def get_user(username):
    return f"Your username is: {username}"

@app.get('/notify/')
def notify():
    submitted = []
    nwemail = request.args.get('newemail')
    submitted.append(nwemail)
    print(submitted)
    return f"{nwemail} Thank you your email has been saved."

@app.route("/register/", methods=['GET', 'POST'])
def student_register():
    form = RegisterForm()
    if form.validate_on_submit():       ##to add condition to validate form 
        # username = request.form.get('username')   #using request.get method
        # firstname = request.form.get('firstname')
        
        username= form.username.data        #using request.data when using a form attribute from flask 
        firstname = form.firstname.data
        lastname = form.lastname.data
        return f"""{firstname}  {lastname} Thank you for creating an Account. 
        {username} Successfully Registered"""
    return render_template("register.html", myform=form )


@app.route('/signin/', methods=['POST', 'GET'])
## @csrf.exempt
def signin():
    passcodes = ['1111', '2222', '3333', '4444' ]
    if request.method== 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        if username != '' and password in passcodes:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('signin'))
        return "<h1>You are logged in </h1>"
    return render_template('signin.html')

@app.route("/dashboard/")
def dashboard():
    if session.get('username') == None:
        return redirect('/signin') 
    return render_template("dashboard.html")

@app.route("/profile/")
def profile():
    if session.get('username') == None:
        return redirect('/signin')
    return render_template("profile.html")

@app.post("/logout/")
def logout():
    session.clear()
    return redirect(url_for('signin'))

@app.route('/contact/', methods=['POST', 'GET'])
def contact():
    cform= ContactForm()
    if cform.validate_on_submit():
        fullname = cform.fullname.data
        email = cform.email.data
        message = cform.message.data
        return f"{fullname}, Thanks for contacting us with {email}"
    return render_template('contact.html', form=cform)


@app.route('/set_cookie/', methods=['GET', "POST"])
def set_cookie():
    if request.method == "POST":
        resp = make_response(redirect("/"))
        resp.set_cookie('fullname', 'Mark Henry', max_age=30*24*60*60 ) ##how to set cookie
        resp.set_cookie('age', '25', max_age=30*24*60*60)
        return resp
    return render_template("cookie_page.html")


@app.route('/get_cookie/')
def get_cookie():
    fname = request.cookies.get('fullname')
    return render_template("my_page.html", fname=fname)


@app.route('/travel/', methods=["POST", "GET"])
def travel():
    if request.method == "POST":
        continent = request.form.get("continent")
        feedback = make_response(redirect("/advice"))
        feedback.set_cookie('continent', continent, max_age=30*24*60*60 )
        return feedback
    return render_template("continent.html" )


@app.route("/advice/", methods=["POST", "GET"])
def advice():
    continent = request.cookies.get("continent")
    return render_template("advice.html", continent=continent)
    
##below how to expire a cookie     
@app.route("/delete_cookie/")
def delete_cookie():
    resp = make_response(redirect("/get_cookie"))
    resp.set_cookie('fullname',  max_age=-30*24*60*60 )
    resp.set_cookie('age', max_age=-30*24*60*60  )
    return resp


@app.route("/set_session")
def set_session():
    session['firstname'] = 'Andrew'
    session['lastname'] = 'Thomas'
    return "Session Data has been set"

@app.route("/delete_session")
def delete_session():
    # session.pop('firstname')
    # session.pop('lastname')
    ##to clear every session at once below line
    session.clear()
    return redirect("/")


# @app.route('/insert/')
# def insert():
#     query = "INSERT INTO users SET name='gabe', email='gabe@example.com', message='Hello i am gabe' "
#     db.session.execute(text(query)) 
#     db.session.commit()
#     return "Record inserted successfully"

'''
@app.route("/retrieve/")
def retrieve():
    query = "SELECT * FROM users"
    result = db.session.execute(text(query))
    records = result.fetchall()
    print(records)
    return "Record retrieved"


@app.route("/core/insert") 
def sqlcorel():
    print("*** USER REGISTRATION FORM ***")
    u_name = "Helen"
    u_email = "helen@gmail.com"
    u_message = "hello i am helen, welcome"
    
    stmt = user.insert().values(
        name = u_name,
        email = u_email,
        message = u_message
    )
    result = db.session.execute(stmt)
    db.session.commit()
    return str(result.lastrowid)
    

@app.route("/core2/insert", methods=["GET", "POST"] )
def sqlcore_insert2():
    if request.method == "POST":
        u_name = request.form.get("username")
        u_email = request.form.get("user_email")
        u_message = request.form.get("user_message")
        
        statement = user.insert().values(
            name = u_name ,
            email = u_email,
            message = u_message
        )
        
        result = db.session.execute(statement)
        db.session.commit()
        
        return f"Success!.. User {u_name} has been inserted with ID: {result.lastrowid}"
    return render_template("user_form.html")



@app.route("/update/user")
def update_user():
    update_stmt = (
        db.update(user)
        .where(user.c.id == 29 )
        .values(name = "Smith", email = "smith@gmail.com" )
    )
    db.session.execute(update_stmt)
    db.session.commit()
    return "User Updated"

#updating user from form
@app.route("/update/old_user", methods=["GET", "POST"] )
def update_new_user():
    if request.method == "POST":
        id_no = request.form.get("old_id")
        new_name = request.form.get("new_username")
        new_email = request.form.get("new_user_email")
        new_message = request.form.get("new_user_message")
        
        update_stmt = (
            db.update(user)
            .where(user.c.id == id_no )
            .values(name = new_name, email = new_email, message=new_message )
        )
        db.session.execute(update_stmt)
        db.session.commit()
        # if id_no not in db(user):
        #     return "Record does not exist"
        return f"Old User Updated with Name: {new_name} | Email: {new_email}"
    return render_template("update_user_form.html")



#updating from terminal
# @app.route("/update_new_user")
# def update_new_user():
#     id_no = input("Enter existing id to update: ")
#     new_name = input("Enter new name to update with: ")
#     new_email = input("Enter the new email to update with: ")
#     new_message = input("Enter the new message: ")
    
#     update_stmt = (
#         db.update(user)
#         .where(user.c.id == id_no )
#         .values(name = new_name, email = new_email, message=new_message )
#     )
#     db.session.execute(update_stmt)
#     db.session.commit()
#     return "Old User Updated"





@app.route("/view/all_users")
def view_all_users():
    stmt = select(user)
    all_product = db.session.query(user).all()    
    #all_product = user.query.all()
    return render_template("view_user_data.html", all_data = all_product )
    
    
#selecting only a particular user
@app.route("/select/user")
def view_user():
    stmt = select(user)
    all_product = db.session.query(user.c.name, user.c.id).all()
    #all_product = user.query.all()
    return render_template("view_user_data.html", all_data = all_product )


@app.route("/count/user")
def count_user():
    total_user = db.session.query(user).count()
    return f"The total number of users: {total_user}"



@app.route("/first/user")
def first_user():
    total_user = db.session.query(user).first()
    return (f"First: {total_user}")


@app.route("/filter_data")
def filter_data():
    statement = db.session.query(user.c.id == 2)      
    filtered_data = db.session.execute(statement).first()
    
    #f_data2 = db.session.query(user).get(2)    #same as statement & ifltered_data above
    
    if filtered_data:
        print(f"User iD is 2 | Name: {filtered_data.name} | Email:{filtered_data.email} ")
    else:
        return ("User not found!")



@app.route("/list/guest/<guestid>")
def get_guest(guestid):
    if not guestid.isdigit():
        return "Invalid ID format provided", 400
    
    guest_id = int(guestid)
    
    stmt = select(user).where(user.c.id == guest_id)
    found_user = db.session.execute(stmt).first()
    
    if found_user is None:
        return "Guest not found in database", 404
    return f"Guest found: ID: {found_user.id} - Name: {found_user.name} - Email: {found_user.email} "


@app.route("/f/user")
def filt_user():
    # stmt = select(user).where(user.c.id >= 10)
    # result = db.session.execute(stmt).fetchall()   
    result2 = db.session.query(user).filter(user.c.id >= 15).all()  #does same work as line 322 and 323
    
    return render_template("filter_data.html", all_data=result2)

'''



