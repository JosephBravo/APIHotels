from pymongo import MongoClient

try:
    conn = MongoClient()
except:
    print("NO CONEXION")
