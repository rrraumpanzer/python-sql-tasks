from models import Course, Lesson
from solution import save_course, find_course, save_lesson, find_lesson, get_course_lessons


def test_solution(db_transaction):
    course = Course('test_course', 'test_description')
    course_id = save_course(db_transaction, course)
    found_course = find_course(db_transaction, course_id)

    assert found_course.name == course.name

    lesson1 = Lesson('test_lesson_1', 'test_text_1', course_id)
    lesson2 = Lesson('test_lesson_2', 'test_text_2', course_id)

    save_lesson(db_transaction, lesson1)
    lesson2_id = save_lesson(db_transaction, lesson2)

    found_lesson_2 = find_lesson(db_transaction, lesson2_id)
    assert found_lesson_2.name == lesson2.name

    all_lessons = get_course_lessons(db_transaction, course_id)
    assert all_lessons == [lesson1, lesson2]
