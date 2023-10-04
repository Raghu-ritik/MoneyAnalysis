import DbConfig
import mysql.connector

MYSQL_HOST          =  '20.20.20.133'
MYSQL_USER         =  'root'
MYSQL_PASSWORD          =  ''
MYSQL_DB               =  'vitowix219@ridteam.com'



mysql = mysql.connector.connect(
    host=DbConfig.MYSQL_HOST,
    user=DbConfig.MYSQL_USER,
    password=DbConfig.MYSQL_PASSWORD,
    database=DbConfig.MYSQL_DB
)



# @app.route('/users', methods=['GET'])
# def get_users():
#     cursor = mysql.cursor()
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     cursor.close()
#     return jsonify(users)