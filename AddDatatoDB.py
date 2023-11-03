import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("face-612cb-firebase-adminsdk-wz44r-d3a13202fc.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-612cb-default-rtdb.firebaseio.com/",
    # 'storageBucket':"face-612cb.appspot.com"
})

ref =db.reference('User')

data = {

"1319":
        {
            "name":"Yassar Shitu Mukhtar",
            "course":"Computer Sci and Info",
            "dept": "Computer SCi",
            "last_attendace_time":"2022-12-11 11:54:34"

        },
"1380":
        {
            "name":"Ahmad Abdulrahman",
            "course":"Software Engineering",
            "dept": "Computer SCi",
            "last_attendace_time":"2022-12-11 11:54:34"

        },
"1403":
        {
            "name":"Mahmud L Yakuku",
            "course":"Software Engineering",
            "dept": "Computer SCi",
            "last_attendace_time":"2022-12-11 11:54:34"

        },

}

for key,value in data.items():
    ref.child(key).set(value)
