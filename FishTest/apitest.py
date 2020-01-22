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
