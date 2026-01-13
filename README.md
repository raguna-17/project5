# Todoアプリ (Django + Docker)

シンプルな **Todo管理アプリ**。  
Django REST Framework で API を提供しつつ、SPA風にフロントからタスクを操作できます。Dockerで簡単に立ち上げ可能。

> ⚠️ このアプリは本番向け設定で動作します。ローカルで `runserver` を使った開発用サーバーでは一部機能が正しく動作しない場合があります。

---

## 主な機能

- タスクの作成・編集・削除
- タスクの完了/未完了切り替え
- ユーザー別タスク管理（認証必須）
- REST API + SPA HTML 配信
- REST API + SPA HTML 配信
- JWTトークンによる認証でユーザーごとにタスク操作を保護

---

## 技術スタック

- Python 3.11
- Django 4.2
- Django REST Framework
- PostgreSQL 15
- Gunicorn
- Docker / Docker Compose
- Pytest / pytest-django / pytest-cov
- GitHub ActionsによるCI自動化
- プッシュ時に自動でテストとカバレッジチェックを実行


---

## セットアップ

### 1. リポジトリをクローン
```bash
git clone <repo_url>
cd todo_project5
```

## 2. .env を準備
```bash
cp .env.example .env
```

## 3. Dockerで起動
```bash
docker-compose up -d
```

## 4. アプリにアクセス

http://localhost:8000/


## テスト実行
```bash
docker-compose run --rm test
```
- タスクアプリのテストを実行
- カバレッジレポートも確認可能
