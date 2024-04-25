from dataclasses import dataclass
from datetime import datetime
from typing import List, Union



@dataclass(frozen=True, slots=True)
class UserAnnotation:
    password: str
    first_name: str
    last_name: str
    email: str


@dataclass(frozen=True, slots=True)
class TeacherAnnotation:
    experience: int
    user: UserAnnotation


@dataclass(frozen=True, slots=True)
class StudentAnnotation:
    age: int
    rating: int
    user: UserAnnotation


@dataclass(frozen=True, slots=True)
class CourseAnnotation:
    name: str
    teacher: TeacherAnnotation
    price: int


@dataclass(frozen=True, slots=True)
class GroupAnnotation:
    group_name: str
    teacher: TeacherAnnotation
    student: List[StudentAnnotation]
    course: CourseAnnotation


@dataclass(frozen=True, slots=True)
class TopicAnnotation:
    name: str
    course: CourseAnnotation
    content: str


@dataclass(frozen=True, slots=True)

class MessageAnnotation:
    sender: UserAnnotation
    recipients: UserAnnotation
    topic: str
    text: str


@dataclass(frozen=True, slots=True)
class ArticleAnnotation:
    title: str
    teacher: TeacherAnnotation
    topic: TopicAnnotation
    content: str

@dataclass(frozen=True, slots=True)
class TestAnnotation:
    title: str
    topic: TopicAnnotation
    teacher: TeacherAnnotation
    description: str
    is_open: bool


@dataclass(frozen=True, slots=True)
class TestAccessAnnotation:
    test: TestAnnotation
    shared_with_teacher: TeacherAnnotation


@dataclass(frozen=True, slots=True)
class QuestionAnnotation:
    text: str
    test: TestAnnotation
    is_important: bool


@dataclass(frozen=True, slots=True)
class AnswerAnnotation:
    text: str
    question: QuestionAnnotation
    is_correct: bool


@dataclass(frozen=True, slots=True)
class AttemptAnnotation:
    test: TestAnnotation
    student: StudentAnnotation
    score: int



@dataclass(frozen=True, slots=True)
class ChatRoomAnnotation:
    name_chat: str
    description_topics: str
    participant: UserAnnotation


@dataclass(frozen=True, slots=True)
class ChatMessageAnnotation:
    chatroom: str
    text_message: str
    sending_time: datetime
    sender: Union[UserAnnotation, TeacherAnnotation, StudentAnnotation]
    recipient: Union[UserAnnotation, TeacherAnnotation, StudentAnnotation]


@dataclass(frozen=True, slots=True)
class RecommendationAnnotation:
    text: str
    student: StudentAnnotation
    test: TestAnnotation
    recommended_courses: CourseAnnotation
    recommended_articles: ArticleAnnotation
