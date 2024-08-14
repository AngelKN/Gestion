import pymysql

def obtener_conexion():
    return pymysql.connect(host='betngwc5ohto5j57at2o-mysql.services.clever-cloud.com',
                          user='ukjfe3vekczw06ds',
                          password='K5UxfBSrIWJptj1MVJtE',
                          db='betngwc5ohto5j57at2o',
                          port=3306)