from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.student import StudentCreate, StudentResponse
from app.services import student as student_service

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# for craate student
@router.post("/", response_model=StudentResponse)
def create(student: StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student(db, student)

# get list of students
@router.get("/", response_model=list[StudentResponse])
def read_all(db: Session = Depends(get_db)):
    return student_service.get_students(db)

# search student id
@router.get("/{student_id}", response_model=StudentResponse)
def read_one(student_id: int, db: Session = Depends(get_db)):
    db_student = student_service.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail= " Student not found")
    return db_student

@router.put("/{student_id}", response_model=StudentResponse)
def update(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    updated = student_service.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/{student_id}")
def delete(student_id: int, db:Session = Depends(get_db)):
    success = student_service.delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not fount")
    return {"message": "Student deleted successfully"}