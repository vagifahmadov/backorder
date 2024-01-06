from setting.config import *
# apps.config['MONGO_URI'] = 'mongodb://security:Aze1234@ds137508.mlab.com:37508/security?retryWrites=false'

con_mysql = pymysql.connect(host="localhost", user="backorder", password="hDZ8/UJuuzduIq(]", database="backorder")

mysql = con_mysql.cursor()
