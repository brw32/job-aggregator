from flask import Flask, render_template, request
from models import Session, Job
import os


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    session = Session()
    query = request.args.get("q", "")
    tag = request.args.get("tag", "")
    jobs = session.query(Job)
    if query:
        jobs = jobs.filter(Job.title.ilike(f"%{query}%"))
    if tag:
        jobs = jobs.filter(Job.tags.ilike(f"%{tag}%"))
    jobs = jobs.all()
    return render_template("index.html", jobs=jobs, query=query, tag=tag)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)