==================
ゲストブックアプリ
==================

目的
====

Webブラウザでコメントを投稿するWebアプリケーションの練習。

（参考：『Pythonプロフェッショナルプログラミング第2版』）

ツールのバージョン
==================

:Python:     2.7.9
:pip:        7.1.2
:pyenv:   20141211

インストールと起動方法
======================

リポジトリからコードを取得し、その下にvirtualenv環境を用意します。

.. code-block:: bash

    $ git clone git@github.com:raimon49/pypro2-guestbook-webapp.git
    $ cd pypro2-guestbook-webapp
    $ pyenv virtualenv 2.7.9 venv-guestbook
    $ pyenv activate venv-guestbook
    $ (venv-guestbook) pyenv rehash
    $ (venv-guestbook) pip install -U pip && pip install .
    $ (venv-guestbook) guestbook

開発手順
========

開発用インストール
------------------

1. チェックアウトする
2. 以下の手順でインストールする

.. code-block:: bash

    $ pyenv virtualenv 2.7.9 venv-edit
    $ pyenv activate venv-edit
    $ (venv-edit) pyenv rehash
    $ (venv-edit) pip install -U pip
    $ (venv-edit) pip install -e .
