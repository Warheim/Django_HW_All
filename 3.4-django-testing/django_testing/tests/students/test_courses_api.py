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
    assert data[0]['id'] == 1


@pytest.mark.django_db
def test_len_list(client, course_factory):
    some_courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5


@pytest.mark.django_db
def test_course_filter(client, course_factory):
    some_courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert len(data) == 1

