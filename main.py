from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)
    return render_template('th.html', title="Work log", jobs=jobs)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    app.run(host="127.0.0.1", port="8080")
