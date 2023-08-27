import random
import time
import pyrebase
from api.firebase_config import firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

def generate_data(frequency: int):
    '''This function generates data and saves it to the firebase realtime database'''
    while frequency > 0:
        humidity = random.randint(0, 100)
        temperature = random.randint(0, 100)
        moisture = random.randint(0, 100)
        data = {
            "humidity": humidity,
            "temperature": temperature,
            "moisture": moisture,
        }
        database.child("").push(data)
        frequency =- 1
        time.sleep(5)
    print("Database Successfully Populated!")