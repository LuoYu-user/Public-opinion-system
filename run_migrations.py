from sqlalchemy import text
from app import app, db

with app.app_context():
    # 直接执行SQL来添加role字段
    print("开始执行数据库迁移...")
    try:
        # 检查字段是否存在
        result = db.engine.execute(text("PRAGMA table_info(user)"))
        columns = [row[1] for row in result]
        
        if 'role' not in columns:
            # 添加role字段
            db.engine.execute(text("ALTER TABLE user ADD COLUMN role VARCHAR(20) DEFAULT 'user'"))
            print("成功添加role字段")
        else:
            print("role字段已存在")
            
    except Exception as e:
        print(f"迁移过程中发生错误: {e}")
        
    print("数据库迁移完成")
