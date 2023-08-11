from flask import Flask, render_template, jsonify

# Create a Flask application
app = Flask(__name__)
JOBS = [{
  'id': 1,
  'Title': 'Data Analyst',
  'Location': 'Hyderbad',
  'Salary': 'Rs 10,00,000'
}, {
  'id': 2,
  'Title': 'Data Engineer',
  'Location': 'Hyderbad',
  'Salary': 'Rs 8,00,000'
}, {
  'id': 3,
  'Title': 'Web Developer',
  'Location': 'Mumbai',
  'Salary': 'Rs 12,00,000'
}]


# Define a route and the associated view function
@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS)


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


# Run the application if this script is executed
if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
