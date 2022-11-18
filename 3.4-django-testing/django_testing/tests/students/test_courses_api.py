import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def address():
    return f'/api/v1/courses/'


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
def test_one_course(client, course_factory, address):
    one_course = course_factory(_quantity=1)

    response = client.get(address)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(one_course)
    assert data[0]['id'] == one_course[0].id
    assert data[0]['name'] == one_course[0].name


@pytest.mark.django_db
def test_some_courses(client, course_factory, address):
    some_courses = course_factory(_quantity=5)
    print(some_courses)

    response = client.get(address)

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert len(data) == len(some_courses)
    for num, course in enumerate(data):
        assert course['id'] == some_courses[num].id
        assert course['name'] == some_courses[num].name


@pytest.mark.django_db
def test_courses_id(client, course_factory, address):
    some_courses = course_factory(_quantity=5)
    for course in some_courses:
        response = client.get(address, {'id': str(course.id)})
        assert response.status_code == 200
        data = response.json()
        assert data[0]['id'] == course.id
        assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_courses_name(client, course_factory, address):
    some_courses = course_factory(_quantity=5)
    for course in some_courses:
        response = client.get(address, {'name': str(course.name)})
        assert response.status_code == 200
        data = response.json()
        assert data[0]['id'] == course.id
        assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_course_creation(client, address):
    course_name = 'Python'
    response = client.post(address, data={'name': course_name})

    assert response.status_code == 201
    data = response.json()
    assert course_name == data['name']


@pytest.mark.django_db
def test_course_update(client, course_factory, address):
    one_course = course_factory(_quantity=1)
    new_course_name = 'Python'

    response = client.patch(f'{address}{one_course[0].id}/', data={'name': new_course_name})

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == one_course[0].id
    assert data['name'] == new_course_name

