import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from goit_pythonweb_hw_06.models import Base, Student, Group, Teacher, Subject, Grade
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

fake = Faker()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Кількість записів для генерації
NUM_GROUPS = 3
NUM_TEACHERS = 5
NUM_SUBJECTS = 8
NUM_STUDENTS = 50
MAX_GRADES_PER_STUDENT = 20


def seed_data():
    try:
        # Очистка існуючих даних
        if session.query(Grade).count() > 0:
            session.query(Grade).delete()
        if session.query(Student).count() > 0:
            session.query(Student).delete()
        if session.query(Subject).count() > 0:
            session.query(Subject).delete()
        if session.query(Teacher).count() > 0:
            session.query(Teacher).delete()
        if session.query(Group).count() > 0:
            session.query(Group).delete()
        session.commit()

        # Створення груп
        groups = []
        for i in range(NUM_GROUPS):
            group_name = f"Group {i+1}"
            groups.append(Group(name=group_name))

        session.add_all(groups)
        session.commit()

        # Логування успішного додавання груп
        print(f"Групи: {', '.join([group.name for group in groups])} успішно додано!")

        # Створення викладачів
        teachers = [Teacher(name=fake.name()) for _ in range(NUM_TEACHERS)]
        session.add_all(teachers)
        session.commit()

        # Логування успішного додавання викладачів
        print(f"Викладачі: {', '.join([teacher.name for teacher in teachers])} успішно додано!")

        # Створення предметів
        subjects = [
            Subject(name=fake.word().capitalize(), teacher=random.choice(teachers))
            for _ in range(NUM_SUBJECTS)
        ]
        session.add_all(subjects)
        session.commit()

        # Логування успішного додавання предметів
        print(f"Предмети: {', '.join([subject.name for subject in subjects])} успішно додано!")

        # Створення студентів
        students = [
            Student(name=fake.name(), group=random.choice(groups))
            for _ in range(NUM_STUDENTS)
        ]
        session.add_all(students)
        session.commit()

        # Логування успішного додавання студентів
        print(f"Студенти:")
        pprint([student.name for student in students])

        # Створення оцінок
        grades = []
        for student in students:
            for _ in range(random.randint(1, MAX_GRADES_PER_STUDENT)):
                grade = Grade(
                    student=student,
                    subject=random.choice(subjects),
                    grade=random.uniform(1.0, 5.0),
                    date_received=fake.date_between(start_date="-2y", end_date="today"),
                )
                grades.append(grade)

        session.add_all(grades)
        session.commit()

        # Логування успішного додавання оцінок
        print("Оцінки для студентів успішно додано!")

        print("Дані успішно додано до бази даних!")
    except Exception as e:
        session.rollback()
        print(f"Помилка при заповненні бази даних: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()