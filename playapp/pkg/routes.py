from flask import render_template, request
from pkg import app

@app.route('/')
def home():
    firstname = '   <script> alert ("alexander the great")</script>     '
    employees = ["Janet", "Sam", "Gbolahan", "Lola"]
    nums = [1,2,3,4,5]
    team = {"CEO":"Alhaji Dangote", "secretary": "Mayor Olu", "President":"Prof Yemi", "Chairman":"Bola Tinubu"}
    return render_template("index.html" ,score=40, nums=nums, age="You are 38 years old", fname=firstname, list=employees, team=team )

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


