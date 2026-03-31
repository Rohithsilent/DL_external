import mysql.connector

# =============================
# 1. CONNECT TO MYSQL DB
# =============================
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = db.cursor()
print("Connected to MySQL Database!")

# =============================
# 2. CREATE TABLE (DDL)
# =============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")
print("Table checked/created.")


# =============================
# 3. CREATE (INSERT DATA)
# =============================
def create_student(name, age):
    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(sql, values)
    db.commit()
    print("Student Added!")


# =============================
# 4. READ (FETCH DATA)
# =============================
def read_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("Student Records:")
    for row in result:
        print(row)


# =============================
# 5. UPDATE (MODIFY DATA)
# =============================
def update_student(student_id, new_age):
    sql = "UPDATE students SET age=%s WHERE id=%s"
    values = (new_age, student_id)
    cursor.execute(sql, values)
    db.commit()
    print("Student Updated!")


# =============================
# 6. DELETE (REMOVE DATA)
# =============================
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id=%s"
    values = (student_id,)
    cursor.execute(sql, values)
    db.commit()
    print("Student Deleted!")


# =============================
# TEST CRUD FUNCTIONS
# =============================

create_student("Rohith", 21)
create_student("Kiran", 22)

read_students()

update_student(1, 25)

delete_student(2)

read_students()

# =============================
# CLOSE CONNECTION
# =============================
db.close()
