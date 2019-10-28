from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEVELOPMENT'] = True
app.config['DEBUG'] = True
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testuser:testuser@localhost/jobad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Jobad(db.Model):
    __tablename__ = 'tempjobad'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    company_name = db.Column(db.String())
    location = db.Column(db.String())
    ad_url = db.Column(db.String())

    def __init__(self, title, description, company_name, location, ad_url):
        self.title = title
        self.description = description
        self.company_name = company_name
        self.location = location
        self.ad_url = ad_url

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'title': self.title,
            'description': self.description,
            'company_name': self.company_name,
            'location': self.location,
            'ad_url': self.ad_url
        }

@app.route("/")
def hello():
    try:
        jobads = Jobad.query.all()
        jobadlist = [jobad.serialize() for jobad in jobads]
        
        return render_template('index.html', jobadlist=jobadlist)
    except Exception as e:
	    return(str(e))

@app.route("/jobs")
def get_all():
    try:
        jobads = Jobad.query.all()
        return jsonify([jobad.serialize() for jobad in jobads])
    except Exception as e:
	    return(str(e))

@app.route("/job/<id>")
def get_by_id(id):
    try:
        jobad = Jobad.query.filter_by(id = id).first()
        return render_template('job.html', jobad=jobad)
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run()