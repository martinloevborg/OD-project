from flask import Flask, request, Response
import json
import mysql.connector
app = Flask(__name__)

@app.route('/person', methods=['POST'])
def person():
    connect = mysql.connector.connect(
            host = "database",
            user = "user",
            password = "password",
            database = "pDatabase"
    )
    curso = connect.cursor() #get_db()
    #curso.execute("INSERT INTO persontb (Firstname, Lastname) VALUES ('{}','{}');", (request.form['firstname'], request.form['lastname']))
    curso.execute("INSERT INTO persontb (Firstname, Lastname) VALUES ('{}','{}');".format(request.form['firstname'], request.form['lastname']))
    #curso.execute("INSERT INTO persontb (Firstname, Lastname) VALUES (%s,%s);", (request.form['firstname'], request.form['lastname']))
    connect.commit() #close()
    #return '200'
    return Response(status=200)
    #return "succes"

@app.route('/persons', methods=['GET'])
def persons():
    connect = mysql.connector.connect(
            host = "database",
            port = 3306, #
            user = "user",
            password = "password",
            database = "pDatabase"
    )
    dict = []
    curso = connect.cursor()
    curso.execute("SELECT * from persontb")     
    list = curso.fetchall()
    for i in list:
        dict.append({"Firstname":i[1],"PersonID":i[0],"Lastname":i[2]})
    return json.dumps(dict)

#Initialiserer det
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)