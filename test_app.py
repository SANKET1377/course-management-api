from fastapi.testclient import TestClient
from pymongo import MongoClient
from bson import ObjectId
import pytest
from main import app

client = TestClient(app)
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['courses']

# 🔥 Your real course ID
COURSE_ID = "6994985c29bff359117dbda3"


def test_get_courses_no_params():
    response = client.get("/courses")
    assert response.status_code == 200


def test_get_courses_sort_by_alphabetical():
    response = client.get("/courses?sort_by=alphabetical")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert sorted(courses, key=lambda x: x['name']) == courses


def test_get_courses_sort_by_date():
    response = client.get("/courses?sort_by=date")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert sorted(courses, key=lambda x: x['date'], reverse=True) == courses


def test_get_courses_sort_by_rating():
    response = client.get("/courses?sort_by=rating")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert sorted(courses, key=lambda x: x['rating']['total'], reverse=True) == courses


def test_get_courses_filter_by_domain():
    response = client.get("/courses?domain=mathematics")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert all([c['domain'][0] == 'mathematics' for c in courses])


def test_get_courses_filter_by_domain_and_sort_by_alphabetical():
    response = client.get("/courses?domain=mathematics&sort_by=alphabetical")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert all([c['domain'][0] == 'mathematics' for c in courses])
    assert sorted(courses, key=lambda x: x['name']) == courses


def test_get_courses_filter_by_domain_and_sort_by_date():
    response = client.get("/courses?domain=mathematics&sort_by=date")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert all([c['domain'][0] == 'mathematics' for c in courses])
    assert sorted(courses, key=lambda x: x['date'], reverse=True) == courses


def test_get_course_by_id_exists():
    response = client.get(f"/courses/{COURSE_ID}")
    assert response.status_code == 200
    course = response.json()

    # Get the course from database using real ID
    course_db = db.courses.find_one({'_id': ObjectId(COURSE_ID)})
    name_db = course_db['name']
    name_response = course['name']

    assert name_db == name_response


def test_get_course_by_id_not_exists():
    response = client.get("/courses/000000000000000000000000")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Course not found'}


def test_get_chapter_info():
    response = client.get(f"/courses/{COURSE_ID}/1")
    assert response.status_code == 200
    chapter = response.json()
    assert "name" in chapter
    assert "text" in chapter


def test_get_chapter_info_not_exists():
    response = client.get(f"/courses/{COURSE_ID}/990")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Chapter not found'}


def test_rate_chapter():
    chapter_id = "1"
    rating = 1

    response = client.post(f"/courses/{COURSE_ID}/{chapter_id}?rating={rating}")

    assert response.status_code == 200

    assert "name" in response.json()
    assert "rating" in response.json()
    assert "total" in response.json()["rating"]
    assert "count" in response.json()["rating"]

    assert response.json()["rating"]["count"] > 0


def test_rate_chapter_not_exists():
    response = client.post(f"/courses/{COURSE_ID}/990?rating=1")
    assert response.status_code == 404
