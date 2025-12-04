from app import app, db
from sqlalchemy import text

with app.app_context():
    # 检查user表的列
    print("检查user表的列结构...")
    result = db.engine.execute(text("PRAGMA table_info(user)"))
    columns = [row[1] for row in result]
    print("当前user表的列:", columns)
    
    # 检查role列是否存在
    if 'role' not in columns:
        print("添加role列...")
        try:
            db.engine.execute(text("ALTER TABLE user ADD COLUMN role VARCHAR(20) DEFAULT 'user'"))
            print("成功添加role列")
        except Exception as e:
            print(f"添加role列失败: {e}")
    else:
        print("role列已存在")
        
    # 再次检查列
    result = db.engine.execute(text("PRAGMA table_info(user)"))
    updated_columns = [row[1] for row in result]
    print("更新后的user表列:", updated_columns)
