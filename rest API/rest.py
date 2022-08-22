import requests
from flask import Flask, jsonify, request


students = [
{"student_name":"Donna Snider","mobile":"041234560","studentid":1000},
{"student_name":"Michael Bruce","mobile":"041233360","studentid":1001},
{"student_name":"onas Alexander","mobile":"041444560","studentid":1002},
{"student_name":"Lael Greer","mobile":"041234551","studentid":1003},
{"student_name":"Hermione Butler","mobile":"0435431132","studentid":1004}
]

app = Flask(__name__)

@app.route('/student/')
def get_students():
    if request.args.get("sid"):
        for student in students:
            if student["studentid"] == int(request.args.get("sid")):
                response = jsonify(student)
                response.status_code =200
                return response
        response = jsonify("Student not found...")
        response.status_code =404
        return response
    else :
        response = jsonify(students)
        response.status_code =200
        return response


@app.route('/student/', methods = ["DELETE"])
def delete_student_by_id():
    for student in students:
        if student["studentid"] == int(request.args.get("sid")):
            students.remove(student)
            response = jsonify("Student removed successfully")
            response.status_code =200
            return response
    response = jsonify("Student not found...")
    response.status_code =404
    return response

@app.route('/student/', methods = ["POST", "PUT"])
def update_student_by_id():
    new_student = request.json
    for student in students:
        if student["studentid"] == new_student["studentid"]:
            students[students.index(student)]=new_student
            response = jsonify("Student updated successfully")
            response.status_code =200
            return response
    else:
        students.append(new_student)
        response = jsonify("New student added")
        response.status_code =200
        return response


if __name__ == '__main__':
  app.run(host='localhost', port=3001)

