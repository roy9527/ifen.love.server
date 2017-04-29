import os
bind='127.0.0.1:8080' #绑定的端口
workers=2 #worker数量
backlog=2048
debug=True
proc_name='gunicorn.pid'