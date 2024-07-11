import pymysql

def obtener_conexion():
    return pymysql.connect(host='bydmot60f16fgen6jzg6-mysql.services.clever-cloud.com',
                          user='uddstlcsgfq4dbmx',
                          password='EsPl2bBpJtpVQBeFjkZo',
                          db='bydmot60f16fgen6jzg6',
                          port=3306)