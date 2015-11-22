==================
ゲストブックアプリ
==================

.. image:: https://travis-ci.org/raimon49/pypro2-guestbook-webapp.svg?branch=master
    :target: https://travis-ci.org/raimon49/pypro2-guestbook-webapp
.. image:: https://requires.io/github/raimon49/pypro2-guestbook-webapp/requirements.svg?branch=master
     :target: https://requires.io/github/raimon49/pypro2-guestbook-webapp/requirements/?branch=master
     :alt: Requirements Status

目的
====

Webブラウザでコメントを投稿するWebアプリケーションの練習。

（参考：『Pythonプロフェッショナルプログラミング第2版』）

ツールのバージョン
==================

:Python:     2.7.9
:Flask:     0.10.1
:pip:        7.1.2
:pyenv:   20141211

インストールと起動方法
======================

リポジトリからコードを取得し、その下にvirtualenv環境を用意します。 ::

    $ git clone git@github.com:raimon49/pypro2-guestbook-webapp.git
    $ cd pypro2-guestbook-webapp
    $ pyenv virtualenv 2.7.9 venv-guestbook
    $ pyenv activate venv-guestbook
    $ (venv-guestbook) pyenv rehash
    $ (venv-guestbook) pip install -U pip && pip install .
    $ (venv-guestbook) guestbook

コマンドラインオプション ::

    $ guestbook -h
    usage: guestbook [-h] [-v] [-n NETWORK] [-p PORT]
    
    A guestbook web application.
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -n NETWORK, --network NETWORK
      -p PORT, --port PORT

開発手順
========

開発用インストール
------------------

1. チェックアウトする
2. 以下の手順でインストールする ::

    $ pyenv virtualenv 2.7.9 venv-edit
    $ pyenv activate venv-edit
    $ (venv-edit) pyenv rehash
    $ (venv-edit) pip install -U pip
    $ (venv-edit) pip install -e .

依存ライブラリ変更時
--------------------

1. ``setup.py`` の ``install_requires`` と ``requirements.in`` を更新する
2. 以下の手順で環境を更新する ::

    $ pyenv uninstall venv-edit
    $ pyenv activate venv-edit
    $ (venv-edit) pyenv rehash
    $ (venv-edit) pip install -U pip
    $ (venv-edit) pip install -e .
    $ (venv-edit) pip-compile requirements.in
    $ (venv-edit) pip-compile dev-requirements.in
    $ (venv-edit) pip-sync dev-requirements.txt

3. ``setup.py`` をリポジトリにコミットする
