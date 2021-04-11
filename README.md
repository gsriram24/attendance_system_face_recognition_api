# Attendance System Face Recognition API

A sample Flask application which helps with the face recognition in the [Attendance System App](https://github.com/sgcuber24/attendance_system_app)  


## Getting Started

To get started, you'll want to first clone this GitHub repository locally:

```bash
$ git clone https://github.com/sgcuber24/attendance_system_face_recognition_api.git
```

Next, you'll want to go into the sample app directory:

```bash
$ cd attendance_system_face_recognition_api
```

Then you'll want to install all of the Python requirements (via
[pip](http://pip.readthedocs.org/en/latest/)):

```bash
$ pip install -r requirements.txt
```

And lastly, you'll want to run the `app.py` script which will guide you
the rest of the way:

```bash
$ python app.py
```

**Note**: Since this API is built for the [Attendance System App](https://github.com/sgcuber24/attendance_system_app), you will have to be authorized as a Teacher and must pass in a JWT (JSON Web Token) with your request. You can find the Attendance System Backend [here](https://github.com/Josh551/attendance-system-backend)


## Available end-points


### POST /

Takes in a File and class ID and returns the students present in the class after performing facial recognition and detection. 

**Headers**

Content-Type : form-data
Authorization : Bearer Token

**Request body**

| Key | Value |
| ------------- | ------------- |
| file  | unknown.jpg |
| classId  | 6049da1fc125133d04bdad6b |
