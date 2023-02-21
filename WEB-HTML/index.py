from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = "Миссия колонизация Марса"
    return render_template('index.html', **param)

@app.route('/promotion')
def promotion():
    return """
            <p>Человечество вырастает из детства.<br>
            Человечеству мала одна планета.<br>
            Мы сделаем обитаемыми безжизненные пока планеты.<br>
            И начнем с Марса!</p>

            <h3>Присоединяйся!<h3>"""


@app.route('/image_mars')
def image_mars():
  f = open('static/pages/image_mars.html', encoding='utf-8')
  text = f.read()
  text = text.replace('../', 'static/')
  return text



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


#http://127.0.0.1:8080/index
#http://127.0.0.1:8080/
