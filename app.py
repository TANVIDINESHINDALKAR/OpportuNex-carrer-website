from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_jobs_from_db_id

app = Flask(__name__)


#html endpoint, html route
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()

    return render_template('home.html', jobs=jobs, company_name="OpportuNex")


#json endpoint, api route
#we can also access the info in the form of json and not only html
@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/api/job/<id>")
def show_job(id):
    job = load_jobs_from_db_id(id)
    return render_template('jobpage.html', job=job)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
