from flask import Flask, render_template, jsonify
# create a Flask app
app = Flask(__name__)
JOBS = [
  {"id": 1,
  "title": "Data Analyst",
   "location": "Bengaluru, India",
  "salary": "Rs. 10,00,000"},
  
  {"id": 2,
  "title": "Data Scientist",
   "location": "Mumbai, India",
  "salary": "Rs. 15,00,000"},
  
  {"id": 3,
  "title": "Backend Engineer",
   "location": "Remote",
  },
  
  {"id": 4,
  "title": "Frontend Engineer",
   "location": "San Franciso, USA",
  "salary": "$ 100,000"},
]

# register a route to the application
@app.route("/")
def hello():
  return render_template('home.html', 
                         jobs=JOBS, 
                        company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

# check if we are running this app.py file as script, as python app.py
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # debug=True will auto restart the server when there are changes in the code
# "0.0.0.0" means it will run in local