from flask import Flask,current_app

app = Flask(__name__)
# 应用上下文， 请求上下文
#Flask appContext, Request RequestContext
#离线应用， 手动推入栈
ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config["DEBUG"]
ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config["DEBUG"]

# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
#上下文表达式必须返回一个上下文管理器


#1.连接数据库
#2.sql
#3.释放数据库
'''
两种方法 ：
1. 用try except finally
2. 用with语句上下文
'''

#with open(r'D:\text') as f:
#    print(f.read())




class A:
    def __enter__(self):
        a=1
        print("connect resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        b=2
        print("close resource")
        print(exc_type,exc_val,exc_tb)
        #True代表已处理异常， False代表未处理异常
        return True
    def query(self):
        print("query data")

with A() as object_A:
    object_A.query()
