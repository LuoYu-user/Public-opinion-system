import sqlite3

# 直接连接SQLite数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 检查user表结构
print("检查user表结构...")
cursor.execute("PRAGMA table_info(user)")
columns = [row[1] for row in cursor.fetchall()]
print("当前列:", columns)

# 添加role列
if 'role' not in columns:
    print("添加role列...")
    cursor.execute("ALTER TABLE user ADD COLUMN role VARCHAR(20) DEFAULT 'user'")
    conn.commit()
    print("成功添加role列")
else:
    print("role列已存在")

# 检查修复后的结构
cursor.execute("PRAGMA table_info(user)")
updated_columns = [row[1] for row in cursor.fetchall()]
print("修复后的列:", updated_columns)

# 关闭连接
conn.close()
