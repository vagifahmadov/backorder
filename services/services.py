from setting.config import (request, Blueprint, jsonify, session, render_template,
                            jwt, make_response, timedelta, datetime, apps, redirect)
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


@auth.route('/auth')
@token_required
def auth_func():
    return 'JWT is verified. Welcome to your dashboard !  '


# Login page

login = Blueprint('/login', __name__)


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
    else:
        return render_template("pages/samples/login.html")


# Homework: You can try to create a logout page

logout = Blueprint('/logout', __name__)


@logout.route('/logout', methods=['POST'])
@token_required
def logout_func():
    render_template("pages/samples/login.html")


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
