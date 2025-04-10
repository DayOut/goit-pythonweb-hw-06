from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from goit_pythonweb_hw_06.models import Student, Grade, Subject, Teacher, Group
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(Student.name, func.avg(Grade.grade).label('avg')).\
        join(Grade).group_by(Student.id).order_by(desc('avg')).limit(5).all()

def select_2(subject_id):
    return session.query(Student.name, func.avg(Grade.grade).label('avg')).\
        join(Grade).filter(Grade.subject_id == subject_id).\
        group_by(Student.id).order_by(desc('avg')).limit(1).first()

def select_3(subject_id):
    return (
        session.query(Group.name, func.avg(Grade.grade).label('avg'))
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )


def select_4():
    return (
        session.query(func.avg(Grade.grade))
        .scalar()
    )


def select_5(teacher_id):
    return (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )


def select_6(group_id):
    return (
        session.query(Student.name)
        .filter(Student.group_id == group_id)
        .all()
    )


def select_7(group_id, subject_id):
    return (
        session.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )


def select_8(teacher_id):
    return (
        session.query(func.avg(Grade.grade))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


def select_9(student_id):
    return (
        session.query(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )


def select_10(student_id, teacher_id):
    return (
        session.query(Subject.name)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
        .all()
    )

if __name__ == "__main__":
    print("-----------------------------------------------------")
    print("1. Top 5 students by avg grade:")
    for row in select_1():
        print(row)

    print("-----------------------------------------------------")
    print("2. Student with highest grade at subject with id 2:")
    print(select_2(2))

    print("-----------------------------------------------------")
    print("3. Average per group for subject 1:")
    print(select_3(1))

    print("-----------------------------------------------------")
    print("4. Average grade for thread:")
    print(select_4())

    print("-----------------------------------------------------")
    print("5. Courses by teacher 2:")
    print(select_5(2))

    print("-----------------------------------------------------")
    print("6. Students in group 2:")
    for row in select_6(2):
        print(row)

    print("-----------------------------------------------------")
    print('7. Grades in group 2 at subject 1:')
    for row in select_7(2, 1):
        print(row)

    print("-----------------------------------------------------")
    print('8. Average grade for teacher 1:')
    print(select_8(2))

    print("-----------------------------------------------------")
    print('9. Student 1 subjects:')
    for row in select_9(2):
        print(row)

    print("-----------------------------------------------------")
    print("10. Subjects for student 3 taught by teacher 1:")
    print(select_10(3, 1))