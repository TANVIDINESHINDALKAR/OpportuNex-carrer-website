from flask import Flask, json, render_template, jsonify, request
from database import load_jobs_from_db, load_jobs_from_db_id, add_application_to_db

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
    if not job:
        return "Not Found", 404

    return render_template('jobpage.html', job=job)


@app.route("/api/jobs/<id>")
def show_job_json(id):
    job = load_jobs_from_db_id(id)
    return jsonify(job)


@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    job = load_jobs_from_db_id(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html',
                           application=data,
                           job=job)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
