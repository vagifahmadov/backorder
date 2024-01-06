from setting.config import request, Blueprint, jsonify, make_response, jwt, JWTManager, create_access_token, url_for, sha256

index = Blueprint('/', __name__)


@index.route('/', methods=['GET'])
def index_func():
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

    output = "ok"
    return jsonify({'data': output})


select_data = Blueprint('selectData', __name__)


@select_data.route('/selectData', methods=['GET'])
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
def insert_data_func():
    data_request = request.json
    key_list = list(data_request.keys())
    query_schema = []
    list(map(lambda qs: query_schema.append({qs: data_request[qs]}), key_list))

    output = {"result"}
    return jsonify({'data': output})


update_data = Blueprint('updateData', __name__)


@update_data.route('/updateData', methods=['PUT'])
def update_data_func():
    data_request = request.json
    key_list = list(data_request.keys())
    statement_key = "id"
    statement_type = "="
    query_schema = []
    list(map(lambda qs: query_schema.append({qs: data_request[qs]}), key_list))

    output = {"result"}
    return jsonify({'data': output})

