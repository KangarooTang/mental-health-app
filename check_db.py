import sqlite3

# 连接数据库
conn = sqlite3.connect('mental_health.db')
cursor = conn.cursor()

# 查询最新一条记录
cursor.execute('SELECT id, content, phq9_score, gad7_score FROM emotion_records ORDER BY id DESC LIMIT 1')
row = cursor.fetchone()

if row:
    print(f'最新记录 ID: {row[0]}')
    print(f'内容: {row[1]}')
    print(f'phq9_score: {row[2]}')
    print(f'gad7_score: {row[3]}')
else:
    print('无记录')

conn.close()