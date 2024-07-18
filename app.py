from flask import Flask, render_template, request
from flask_mysqldb import MySQL

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "obituary_platform"

mysql = MySQL(app)




@app.route('/')
def landing_page():
    return render_template('landing_page.html')




@app.route('/form', methods=[ 'GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        content = request.form['content']
        author = request.form['author']
        slug = request.form['slug']

        # Get connection and cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author,slug) VALUES (%s, %s, %s, %s, %s,%s)",
                    (name, date_of_birth, date_of_death, content, author,slug))

        # Commit to database
        mysql.connection.commit()

        # Close cursor
        cur.close()

        return "Well done"

    return render_template('index.html')

@app.route('/users')
def users():
    # Get connection and cursor
    cur = mysql.connection.cursor()

    # Execute query
    cur.execute("SELECT * FROM obituaries")

    # Fetch all records
    userDetails = cur.fetchall()

    # Close cursor
    cur.close()

    return render_template('users.html', userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)
