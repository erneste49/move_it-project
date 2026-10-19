from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from pkg.models import db, Post, User
from flask_httpauth import HTTPBasicAuth

apii = Blueprint('api', __name__, url_prefix='/api/v1')

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    user = User.query.filter(User.username == username).first()
    if user:
        return user.password_hash
    else:
        return None
    
@auth.error_handler
def unauthorised(error):
    return jsonify({
                'status': 'failure',
                'message': 'You are not authorised',
                'data': {}
            }), 401
    

@apii.route('/register/', methods=["POST"])
def register():
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        if username != None and email != None and password != None:
            uname = db.session.query(User).filter(User.username == username).first()
            uemail = db.session.query(User).filter(User.email == email).first()
            if uname:
                return jsonify({
                    'status': 'failure',
                    'message': 'Username already exist',
                    'data': {}
                }), 400
            if uemail:
                return jsonify({
                    'status': 'failure',
                    'message': 'Email already exist',
                    'data': {}
                }), 400
            #password_hash = generate_password_hash(password)
            user = User(username=username, email=email, password_hash=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': 'Your account has been created successfully',
                'data': {}
            }), 201
        else:
            return jsonify({
                'status': 'failure',
                'message': 'All fields are required',
                'data': {}
            }), 400
    
    else:
         return jsonify({
            'status': 'failure',
            'message': 'Request type should be post and data should be json',
            'data': {}
        }), 400


@apii.route("/post/all/")    #to access route --> http:127.0.0.1.5000/api/v1/post/all/ 
##@auth.login_required
def api_all():
    posts = db.session.query(Post).all()
    #converting post from list of Post object to list of dictionary object below
    my_posts = []
    for post in posts:
        post_dict = {}
        post_dict['post_id'] = post.id
        post_dict['post_title'] = post.title
        post_dict['post_content'] = post.content
        post_dict['post_image'] = f'http://127.0.0.1:5000/static/uploads/{post.image}'
        post_dict['post_created_at'] = post.created_at
        
        my_posts.append(post_dict)
        
    if my_posts:
         return jsonify({
                'status':'success',
                'message':'Posts fetched successfully',
                'data': my_posts
            }),200
    else:
         return jsonify({
                'status':'success',
                'message':'No posts yet',
                'data': []
            }), 200
         
@apii.route("/post/single/<int:post_id>/")
#@auth.login_required
def post_single(post_id):
    post = db.session.query(Post).get(int(post_id))
    
    
    if post:
        post_dict = {}
        post_dict['post_id'] = post.id
        post_dict['post_title'] = post.title
        post_dict['post_content'] = post.content
        post_dict['post_image'] = f'http://127.0.0.1:5000/static/uploads/{post.image}'
        post_dict['post_created_at'] = post.created_at
        
        return jsonify({
            'status':'success',
            'message':'Post fetched successfully',
            'data': post_dict
        }),200
    else:
        return jsonify({
            'status':'failure',
            'message':'No post found with that id',
            'data': {}
        }), 404
        
@apii.route("/post/create/", methods=['POST'])
def post_create():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        image = data.get('image')
        if title == None or content == None:
            return jsonify({
                'status': 'failure',
                'message': 'Title and content is required',
                'data': {}
            }), 400
        else:
            if image != None:
                post = Post(title=title, content=content, image=image)
                db.session.add(post)
                db.session.commit()
                post_dict = {}
                post_dict['post_id'] = post.id
                post_dict['post_title'] = post.title
                post_dict['post_content'] = post.content
                post_dict['post_image'] = f'http://127.0.0.1:5000/static/uploads/{post.image}'
                post_dict['post_created_at'] = post.created_at
                # return jsonify({
                #     'status': 'success',
                #     'message': 'Post created successfully',
                #     'data': post_dict
                # }), 201
            else:
                post= Post(title=title, content=content)
                db.session.add(post)
                db.session.commit()
                post_dict = {}
                post_dict['post_id'] = post.id
                post_dict['post_title'] = post.title
                post_dict['post_content'] = post.content
                post_dict['post_image'] = None
                post_dict['post_created_at'] = post.created_at
                return jsonify({
                    'status': 'success',
                    'message': 'Post created successfully',
                    'data': post_dict
                }), 400

    else:
        return jsonify({
            'status': 'failure',
            'message': 'Request type should be post and data should be json',
            'data': {}
        }), 400
    
    # return
