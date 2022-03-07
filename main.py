from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Niladri'
app.config['MYSQL_PASSWORD'] = 'Niladri000'
app.config['MYSQL_DB'] = 'librery_app_flask'

mysql = MySQL(app)

app.config["DEBUG"] = True

@app.route("/", methods=['GET', 'POST'])
def create_students():
	if request.method == "POST":
		details = request.form
		StudentID = details['id']
		StudentName = details['name']
		StudentAddress = details['addess']
		BookID = details['bookid']
		cur = mysql.connection.cursor()
		if StudentID or StudentName or StudentAddress or BookID:
			query = f"""INSERT INTO student_details(student_id, student_name,student_address,book_id) VALUES ({StudentID},'{StudentName}','{StudentAddress}',{BookID})"""
			print(query)
			cur.execute(query)
			mysql.connection.commit()
			cur.close()
			return "Success !"
		else:
			return "Please enter all field !"

	return render_template("create.html")


@app.route("/display",methods=['GET'])
def display():
	if request.method == 'GET':
		cur = mysql.connection.cursor()
		query = """Select * from student_details"""
		cur.execute(query)
		records = cur.fetchall()
		cur.close()
		return render_template('display.html', records = records)

@app.route("/update", methods=['GET' ,'POST'])
def update():
	if request.method == "POST":
		details = request.form
		StudentID = details['id']
		StudentAddress = details['addess']
		StudentName = details['name']
		cur = mysql.connection.cursor()
		if StudentAddress:
			query = f"""update student_details set student_address = '{StudentAddress}' where student_id = {StudentID}"""
			cur.execute(query)
			mysql.connection.commit()
			return "Successfully Updated!"
		elif StudentName:
			query = f"""update student_details set student_name = '{StudentName}' where student_id = {StudentID}"""
			cur.execute(query)
			mysql.connection.commit()
			return "Successfully Updated!"
		cur.close()
	return render_template('update.html')

@app.route("/delete", methods=['GET' ,'POST'])
def delete():
	if request.method == "POST":
		details = request.form
		StudentID = details['id']
		cur = mysql.connection.cursor()
		if StudentID:
			query = f"""delete from student_details where student_id = {StudentID}"""
			cur.execute(query)
			mysql.connection.commit()
			cur.close()
			return "Successfully Deleted!"
	return render_template('delete.html')

app.run(port=80)

