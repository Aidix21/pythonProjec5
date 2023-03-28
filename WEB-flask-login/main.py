from flask import Flask
from data import db_session
import jobs_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()

#http://127.0.0.1:8080/api/jobs