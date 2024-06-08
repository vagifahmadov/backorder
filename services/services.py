<<<<<<< HEAD
from setting.config import (request, Blueprint, jsonify, session, render_template,
                            jwt, make_response, timedelta, datetime, apps, redirect)
=======
from setting.config import request, Blueprint, jsonify, session, render_template, jwt, make_response, timedelta, datetime, apps, redirect
>>>>>>> 6089a9c6 (08.06.2024)
from objects.defs import token_required

index = Blueprint('/', __name__)


@index.route('/', methods=['GET'])
@token_required
def index_func():
    # vars
    if not session.get('logged_in'):
        return render_template('pages/samples/login.html')
    else:
        return render_template('index.html')


auth = Blueprint('/auth', __name__)


@auth.route('/auth', methods=['GET'])
@token_required
def auth_func():
    return 'JWT is verified. Welcome to your dashboard !  '


# Login page

login = Blueprint('/login', __name__)


<<<<<<< HEAD
@login.route('/login', methods=['POST', 'GET'])
def login_func():
    if request.method == "POST":
        if request.form['username'] and request.form['password'] == '123456':
            session['logged_in'] = True

            token = jwt.encode({
                'user': request.form['username'],
                # don't forget to wrap it in str function, otherwise it won't work [ I struggled with this one! ]
                'expiration': str(datetime.utcnow() + timedelta(seconds=5))
            },
                apps.config['SECRET_KEY'])
            result = {'token': token}
            print(result)
            return redirect('/')
        else:
            return render_template('pages/samples/error.html', data={"message": "Unable to verify", 'error': 403})
=======
@login.route('/login', methods=['POST'])
def login_func():
    usr_nm = request.form['username']
    passw = request.form['password']
    if usr_nm and passw == '111':
        session['logged_in'] = True
        print(f'\n\n\n\nrequired: \t{usr_nm}|{passw}\n\n\n\n')
        token = jwt.encode(
            payload={
                'user': request.form['username'],
                # don't foget to wrap it in str function, otherwise it won't work [ i struggled with this one! ]
                'expiration': str(datetime.utcnow() + timedelta(seconds=60))
            },
            key=apps.config['SECRET_KEY'],
            algorithm="HS256"
        )
        session['token'] = token
        print({'token': token})
        return redirect('/')
>>>>>>> 6089a9c6 (08.06.2024)
    else:
        return render_template("pages/samples/login.html")


# Homework: You can try to create a logout page

logout = Blueprint('/logout', __name__)


<<<<<<< HEAD
@logout.route('/logout', methods=['POST'])
@token_required
def logout_func():
    render_template("pages/samples/login.html")
=======
@logout.route('/logout', methods=['GET'])
@token_required
def logout_func():
    session['token'] = False
    session['logged_in'] = False
    return redirect('/')
>>>>>>> 6089a9c6 (08.06.2024)


# your code goes here


select_data = Blueprint('selectData', __name__)


@select_data.route('/selectData', methods=['GET'])
@token_required
def select_data_func():
    # vars
    id_b = request.args.get("id")
    if id_b is not None:
        statement = "id"
        statement_value = id_b
        condition = "="
    else:
        statement = ""
        statement_value = ""
        condition = ""

    output = {"ok"}
    return jsonify({'data': output})


insert_data = Blueprint('insertData', __name__)


@insert_data.route('/insertData', methods=['POST'])
@token_required
def insert_data_func():
    data_request = request.json
    key_list = list(data_request.keys())
    query_schema = []
    list(map(lambda qs: query_schema.append({qs: data_request[qs]}), key_list))

    output = {"result"}
    return jsonify({'data': output})


update_data = Blueprint('updateData', __name__)


@update_data.route('/updateData', methods=['PUT'])
@token_required
def update_data_func():
    data_request = request.json
    key_list = list(data_request.keys())
    statement_key = "id"
    statement_type = "="
    query_schema = []
    list(map(lambda qs: query_schema.append({qs: data_request[qs]}), key_list))

    output = {"result"}
    return jsonify({'data': output})
