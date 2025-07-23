# project_config.md

## 使用技術

- Python 3.7 以上
- Flask >=2.0.0
- Flask-WTF >=1.0.0
- WTForms >=2.3.0
- Bootstrap-Flask >=2.0.0
- Quill.js (CDN)

## 重要なパターンとコーディング規約

- PEP8 に準拠した Python コード
- Flask 拡張として Blueprint パターンを意識
- WTForms のカスタムフィールドは`fields.py`に実装
- バージョン管理は`setup.py`と`__init__.py`の両方で行う
- テストは pytest で記述

## その他

- PyPI 配布用パッケージ構成
- ドキュメントは README.md に記載
- 変更履歴は CHANGELOG.md で管理
