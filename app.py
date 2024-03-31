from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title': 'data analyst',
    'location':'bagaluru , india',
    'salary':'Rs.10,00,000',
  },
  {
    'id':2,
    'title': 'scientist',
    'location':'delhi , india',
    'salary':'Rs.12,00,000',
  },
  {
    'id':3,
    'title': 'frontend Engineer',
    'location':'remote',
    
  },
    {
    'id':4,
    'title': 'backend Engineer',
    'location':'San Francisco , USA',
    'salary':'USD.10,00,000',
  },

]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS , company_name='one learner')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__  == '__main__':
  app.run(host='0.0.0.0', debug=True)
