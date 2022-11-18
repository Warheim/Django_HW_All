import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_one_course(client, course_factory):
    one_course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(one_course)
    assert data[0]['id'] == one_course[0].id
    assert data[0]['name'] == one_course[0].name


@pytest.mark.django_db
def test_some_courses(client, course_factory):
    some_courses = course_factory(_quantity=5)
    print(some_courses)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert len(data) == len(some_courses)
    for num, course in enumerate(data):
        assert course['id'] == some_courses[num].id
        assert course['name'] == some_courses[num].name

