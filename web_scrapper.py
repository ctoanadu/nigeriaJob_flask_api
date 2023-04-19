import requests
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd 
from collections import defaultdict


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
    location=record.find_all('p')[-1].text.split()[3:]
    location=list(filter(lambda x:x!='-',location))
        
    #date_posted
    try:
        date_posted=record.find_all('p')[0].text
        date_posted=date_posted.split()[0]
        date_posted=datetime.strptime(date_posted,'%d.%m.%Y').date()
    except AttributeError:
        date_posted=''
    
    
    #technology
    technology=record.find_all('div','badge')
    
    
    dt=[url_link,job_title,company_name,job_description,location,date_posted,technology]
    return dt


#get_info(card_one)
def getAllData():
    data=[]
    for i in records:
        record=get_info(i)
        data.append(record)
    return data


def create_dict():
    spec=['url_link','job_title','company_name','job_description','location','date_posted','technologies']
    spec_dic_list=defaultdict(list)

    all_post=getAllData()
    for i in range(len(all_post)):
        p=(list(zip(spec,all_post[i])))
        for j in p:
            spec_dic_list[j[0]].append(j[1])
    return spec_dic_list




    



