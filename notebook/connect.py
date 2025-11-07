from pymongo import MongoClient, errors
from dotenv import load_dotenv
load_dotenv()
import os
# Cargar entorno en en selecector de entorno para que fuqueione la conexion
MONGO_URI_ATLAS = os.getenv("MONGODB_URI_Atlas")
DATABASE_NAME = os.getenv("MongoDB_Data")
print("MongoDB URI:", MONGO_URI_ATLAS)
print("Database Name:", DATABASE_NAME)
try:
    client = MongoClient(MONGO_URI_ATLAS)
    print("Conectado a Mongo atlas correctamente.")
    db = client[DATABASE_NAME]

    collections = db.list_collection_names()
    print("Conectado atlas a base de datos", (DATABASE_NAME))
    print("Collections: ", collections)
except errors.ServerSelectionTimeoutError as err:
    print("Fallo de conexion a db MongoDB Atlas:", err)

except errors.OperationFailure as e:
    print("Error de autenticación:", e)