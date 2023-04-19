import requests
import lxml
import http3
import json 
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd 


headers={'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}


def get_records():

    #first Page scrape
    url='https://www.nigeriajob.com/job-vacancies-search-nigeria/?f%5B0%5D=im_field_offre_metiers%3A31'
    response=requests.get(url, headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    outer_point=soup.find_all('div','col-lg-5 col-md-5 col-sm-5 col-xs-12 job-title')
    #Second Scrape scrape
    url=url+'&page=1'
    response=requests.get(url, headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')

    #Aggregate total extract
    outer_point_2=soup.find_all('div','col-lg-5 col-md-5 col-sm-5 col-xs-12 job-title')
    outer_point.extend(outer_point_2)
    return outer_point

records=get_records()
record=records[0]
inside=record.h5.a
#card_one=outer_point[0]
#inside=card_one.h5.a

def get_info(record):
    inside=record.h5.a
    #url
    try:
        href=inside.get('href')
        link='https://www.nigeriajob.com'
        url_link=link+href
    except AttributeError:
        url_link=''
    url_link
   
    #job
    try:
        job_title=inside.text
    except AttributeError:
        job_title=''
    job_title

    #company
    try:
        company_name=record.p.b.text
    except AttributeError:
        company_name=''
    company_name
    
    #job_description
    try:
        job_description=record.div.text
    except AttributeError:
        job_description=''
    job_description
    
    #location
    try:
        location=record.find_all('p'[-1])
        location=location.text
        location=list(filter(lambda x:x !='-',x))
    except AttributeError:
        location=''
    location

    #date_posted
    try:
        date_posted=record.find_all('p')[0].text
        date_posted=date_posted.split()[0]
        date_posted=datetime.strptime(date_posted,'%d.%m.%Y').date()
    except AttributeError:
        date_posted=''
    date_posted
    
    #technology
    try:
        technology=record.find_all('div','job-tags').text
        technology=tech.split()
        technology=technology[3:]
    except AttributeError:
        technology=''
    technology
    data=[url_link,job_title,company_name,job_description,location,date_posted,technology]
    return data


def get_url(inside):
    try:
        href=inside.get('href')
        link='https://www.nigeriajob.com'
        url_link=link+href
    except AttributeError:
        url_link=''
    return url_link
    

def get_title(inside):
    try:
        job_title=inside.text
    except AttributeError:
        job_title=''
    return job_title

def get_company(record):
    try:
        company_name=record.p.b.text
    except AttributeError:
        company_name=''
    return company_name

def get_description(record):
    try:
        job_description=record.div.text
    except AttributeError:
        job_description=''
    return job_description

def get_location(record):
    try:
        location=record.find_all('p'[-1])
        location=location.text
        location=list(filter(lambda x:x !='-',x))
    except AttributeError:
        location=''
    return location

def get_date(record):
    try:
        date_posted=record.find_all('p')[0].text
        date_posted=date_posted.split()[0]
        date_posted=datetime.strptime(date_posted,'%d.%m.%Y').date()
    except AttributeError:
        date_posted=''
    return date_posted
        
def get_tech(record):
    try:
        tech=record.find_all('div','job-tags').text
        tech=tech.split()
        tech=tech[3:]
    except AttributeError:
        tech=''
    return tech



dt=[get_url(inside),\
    get_title(inside),\
    get_company(record),\
    get_description(record),\
    get_location(record),\
    get_date(record),get_tech(record)]

def get_all_columns(dt):
    return dt


#get_info(card_one)
def getAllData():
    data=[]
    for i in records:
        record=get_all_columns(i)
        data.append(record)
    return data

from collections import defaultdict

spec=['url_li','job_title','company_name','location','technologies','date_posted','job_description']
spec_dic_list=defaultdict(list)

all_post=getAllData()
for i in range(len(all_post)):
    p=(list(zip(spec,all_post[i])))

    for j in p:
        spec_dic_list[j[0]].append(j[1])
spec_dic_list



def main():  
    df = pd.DataFrame(get_all_columns())
    print(len(df))

if __name__=="__main__":
    main()
    



