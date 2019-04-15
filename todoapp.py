#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment 11 - To Do Web Application w/ Flask"""


from flask import Flask, render_template, request, redirect
app = Flask(__name__)
to_do_tasks = []



@app.route('/')
def to_do_form():
    return render_template('index.html', to_do_tasks=to_do_tasks)


@app.route('/submit', methods=['POST'])
def create_to_do_list():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    to_do_tasks.append((task, email, priority))
    return redirect('/')


if __name__ == '__main__':
    app.run()
