#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 11 - To Do Web Application w/ Flask"""


from flask import Flask, render_template, request, redirect
app = Flask(__name__)
to_do_tasks = [('Wash Car', 'joe.smith@summers.com', 'High'),
               ('Buy Bread', 'jon.snow@got.com', 'High'),
               ('Walk Dog', 'lundo@test.com', 'Medium')]


@app.route('/')
def hello_world():
    return render_template('todo.html', to_do_tasks=to_do_tasks)


if __name__ == '__main__':
    app.run()
