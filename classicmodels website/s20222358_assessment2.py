from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import pymysql
from flask_cors import CORS
import os
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)

auth = HTTPBasicAuth()
@auth.verify_password
def authenticate(username, password):
    if username=='GBCA' and password == 'abc!!':
        return True
    else: 
        return False

# Open database connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
# how to set env: export xxx=123 then os.environ.get(xxx)
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get("MYSQL_DATABASE_PASSWORD")
app.config['MYSQL_DATABASE_DB'] = 'career_training'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



#function to respone
def format_response (message, status_code):
    response=jsonify(message)
    response.status_code=status_code
    return response

@app.route('/employees')
def get_all_employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT employeeNumber, email, lastName,firstName,jobTitle FROM classicmodels.employees")
        rows = cursor.fetchall()
        return format_response(rows, 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

@app.route('/employees/<int:employeeNum>')
def get_employee_byID(employeeNum):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        affected_row=cursor.execute(f"SELECT employeeNumber, email, lastName,firstName,jobTitle FROM classicmodels.employees WHERE employeeNumber={employeeNum}")
        if affected_row==1:
            rows = cursor.fetchone()
            return format_response(rows, 200)
        else:
            return format_response("Employee not found", 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)


@app.route('/employees/<int:employeeNum>', methods =["DELETE"])
@auth.login_required
def delete_employee(employeeNum):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        affected_row=cursor.execute(f'DELETE FROM classicmodels.employees WHERE employeeNumber={employeeNum}')
        conn.commit()
        if affected_row ==1 :
            return format_response("Deleted successfully",200)
        else:
            return format_response("Can't find the student",200)

    except pymysql.Error as e:
        return format_response(e.args[1],400)




@app.route('/employees', methods =["POST"])
@auth.login_required
def add_employee():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        new_employee = request.json
        affected_row=cursor.execute(f'INSERT INTO classicmodels.employees (lastName,firstName,email,jobTitle) VALUES ("{new_employee["lastName"]}","{new_employee["firstName"]}","{new_employee["email"]}","{new_employee["jobTitle"]}")')
        conn.commit()
        if affected_row ==1 :
            return format_response("Added successfully",200)
        else:
            return format_response("Can't add the employee",404)

    except pymysql.Error as e:
        return format_response(e.args[1],400)



# when add auth , redirection will fall
@app.route('/employees', methods =["PUT"])
@auth.login_required
def update_employee():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        new_employee = request.json
        affected_row=cursor.execute(f'UPDATE classicmodels.employees SET lastName="{new_employee["lastName"]}",firstName="{new_employee["firstName"]}",email="{new_employee["email"]}",jobTitle="{new_employee["jobTitle"]}" WHERE employeeNumber={new_employee["employeeNumber"]}')
        conn.commit()
        if affected_row ==1 :
            return format_response("updated successfully",200)
        else:
            return format_response("Employee didn't update",404)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

@app.route('/chart1')
def get_chart1():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select country as xValues, count(*) as yValues from classicmodels.customers group by country order by yValues desc limit 5")
        rows = cursor.fetchall()
        xValues_list=[]
        yValues_list=[]
        for row in rows:
            xValues_list.append(row["xValues"])
            yValues_list.append(row["yValues"])
        chart={
            "xValues":xValues_list,
            "yValues":yValues_list
        }
        return format_response(chart, 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

@app.route('/chart2/<int:year>')
def get_chart2(year):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(f"select month(orderDate) as xValues,count(*) as yValues from classicmodels.orders where year(orderDate)={year} group by month(orderDate)")
        rows = cursor.fetchall()
        xValues_list=[]
        yValues_list=[]
        for row in rows:
            xValues_list.append(row["xValues"])
            yValues_list.append(row["yValues"])
        chart={
            "Year": year,
            "xValues":xValues_list,
            "yValues":yValues_list
        }
        return format_response(chart, 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

@app.route('/chart3')
def get_chart3():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select count(*) as yValues, productLine as xValues from classicmodels.products group by productLine")
        rows = cursor.fetchall()
        xValues_list=[]
        yValues_list=[]
        for row in rows:
            xValues_list.append(row["xValues"])
            yValues_list.append(row["yValues"])
        chart={
            "xValues":xValues_list,
            "yValues":yValues_list
        }
        return format_response(chart, 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

@app.route('/chart4')
def get_chart4():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select year(orderDate) as xValues,count(*) as yValues from classicmodels.orders group by year(orderDate)")
        rows = cursor.fetchall()
        xValues_list=[]
        yValues_list=[]
        for row in rows:
            xValues_list.append(row["xValues"])
            yValues_list.append(row["yValues"])
        chart={
            "xValues":xValues_list,
            "yValues":yValues_list
        }
        return format_response(chart, 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

@app.route('/total_employees')
def get_total_employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT count(*) as totalemployees FROM classicmodels.employees")
        rows = cursor.fetchone()
        return format_response(rows, 200)
    except pymysql.Error as e:
        return format_response(e.args[1],400)

app.run(host='localhost', port=3001)