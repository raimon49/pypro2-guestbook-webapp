# -*- coding: utf-8 -*-

import shelve
import os
import argparse
from datetime import datetime
from flask import Flask, request, render_template, redirect, escape, Markup

DATA_FILE = 'guestbook'
NETWORK = '127.0.0.1'
PORT = 8000

application = Flask(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description='A guestbook web application.')
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s 1.0.0')

    return parser.parse_args()

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
    """投稿用URL
    """
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()

    save_data(name, comment, create_at)

    return redirect('/')

@application.template_filter('nl2br')
def nl2br_filter(s):
    """改行文字をbrタグに置き換えるテンプレートフィルタ
    """
    return escape(s).replace('\n', Markup('<br>'))

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """datetimeオブジェクトを見易い表示にするテンプレートフィルタ
    """
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def main(debug=False):
    args = parse_args()
    application.run(NETWORK, PORT, debug=debug)

if __name__ == '__main__':
    main(debug=True)
