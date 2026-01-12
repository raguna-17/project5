# Project5 Todo App

Django + Docker で作った Todo アプリです。

## 環境

- Python 3.11
- Django 4.x
- Docker / docker-compose
- PostgreSQL (オプション)

## デプロイ

Render でのデプロイ手順:

1. GitHub リポジトリを Render に接続
2. 環境変数 `SECRET_KEY` と `DEBUG` を設定
3. Docker Runtime でサービスを作成
4. Deploy

## ローカル実行

```bash
docker-compose up --build
