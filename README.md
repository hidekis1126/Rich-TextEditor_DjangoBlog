プロジェクトのセットアップ

このプロジェクトをローカル環境で実行するには、以下の手順を実行してください。

1. 依存関係をインストールします：

  pip install -r requirements.txt

依存関係は requirements.txt ファイルに記載されています1。

2. Djangoサーバーを起動します：
  
  python manage.py runserver

プロジェクトの機能

このプロジェクトは、Djangoを使用したブログアプリケーションです。以下の機能が含まれています：

- ブログ記事の作成、編集、削除
- TinyMCEを使用したリッチテキストエディタ
- 画像のアップロード機能
- コメントの作成、削除

使用技術

- Python 3.11
- Django 5.0
- django-tinymce 3.6.1
- Pillow==10.1.0


仮想環境で実行するには、以下の手順を実行してください。
1. test-richtextediterディレクトリで、仮想環境作成
2. python3 -m venv env
3. source env/bin/activate
4. pip install -r requirements.txt
5. python manage.py runserver

## プロジェクトのセットアップ

1. まず、必要なパッケージをインストールします。以下のコマンドを実行してください。
bash
pip install -r requirements.txt

2. 次に、データベースのマイグレーションを行います。以下のコマンドを実行してください。
bash
python manage.py migrate

3. 最後に、開発サーバーを起動します。以下のコマンドを実行してください。
bash
python manage.py runserver

以上で、開発環境のセットアップは完了です。ブラウザで`http://localhost:8000`にアクセスして、アプリケーションが正しく動作していることを確認してください。

## ファイルストレージ

このプロジェクトでは、Djangoの`django.core.files.storage`モジュールの`default_storage`と`FileSystemStorage`を使用して、ファイルの保存と取得を行っています。

`default_storage`は設定で指定されたデフォルトのストレージシステムを使用します。通常はファイルシステムを使用しますが、設定によりAmazon S3などの他のストレージシステムを使用することも可能です。

一方、`FileSystemStorage`は直接ファイルシステムを操作するためのクラスで、特定のディレクトリに対する操作を行いたい場合などに使用します。
python
from django.core.files.storage import default_storage, FileSystemStorage

これらのクラスを適切に使用することで、ファイルのアップロードやダウンロードなどの操作を行うことができます。# Rich-TextEditor_DjangoBlog
