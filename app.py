from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_parameter


app=Flask(__name__)

#Innitiating connection to the app to connect to PostgresQl
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://user_new:Password1@localhost:5432/beekin_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False




db=SQLAlchemy(app)

class Job(db.Model):
    __tablename__='beekin_job'

    id=db.Column(db.Integer,primary_key=True)
    url_link=db.Column(db.String(255), nullable=False)
    job_title=db.Column(db.String(255), nullable=False)
    company_name=db.Column(db.String(255), nullable=False)
    job_description=db.Column(db.String(255), nullable=False)
    date_posted=db.Column(db.DateTime(255), nullable=False)
    technology=db.Column(db.String(255), nullable=False)
    location_name=db.Column(db.String(255), nullable=False)

    def __init__(self,url_link,job_title,company_name,job_description,date_posted,technology, location_name) -> None:
        self.url_link=url_link
        self.job_title=job_title
        self.company_name=company_name
        self.job_description=job_description
        self.date_posted=date_posted
        self.technology=technology
        self.location_name=location_name

    def to_dict(self):
        return {
            'id': self.id,
            'url_link': self.url_link,
            'job_title': self.job_title,
            'company_name': self.company_name,
            'job_description': self.job_description,
            'date_posted': self.date_posted.strftime('%Y-%m-%d %H:%M:%S'), # convert datetime to string format
            'technology': self.technology,
            'location_name': self.location_name
        }
        

@app.route('/jobs/filter', methods=['GET'])
def filter_jobs():
    """Get method that filters job query by technology and location"""
    location = request.args.get('location')
    technology=request.args.get('technology')

    if not location and not technology:
        print('no input was provided')

    query=Job.query

    if location:
        query=query.filter(Job.location_name.ilike(f'%{location}%'))

    if technology:
        query=query.filter(Job.technology.ilike(f'%{technology}%'))

    jobs=query.all()
    results=[job.to_dict() for job in jobs]
    data={'data':results}
    return jsonify(data)
    

@app.route('/jobs/sort', methods=['GET'])
def sort_jobs():
    """Get method to sorts"""
    sort_by =request.args.get('sort_by')

    query=Job.query.order_by(sort_by)
    jobs=query.all()
    results=[job.to_dict() for job in jobs]
    data={'data':results}
    return jsonify(data)

@app.route('/jobs/paginate', methods=['GET'])
def paginator():
    """Get method to provide pagination to the app"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per-page', 1, type=int)

    query=Job.query
    jobs=query.paginate(page,per_page,error_out=False)

    results=[job.to_dict() for job in jobs.items]
    data={
        'data':results,
        'page':page,
        'per_page':per_page
    }

    return jsonify (data)

 

if __name__=='__main__':
    app.run(debug=True)





