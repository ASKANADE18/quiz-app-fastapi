from pydantic import BaseModel
from typing import List

class QuizQuestionCreate(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str

# ADD THIS NEW SCHEMA - For API responses
class QuizQuestionResponse(BaseModel):
    id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    # Note: We don't include correct_option in response for security
    
    class Config:
        from_attributes = True

class QuizQuestionsCreate(BaseModel):
    questions: List[QuizQuestionCreate]

class QuizAnswer(BaseModel):
    question_id: int
    selected_option: str

class QuizSubmission(BaseModel):
    answers: List[QuizAnswer]
    