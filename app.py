from flask import Flask, current_app

# static_url_path   这是访问静态文件的前缀，默认："/static"，（不修改static文件名）http://127.0.0.1:5000/static/
# static_folder     这是指明静态文件目录，默认：static
# template_folder   这是指明模板文件路径，默认：templates
app = Flask(__name__,
            static_url_path="/static",
            static_folder="static",
            template_folder="templates"
            )

# 配置参数文件的使用方式
# 1.使用配置文件 from_pyfile: 通过指明相应的 推荐使用
app.config.from_pyfile("setting/config.cfg")

# 2.使用类来加载配置文件
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)

# 直接获取配置文件参数值：app.config.get(“变量名”)
# 导包间接接获取配置文件参数值：current_app.config.get(“变量名”)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 路由规则， 注意两边“/”
@app.route('/about/')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)












# 首先，我们导入了 Flask 类。这个类的实例将会是我们的 WSGI 应用程序。
# 接下来，我们创建一个该类的实例，第一个参数是应用模块或者包的名称。
# 如果你使用单一的模块（如本例），你应该使用 __name__ ，
# 因为模块的名称将会因其作为单独应用启动还是作为模块导入而有不同（ 也即是 '__main__' 或实际的导入名）。这是必须的，这样 Flask 才知道到哪去找模板、静态文件等等。详情见 Flask的文档。
# 然后，我们使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。
# 这个函数的名字也在生成 URL 时被特定的函数采用，这个函数返回我们想要显示在用户浏览器中的信息。
# 最后我们用 run() 函数来让应用运行在本地服务器上。 其中 if __name__ =='__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。


