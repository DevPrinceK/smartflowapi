import time
import random
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyD4V-9krwKA3CpFj5Vt6zTdBofkV908eRc",
  "authDomain": "smartflow-f427f.firebaseapp.com",
  "databaseURL": "https://smartflow-f427f-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "smartflow-f427f",
  "storageBucket": "smartflow-f427f.appspot.com",
  "messagingSenderId": "517900042843",
  "appId": "1:517900042843:web:e56889e88715a0d113757e"
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

def generate_data(frequency: int):
    '''This function generates data and saves it to the firebase realtime database'''
    while frequency > 0:
        print(f"Remaining Data to Generate ... {frequency}")
        humidity = random.randint(0, 100)
        temperature = random.randint(0, 100)
        moisture = random.randint(0, 100)
        timestamp = time.time()
        data = {
            "humidity": humidity,
            "temperature": temperature,
            "moisture": moisture,
            "timestamp": timestamp,
        }
        database.child("data").push(data, token=None)
        frequency = frequency - 1
        time.sleep(5)
        print(time.time())
    print("Database Successfully Populated!")
    
    
def get_data():
    res = database.child("data").get().val()
    return(dict(res))

generate_data(frequency=50)
# data = get_data().values()
# lst_data = list(data)
# temps = [i['temperature'] for i in lst_data]
# humids = [i['humidity'] for i in lst_data]
# moists = [i['moisture'] for i in lst_data]
# stamps = [i['timestamp'] for i in lst_data]
# # print(data)
# # print(lst_data)
# # print(temps)
# # print(humids)
# # print(moists)
# print(stamps)