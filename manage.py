#!/usr/bin/env python
import os

from app import create_app

from flask_script import Manager, Server, Shell

app = create_app('default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
