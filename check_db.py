import sqlite3

# 直接连接SQLite数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 检查user表结构
print("检查user表的最终结构...")
cursor.execute("PRAGMA table_info(user)")
columns = [row[1] for row in cursor.fetchall()]
print("user表的列:", columns)

# 查看用户数据
print("\n当前用户数据:")
cursor.execute("SELECT username, role FROM user")
users = cursor.fetchall()
for user in users:
    print(f"用户名: {user[0]}, 角色: {user[1]}")

# 关闭连接
conn.close()
