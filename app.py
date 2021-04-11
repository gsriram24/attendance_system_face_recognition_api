import flask
from flask import request, jsonify
import face_recognition
import numpy as np
import urllib
import requests

app = flask.Flask(__name__)


cached_image_encodings = {}


@app.route('/', methods=['POST'])
def api_id():
    known_image_encodings = []
    known_face_ids = []
    try:
        token = request.headers['Authorization']
    except KeyError:
        return jsonify({"message": "Not authorized, no token"}), 401
    class_id = request.form['classId']
    req_url = f'https://attendancesystemadmin.herokuapp.com/api/student/byClass/{class_id}'
    headers = {"Authorization": f'{token}'}

    response = requests.get(req_url, headers=headers)

    if(response.status_code == 401):
        return jsonify(response.json()), 401

    students = response.json()

    for student in students['students']:

        known_face_ids.append(student['_id'])
        if(student['_id'] in cached_image_encodings):
            encoding = cached_image_encodings[student['_id']]
        else:
            response = urllib.request.urlopen(student['images'][0])
            image = face_recognition.load_image_file(response)
            encoding = face_recognition.face_encodings(image)
            cached_image_encodings[student['_id']] = encoding
        known_image_encodings.append(encoding[0])

    file = request.files['file']
    unknown_image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(
        unknown_image, model="hog")
    face_encodings = face_recognition.face_encodings(
        unknown_image, face_locations)

    face_ids = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(
            known_image_encodings, face_encoding)
        face_distances = face_recognition.face_distance(
            known_image_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            known_id = known_face_ids[best_match_index]
            face_ids.append(known_id)

    results = {}
    results['data'] = face_ids
    return jsonify(results)


if __name__ == '__main__':
    app.run(threaded=True, port=80)
