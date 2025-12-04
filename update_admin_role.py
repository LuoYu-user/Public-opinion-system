import sqlite3

# 直接连接SQLite数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 更新admin用户的角色
print("更新admin用户的角色为'admin'...")
cursor.execute("UPDATE user SET role = 'admin' WHERE username = 'admin'")
conn.commit()

# 验证更新
print("验证更新结果...")
cursor.execute("SELECT username, role FROM user WHERE username = 'admin'")
admin = cursor.fetchone()
if admin:
    print(f"用户: {admin[0]}, 角色: {admin[1]}")
    print("更新成功!")
else:
    print("更新失败，未找到admin用户")

# 关闭连接
conn.close()
