from data.jobs import Jobs
from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# Добавляем капитана

def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()


    user = User()
    user.surname = "Ivanov",
    user.name = "Ivan",
    user.age = 21,
    user.position = "пилот",
    user.speciality = "мойщик посуды",
    user.address = "module_2",
    user.email = "ivanov@mars.org"

    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()