# Todo Project 5

JWT 認証APIとWeb画面を併用し、Docker 環境で開発・本番差異を吸収したタスク管理アプリです。  
Render への本番デプロイを前提に設計しています。

---

## デモ

https://project5-yuhx.onrender.com

**ログイン情報（デモ用）**  
ユーザー名: raguna  
パスワード: kaibasensei


## 主な機能

- ユーザごとのタスク管理
- タスクの作成 / 一覧 / 更新 / 完了管理
- 期限日 (due_date) 設定
- JWT による API 認証
- Django 管理画面
- pytest によるテスト実行環境

---

## 技術スタック

| 分野 | 技術 |
|------|------|
| Backend | Django 4.2 |
| API | Django REST Framework |
| 認証 | JWT (SimpleJWT) |
| DB | PostgreSQL / SQLite(ローカル簡易利用) |
| コンテナ | Docker / docker-compose |
| WSGI | Gunicorn |
| テスト | pytest / pytest-django / pytest-cov |
| デプロイ | Render |

ローカルと本番で同一構成を維持するため、Docker + PostgreSQL を採用しています。

---

## アーキテクチャ概要

- `tasks` 認証・画面表示・API を同一 Django プロジェクト内で共存させ、将来的な SPA 分離を想定した構成です。
- `Task` モデルは User 外部キーを持ち、マルチユーザ対応
- ルートURL `/` にタスク一覧画面を配置し、UI導線を簡素化
- API 認証は JWT トークン発行・更新エンドポイントを分離
- settings.py で環境変数ベースの設定切替を行い、本番/開発の差異を吸収

---

## データモデル

### Task

| フィールド | 型 | 説明 |
|------------|----|------|
| title | CharField | タスク名 |
| completed | BooleanField | 完了フラグ |
| created_at | DateTimeField | 作成日時 |
| due_date | DateField | 期限日 (任意) |
| user | ForeignKey | 所有ユーザ |

シンプルな構成とし、拡張しやすい最小モデル設計としています。

---

## 環境構築

### 1. リポジトリをクローン

git clone <repository-url>
cd todo_project5

shell
コードをコピーする

### 2. 環境変数ファイル作成

cp .env.example .env

`.env` には SECRET_KEY / DEBUG / DATABASE_URL を設定します。
`.env.example` に記載のフォーマットを参考にしてください。

### 3. Docker ビルド & 起動

docker-compose up --build

コードをコピーする

ブラウザで以下にアクセス

http://localhost:8000

yaml
コードをコピーする

---

## JWT 認証エンドポイント

| エンドポイント | 内容 |
|----------------|------|
| `/api/token/` | トークン発行 |
| `/api/token/refresh/` | トークン更新 |

---

## テスト実行

docker-compose run test

yaml
コードをコピーする

pytest + coverage により tasks アプリのテストを実行します。

---

## 本番環境

- Render にデプロイ
- DATABASE_URL / SECRET_KEY / DEBUG は環境変数管理
- Gunicorn + PostgreSQL 構成

---

## 設計上の工夫

- 環境変数ベース設定によりローカルと本番の差異を最小化
- Docker により開発環境の再現性を担保
- JWT 認証でフロントエンド分離を想定可能な API 設計
---

## 今後の改善予定

- タスクの優先度・カテゴリ機能追加
- API エラーハンドリングの統一
- フロントエンド SPA 分離

---