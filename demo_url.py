from flask import Flask, current_app, redirect, url_for

app = Flask(__name__)

# methods指明请求方式
@app.route('/', methods=["POST", "GET"])
def hello_world():
    # 查看路由
    print(app.url_map)
    return 'Hello World!'

# 路由问题1：路由重名， 优先执行上面的，可以通过限制访问方式进行区分
@app.route('/hello')
def hello():
    return "hello"

# 路由问题2：一个视图，多个访问路径。 @app.route('')用它定义就行，有几个，定义几个
@app.route('/h')
@app.route('/hello1')
def hello1():
    return "hello1"

# 路由问题3：重定向与反解析
@app.route('/hello2')
def hello2():
    # 重定向路径1：直接写死
    url = '/'
    # 重定向路径2: 通过url_for（"视图函数名"）:相当于反解析
    urls = url_for("hello_world")
    # redirect 重定向
    return redirect(url)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

