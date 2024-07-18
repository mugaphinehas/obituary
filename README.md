### Report on Creating the Obituary Management Website using Flask and MySQL

#### Project Overview

The goal of this project was to create a web application for managing and displaying obituaries, with features optimized for SEO and social media engagement. The application was built using Flask for the backend, MySQL for the database, and basic HTML/CSS for the frontend.

#### Timeline

**Total Duration: 12 hours**

1. **Hour 1-2: Environment Setup**
2. **Hour 3-4: Database Creation**
3. **Hour 5-6: HTML Form Creation**
4. **Hour 7-8: Backend Script for Data Submission**
5. **Hour 9: Backend Script for Data Retrieval**
6. **Hour 10-11: SEO and Social Media Optimization**
7. **Hour 12: Testing and Validation**

### Steps Taken

#### Task 1: Environment Setup

1. Set up the development environment with Flask and MySQL.
2. Created a virtual environment and installed Flask and Flask-MySQLdb.
3. Ensured the MySQL service was running.

**Code Snippet:**
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install flask flask-mysqldb
```

#### Task 2: Database Creation

Created a MySQL database named `obituary_platform` and a table named `obituaries` with the specified columns.

**SQL Script:**
```sql
CREATE DATABASE obituary_platform;
USE obituary_platform;
CREATE TABLE obituaries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    date_of_birth DATE,
    date_of_death DATE,
    content TEXT,
    author VARCHAR(100),
    submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    slug VARCHAR(255) UNIQUE
);
```

#### Task 3: HTML Form Creation

Developed an HTML form for submitting obituaries with fields for name, date of birth, date of death, content, and author.

**HTML Form (`templates/index.html`):**

    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="date_of_birth">Date of Birth:</label>
        <input type="date" id="date_of_birth" name="date_of_birth" required><br>
        <label for="date_of_death">Date of Death:</label>
        <input type="date" id="date_of_death" name="date_of_death" required><br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea><br>
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" required><br>
         <label for="author">slug:</label>
        <input type="text" id="author" name="slug" required><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### Task 4: Backend Script for Data Submission

Implemented a Flask route to handle form submission and store the data in the MySQL database.

**Flask Route for Data Submission (`app.py`):**
```python
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "obituary_platform"

mysql = MySQL(app)

@app.route('/form', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        content = request.form['content']
        author = request.form['author']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author) VALUES (%s, %s, %s, %s, %s)",
                    (name, date_of_birth, date_of_death, content, author))
        mysql.connection.commit()
        cur.close()

        return "Obituary submitted successfully!"

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

#### Task 5: Backend Script for Data Retrieval

Implemented a Flask route to retrieve and display the stored obituaries.

**Flask Route for Data Retrieval (`app.py`):**
```python
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM obituaries")
    userDetails = cur.fetchall()
    cur.close()

    return render_template('users.html', userDetails=userDetails)
```

**HTML Template for Display (`templates/users.html`):**
```html

```

#### Task 6: SEO and Social Media Optimization

1. Added meta tags dynamically based on the obituary content.
2. Used semantic HTML tags and structured data for improved search engine visibility.
3. Implemented Open Graph tags for better social media sharing previews.

**Example Meta Tags:**
```html
<meta name="description" content="Obituary for {{ user[1] }}">
<meta property="og:title" content="Obituary for {{ user[1] }}">
<meta property="og:description" content="{{ user[4] }}">
<meta property="og:type" content="article">
```

#### Task 7: Testing and Validation

1. Tested the HTML form by submitting sample obituaries.
2. Verified the data insertion and retrieval from the MySQL database.
3. Ensured cross-browser compatibility.

### Conclusion

The obituary management platform was successfully created using Flask and MySQL. The platform allows users to submit and view obituaries with features for SEO and social media optimization. The project followed a structured timeline and achieved all the specified tasks.

### Key Features

1. **User-Friendly Form:** A simple HTML form for submitting obituaries.
2. **Database Integration:** Securely storing obituary data in a MySQL database.
3. **SEO Optimization:** Enhanced visibility through meta tags and structured data.
4. **Social Media Integration:** Open Graph tags for better social media previews.
5. **Cross-Browser Compatibility:** Ensured functionality across different web browsers.
