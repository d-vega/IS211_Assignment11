#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 11 - To Do Web Application w/ Flask"""


import re
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
to_do_tasks = []


@app.route('/', methods=['GET', 'POST'])
def to_do_form():
    return render_template('index.html', to_do_tasks=to_do_tasks)


@app.route('/submit', methods=['POST'])
def create_to_do_list():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    try:
        if task is None or re.search(r'^\s*$', task):
            raise Exception('Task is null')
        else:
            pass

        if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            pass
        else:
            raise Exception('Invalid email format')

        if priority in ('low', 'medium', 'high'):
            pass
        else:
            raise Exception('Invalid priority choice')

        to_do_tasks.append((task, email, priority))
        return redirect('/')

    except Exception as error:
        print error
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear_to_do_list():
    global to_do_tasks
    to_do_tasks = []
    return redirect(url_for('to_do_form'), code=307)


if __name__ == '__main__':
    app.run()
