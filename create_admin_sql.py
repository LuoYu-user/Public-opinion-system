import sqlite3
from werkzeug.security import generate_password_hash
from datetime import datetime

# 连接到数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 生成密码哈希
admin_password = generate_password_hash('admin123')
user_password = generate_password_hash('user123')

# 获取当前时间
current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# 创建管理员用户
cursor.execute('''
    INSERT OR IGNORE INTO user (username, email, password_hash, role, created_at)
    VALUES (?, ?, ?, ?, ?)
''', ('admin', 'admin@example.com', admin_password, 'admin', current_time))

# 创建普通用户
cursor.execute('''
    INSERT OR IGNORE INTO user (username, email, password_hash, role, created_at)
    VALUES (?, ?, ?, ?, ?)
''', ('user', 'user@example.com', user_password, 'user', current_time))

# 提交事务
conn.commit()

print("用户创建成功:")
print("管理员: 用户名=admin, 密码=admin123")
print("普通用户: 用户名=user, 密码=user123")

# 关闭连接
conn.close()
