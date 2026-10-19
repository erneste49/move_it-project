
from pkg import app, db
from pkg.models import user




def sqlcorel():
    print("*** USER REGISTRATION FORM ***")
    u_name = input("Enter your name: ")
    u_email = input("Enter your email: ")
    u_message = input("Write your message: ")
    
    with app.app_context():
        db.create_all()
    
    stmt = user.insert().values(
        name = u_name,
        email = u_email,
        message = u_message
    )
    result = db.session.execute(stmt)
    db.session.commit()
    return f"Success!.. User {u_name} Inserted with ID:{result.lastrowid}"

# if __name__ == "__main__":
#     add_user_cli() 

