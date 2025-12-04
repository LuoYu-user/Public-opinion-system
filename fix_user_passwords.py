import sqlite3
from werkzeug.security import generate_password_hash

# 直接连接SQLite数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 更新admin用户的密码
print("更新admin用户的密码...")
admin_password_hash = generate_password_hash('admin123')
cursor.execute("UPDATE user SET password_hash = ? WHERE username = 'admin'", (admin_password_hash,))

# 更新或添加user用户
print("更新或添加user用户...")
user_password_hash = generate_password_hash('user123')
cursor.execute("INSERT OR REPLACE INTO user (username, email, password_hash, role) VALUES (?, ?, ?, ?)", 
              ('user', 'user@example.com', user_password_hash, 'user'))

# 提交更改
conn.commit()

# 验证更新结果
print("验证更新结果...")
cursor.execute("SELECT username, password_hash, role FROM user")
users = cursor.fetchall()
for user in users:
    print(f"用户名: {user[0]}, 角色: {user[2]}, 密码哈希: {'存在' if user[1] else '不存在'}")

# 关闭连接
conn.close()
print("密码更新完成!")
