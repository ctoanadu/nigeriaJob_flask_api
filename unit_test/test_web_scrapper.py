from web_scrapper import get_records, get_info, getAllData, create_dict
import pytest

from bs4 import BeautifulSoup
from collections import defaultdict

@pytest.fixture
def records():
    record=BeautifulSoup('''<div class="col-lg-5 col-job-title">
                            <h5><a href="link">Industrial</a></h5>
                            <p class="job-recruiter">19.04.2023 | <b><a class="company-name" href="/recruiter/127005">Comapny</a></b></p>
                            <div class="search-description">Job Title: Industrial Training InternshipLocation: Palmgroove </div>
                            <p>Region of : Lagos</p>
                            <!-- new tags position -->
                            </div>''', 'html.parser')
    return record


def test_get_records():
    rec = get_records()
    assert len(rec) > 0

def test_get_info(records):
    assert len(get_info(records))==7 

def test_getAllData(records):
    output=getAllData()
    assert len(output)>=len(records)

def test_create_dict():
    dict_output = create_dict()
    assert isinstance(dict_output, defaultdict)
    assert all([key in dict_output for key in ['url_link', 'job_title', 'company_name', 'job_description',\
                                                 'location', 'date_posted', 'technologies']])


