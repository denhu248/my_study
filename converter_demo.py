from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


#        路由传参----转换器
# <int:goods_id> 指定转化参数类型
# <goods_id> 使用默认字符串（除了斜线之外的）
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    return 'goods detail page %s' % goods_id


# A自定义：全能型匹配转换器
# 1：自定义转化器是需要继承 from werkzeug.routing import BaseConverter 的BaseConverter方法
class RegexConverter(BaseConverter):
    """
    路由正则匹配
    url_map,regex:固定写法
    """

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法   用父类方法初始化url，并将其传给父类
        super(RegexConverter, self).__init__(url_map)
        # regex将接受的参数进行保存
        # 将正则表达式的参数保存到对象的属性中， flask会使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        """
        value: 路径进行正则匹配的时候提取的参数
        1.会优先将请求值，放在这里处理
        2.经过处理后才会将值return后
        3.将返回值传给视图对应接收
        :param value:
        :return:
        """
        print('调用to_python')
        # return 'abc'
        return value

    def to_url(self, value):
        """
        触发情况：
            运用反解析：url_for
        :param value:
        :return:
        """
        return '18223794550'


# B:实现独立功能转化器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        # 用父类方法初始化url，并将其传给父类
        super(MobileConverter, self).__init__(url_map)
        # self.regex ==>固定方法
        self.regex = r'1[34578]\d{9}'


# 2：自定义转化器添加在flask的应用中
#     将转化器通过converters键值对的方法添加： re：自己定义的键名 ； RegexConverter：我定义的转化器类方法
app.url_map.converters['re'] = RegexConverter
app.url_map.converters['mobile'] = MobileConverter


# 使用方式如下
# @app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
@app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
def sms_sends(mobile_num):
    return "sms send %s" % mobile_num


@app.route("/call/<mobile:mobile>")
def sms_send(mobile):
    return "sms send %s" % mobile


# 路由问题3：重定向与反解析
@app.route('/hello2')
def hello2():
    # 重定向路径2: 通过url_for（"视图函数名"）:相当于反解析
    urls = url_for("sms_sends", mobile_num='18223794660')
    # redirect 重定向
    return redirect(urls)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
