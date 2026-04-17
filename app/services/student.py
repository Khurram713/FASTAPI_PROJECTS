from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate


def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name = student.name,
        age = student.age,
        email = student.email,
        CNIC = student.CNIC
    )

    db.add(db_student) # add in meomory
    db.commit() # save in database
    db.refresh(db_student) # updated data (id) 
    return db_student

# for all sutdents 
def get_students(db: Session):
    return db.query(Student).all()

# for search student_id
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# for update student data
def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student = get_student(db, student_id)
    if not db_student:
        return None
    db_student.name = student.name
    db_student.age = student.age
    db_student.email = student.email
    db_student.CNIC = student.CNIC
    db.commit()
    db.refresh(db_student)
    return db_student

# fro delete student Id
def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if not db_student:
        return False
    db.delete(db_student)
    db.commit()
    return True
