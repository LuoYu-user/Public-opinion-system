import sqlite3

# 直接连接SQLite数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 查看用户表中的所有数据
print("用户表中的数据：")
cursor.execute("SELECT id, username, email, password_hash, role FROM user")
users = cursor.fetchall()

for user in users:
    print(f"ID: {user[0]}, 用户名: {user[1]}, 邮箱: {user[2]}, 角色: {user[4]}")
    print(f"  密码哈希: {'存在' if user[3] else '不存在'}")
    if user[3]:
        print(f"  哈希长度: {len(user[3])}")

# 关闭连接
conn.close()
