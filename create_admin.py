from app import app, db
from app.models import User

with app.app_context():
    # 检查是否已有管理员用户
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        # 创建管理员用户
        admin = User(
            username='admin',
            email='admin@example.com',
            role='admin'
        )
        admin.set_password('admin123')
        
        # 创建普通用户
        user = User(
            username='user',
            email='user@example.com',
            role='user'
        )
        user.set_password('user123')
        
        # 保存到数据库
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()
        
        print("管理员用户创建成功:")
        print(f"用户名: admin, 密码: admin123, 角色: admin")
        print(f"用户名: user, 密码: user123, 角色: user")
    else:
        print("管理员用户已存在")
