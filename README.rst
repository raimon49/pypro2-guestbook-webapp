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

:Python:     3.8.6
:Flask:      1.1.2
:bpmappers:  0.8.2
:pip:       21.0.2

インストールと起動方法
======================

リポジトリからコードを取得し、その下にvirtualenv環境を用意します。 ::

    $ git clone git@github.com:raimon49/pypro2-guestbook-webapp.git
    $ cd pypro2-guestbook-webapp
    $ python3 -m venv venv/venv-pypro2-guestbook-webapp
    $ source venv/venv-pypro2-guestbook-webapp/bin/activate
    $ (venv-pypro2-guestbook-webapp) pyenv rehash
    $ (venv-pypro2-guestbook-webapp) pip install -U pip && pip install .
    $ (venv-pypro2-guestbook-webapp) guestbook

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

1. ファイル ``setup.py`` の ``install_requires`` とファイル ``requirements.in`` を更新する
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
