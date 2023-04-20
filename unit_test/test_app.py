import json
import pytest

from app import app, db, Job


@pytest.fixture(scope='module')
def new_job():
    job = Job(
        url_link='http://naijajob.com',
        job_title='Software Engineer',
        company_name='Beekin',
        job_description='2 years pythin experience',
        date_posted='2022-01-01',
        technology='Python',
        location_name='Lagos'
    )
    return job


def test_filter_jobs_with_location(new_job):
    with app.test_client() as client:
        response = client.get('/jobs/filter?location_name=Lagos')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
       


def test_filter_jobs_with_technology(new_job):
    with app.test_client() as client:
        response = client.get('/jobs/filter?technology=Python')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
        


def test_sort_jobs_by_job_title(new_job):
    with app.test_client() as client:
        response = client.get('/jobs/sort?sort_by=job_title')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
        


def test_pagination(new_job):
    with app.test_client() as client:
        response = client.get('/jobs/paginate?page=1')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
        assert data['page'] == 1
        assert data['per_page'] == 10
        
       
