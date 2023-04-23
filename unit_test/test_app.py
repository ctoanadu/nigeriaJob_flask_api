import json
import pytest

from app import app, db, Job


def test_filter_jobs_with_location():
    with app.test_client() as client:
        response = client.get('/jobs/filter?location_name=Lagos')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
       

def test_filter_jobs_with_technology():
    with app.test_client() as client:
        response = client.get('/jobs/filter?technology=Python')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
        

def test_sort_jobs_by_job_title():
    with app.test_client() as client:
        response = client.get('/jobs/sort?sort_by=job_title')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
        

def test_pagination():
    with app.test_client() as client:
        response = client.get('/jobs/paginate?page=1')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']) > 0
        
        
       
