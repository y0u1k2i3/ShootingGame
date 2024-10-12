import sqlite3

# データベースに接続（存在しない場合は自動で作成）
conn = sqlite3.connect('game_scores.db')
cursor = conn.cursor()

# 名前とスコアを保存するテーブルの作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
    )
''')

# 変更を保存
conn.commit()
