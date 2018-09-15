# 《Flask web开发————基于Python的Web应用开发实战》
# 第2章 程序的基本结构：
# 2.1 初始化：创建程序实例（Flask类的对象）
from flask import Flask
app = Flask(__name__)   #将name参数传给Flask程序，程序主模块或包的名字app？

# 2.2 路由和视图函数(view function)：客户端（Web浏览器）把请求发送给Web服务器，Web服务器再把请求发送给Flask程序实例。
# 程序实例需要知道每个URL请求运行哪些代码。处理URL与函数之间关系的程序成为路由。
@app.route('/')     # app.route修饰器，把修饰的函数注册为路由（事件的处理程序）。
def index():
    return '<h1> Hello World! </h1>'
# 如果部署程序的服务器域名为www.example.com，在浏览器中访问该域名时，会触发index()程序，返回值称为响应，即显示给用户的文档。

@app.route('/')     # 动态路由：访问这个地址时，会看到一则针对个人的欢迎信息。
def user(name):
    return '<h1> Hello, %s! </h1>' %name

# 2.3 启动服务器：用run方法。
# 服务器启动后，会进入轮询，等待并处理请求。轮询会一直运行，直到程序停止，比如按Ctrl+C键。
if __name__ == '__main__':
    app.run(debug=True)     # 启用调试模式，可以把debug参数设为True
