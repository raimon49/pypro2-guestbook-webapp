# -*- coding: utf-8 -*-

import shelve
import os
from flask import Flask, request, render_template, redirect, escape, Markup

DATA_FILE = 'guestbook.dat'
NETWORK = '127.0.0.1'
PORT = 8000

application = Flask(__name__)


def save_data(name, comment, create_at):
    """投稿データを保存します
    """
    database = shelve.open(DATA_FILE)

    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']

    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })
    database['greeting_list'] = greeting_list
    database.close()

def load_data():
    """投稿されたデータを返します
    """
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()

    return greeting_list

@application.route('/')
def index():
    """トップページ
    """
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

@application.route('/post', methods=['POST'])
def post():
    # TODO
    pass

if __name__ == '__main__':
    application.run(NETWORK, PORT, debug=True)
