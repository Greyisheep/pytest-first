import pytest
from unittest.mock import MagicMock
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def sample_classroom():
    teacher = Teacher("John Doe")
    students = [Student("Alice"), Student("Bob"), Student("Charlie")]
    course_title = "Mathematics"
    classroom = Classroom(teacher, students, course_title)
    return classroom

def test_add_student(sample_classroom):
    # Ensure that a student can be added to the classroom
    new_student = Student("David")
    sample_classroom.add_student(new_student)
    assert new_student in sample_classroom.students

    # Ensure that TooManyStudents exception is raised when trying to add more than 10 students
    with pytest.raises(TooManyStudents):
        for i in range(11):
            sample_classroom.add_student(Student(f"Student_{i}"))

def test_remove_student(sample_classroom):
    # Ensure that a student can be removed from the classroom
    student_to_remove = sample_classroom.students[0]
    sample_classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in sample_classroom.students

def test_change_teacher(sample_classroom):
    # Ensure that the teacher can be changed
    new_teacher = Teacher("Jane Doe")
    sample_classroom.change_teacher(new_teacher)
    assert sample_classroom.teacher == new_teacher

def test_change_teacher_with_mock(sample_classroom):
    # Ensure that the change_teacher method uses the new teacher
    new_teacher = Teacher("Jane Doe")
    sample_classroom.change_teacher = MagicMock()
    sample_classroom.change_teacher(new_teacher)
    sample_classroom.change_teacher.assert_called_once_with(new_teacher)
