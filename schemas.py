from pydantic import BaseModel
from typing import List

class QuizQuestionCreate(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str

class QuizQuestionsCreate(BaseModel):
    questions: List[QuizQuestionCreate]

class QuizAnswer(BaseModel):
    question_id: int
    selected_option: str

class QuizSubmission(BaseModel):
    answers: list[QuizAnswer]

