from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000',
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000',
  },
  {
    'id': 5,
    'title': 'Machine Learning Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 18,00,000',
  },
  {
    'id': 6,
    'title': 'Product Manager',
    'location': 'New York, USA',
    'salary': '$130,000',
  },
  {
    'id': 7,
    'title': 'UX/UI Designer',
    'location': 'Berlin, Germany',
    'salary': '€70,000',
  },
  {
    'id': 8,
    'title': 'DevOps Engineer',
    'location': 'Remote',
    'salary': 'Rs. 14,00,000',
  },
  {
    'id': 9,
    'title': 'Full Stack Developer',
    'location': 'Toronto, Canada',
    'salary': 'CAD 90,000',
  },
  {
    'id': 10,
    'title': 'Cybersecurity Analyst',
    'location': 'Sydney, Australia',
    'salary': 'AUD 100,000',
  },
  {
    'id': 11,
    'title': 'AI Researcher',
    'location': 'London, UK',
    'salary': '£85,000',
  },
  {
    'id': 12,
    'title': 'Systems Architect',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 20,00,000',
  },
  {
    'id': 13,
    'title': 'Cloud Engineer',
    'location': 'San Francisco, USA',
    'salary': '$140,000',
  },
  {
    'id': 14,
    'title': 'Network Administrator',
    'location': 'Tokyo, Japan',
    'salary': '¥8,000,000',
  },
  {
    'id': 15,
    'title': 'Mobile App Developer',
    'location': 'Remote',
    'salary': 'Rs. 13,00,000',
  },
  {
    'id': 16,
    'title': 'Business Analyst',
    'location': 'Mumbai, India',
    'salary': 'Rs. 9,00,000',
  },
  {
    'id': 17,
    'title': 'Data Engineer',
    'location': 'Seattle, USA',
    'salary': '$115,000',
  },
  {
    'id': 18,
    'title': 'IT Support Specialist',
    'location': 'Dublin, Ireland',
    'salary': '€60,000',
  },
  {
    'id': 19,
    'title': 'Technical Writer',
    'location': 'Remote',
    'salary': 'Rs. 8,00,000',
  },
  {
    'id': 20,
    'title': 'Quality Assurance Engineer',
    'location': 'Singapore',
    'salary': 'SGD 85,000',
  }
   ]


@app.route("/")
def hello():
  return render_template("home.html", jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
 

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)
