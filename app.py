from setting.config import apps
<<<<<<< HEAD
from services.services import select_data, insert_data, update_data, index, auth, login, logout
=======
from services.services import select_data, insert_data, update_data, index, login, logout, auth
>>>>>>> 6089a9c6 (08.06.2024)

apps.register_blueprint(index)
apps.register_blueprint(auth)
apps.register_blueprint(login)
apps.register_blueprint(logout)

apps.register_blueprint(select_data)
apps.register_blueprint(insert_data)
apps.register_blueprint(update_data)
apps.register_blueprint(login)
apps.register_blueprint(logout)
apps.register_blueprint(auth)

if __name__ == '__main__':
    apps.run(debug=True, port=1985, host='localhost')


