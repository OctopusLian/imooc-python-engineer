from flask import Flask, current_app, g, request, session
app = Flask(__name__)


@app.route('/index')
def index():
    print(app)
    print(current_app)
    print(app == current_app)
    print(app is current_app)
    return 'index'


@app.route('/')
def hello_world():
    """ 视图函数 """
    return 'hello_world, success'


@app.route('/user/')
@app.route('/user/<page>')
def list_user(page=1):
    return '您好，你是第{}页用户'.format(page)


app.add_url_rule('/home', 'home', hello_world)

print(app.url_map)

# v1.0之后的版本，不推荐的写法
# if __name__ == '__main__':
#    app.run()