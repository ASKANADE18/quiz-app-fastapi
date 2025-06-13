from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ADD THIS NEW ENDPOINT - Get all questions
@router.get("/quiz/", response_model=List[schemas.QuizQuestionResponse])
def get_all_questions(db: Session = Depends(get_db)):
    questions = db.query(models.QuizQuestion).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found")
    return questions

# Your existing endpoints
@router.post("/quiz/")
def create_quiz(q: schemas.QuizQuestionCreate, db: Session = Depends(get_db)):
    new_q = models.QuizQuestion(**q.dict())
    db.add(new_q)
    db.commit()
    db.refresh(new_q)
    return new_q

@router.post("/quiz/bulk")
def create_multiple_quizzes(request: schemas.QuizQuestionsCreate, db: Session = Depends(get_db)):
    added_questions = []
    for q in request.questions:
        new_q = models.QuizQuestion(**q.dict())
        db.add(new_q)
        db.commit()
        db.refresh(new_q)
        added_questions.append(new_q)
    return added_questions

@router.post("/quiz/submit")
def submit_quiz(submission: schemas.QuizSubmission, db: Session = Depends(get_db)):
    score = 0
    for answer in submission.answers:
        question = db.query(models.QuizQuestion).filter(models.QuizQuestion.id == answer.question_id).first()
        if question and question.correct_option == answer.selected_option:
            score += 1
    return {"score": score, "total": len(submission.answers)}

@router.post("/quiz/reset")
def reset_quiz(db: Session = Depends(get_db)):
    db.query(models.QuizQuestion).delete()
    db.commit()
    return {"message": "All quiz questions deleted."}
