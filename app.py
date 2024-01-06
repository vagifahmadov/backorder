from setting.config import apps
from services.services import select_data, insert_data, update_data, index

apps.register_blueprint(index)
apps.register_blueprint(select_data)
apps.register_blueprint(insert_data)
apps.register_blueprint(update_data)

if __name__ == '__main__':
    apps.run(debug=True, port=1985, host='localhost')


