import cv2
from simple_facerec import SimpleFacerec
import pandas as pd
from datetime import datetime
import openpyxl


# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

data = pd.DataFrame(columns=["Name", "Date", "Timestamp"])

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        now = datetime.now()
        date = now.date()
        timestamp = now.strftime("%H:%M:%S")
        data = data._append({"Name": name, "Date": date, "Timestamp": timestamp}, ignore_index=True)


    cv2.imshow("FoC Live Camera Feed", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
data.to_excel("face_rec_data.xlsx", index=False)
print(data)
cap.release()
cv2.destroyAllWindows()





