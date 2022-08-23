from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)

# Open database connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'career_training'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)

#function to respone
def format_response (message, status_code):
    response=jsonify(message)
    response.status_code=status_code
    return response

@app.route('/student/')
def get_all_students():
    try:
        if request.args.get("sid"):
            affected_row=cursor.execute(f'SELECT * FROM student WHERE studentID = {request.args.get("sid")}')
            if affected_row==1:
                rows = cursor.fetchall()
                return format_response(rows, 200)
            else:
                return format_response("Student not found", 200)
        else:
            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            return format_response(rows, 200)

    except pymysql.Error as e:
        return format_response(e.args[1],400)


@app.route('/student/', methods =["DELETE"])
def delete_student():
    try:
        affected_row=cursor.execute(f'DELETE FROM student WHERE studentID={request.args.get("sid")}')
        conn.commit()
        if affected_row ==1 :
            return format_response("Deleted successfully",200)
        else:
            return format_response("Can't find the student",200)

    except pymysql.Error as e:
        return format_response(e.args[1],400)




@app.route('/student/', methods =["POST"])
def add_student():
    try:
        new_student = request.json
        affected_row=cursor.execute(f'INSERT INTO student VALUES ({new_student["studentID"]},"{new_student["studentName"]}","{new_student["contact"]}","{new_student["courseCode"]}","{new_student["dateOfBirth"]}")')
        conn.commit()
        if affected_row ==1 :
            return format_response("Added successfully",200)
        else:
            return format_response("Student didn't add",404)

    except pymysql.Error as e:
        return format_response(e.args[1],400)




@app.route('/student/', methods =["PUT"])
def update_student():
    try:
        edit_student = request.json
        affected_row=cursor.execute(f'UPDATE student SET studentName="{edit_student["studentName"]}",contact="{edit_student["contact"]}",courseCode="{edit_student["courseCode"]}",dateOfBirth="{edit_student["dateOfBirth"]}" WHERE studentID={edit_student["studentID"]}')
        conn.commit()
        if affected_row ==1 :
            return format_response("updated successfully",200)
        else:
            return format_response("Student didn't update",404)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

app.run(host='localhost', port=3001)