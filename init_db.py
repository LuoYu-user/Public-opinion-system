import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app, db
from app.models import User, News, Comment

print("开始初始化数据库...")
print(f"当前工作目录: {os.getcwd()}")
print(f"数据库URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

# 创建应用上下文
with app.app_context():
    try:
        # 创建所有表
        db.create_all()
        print("数据库表创建成功！")
        
        # 添加一些示例数据
        # 创建测试用户
        test_user = User(username='admin', email='admin@example.com')
        db.session.add(test_user)
        
        # 创建测试新闻
        test_news = News(
            title='测试新闻标题',
            content='这是一条测试新闻内容',
            source='测试来源',
            url='http://example.com/test',
            sentiment=0.3
        )
        db.session.add(test_news)
        
        # 提交数据
        db.session.commit()
        print("示例数据添加成功！")
    except Exception as e:
        import traceback
        traceback.print_exc()
        db.session.rollback()
        print(f"操作出错: {e}")
    finally:
        db.session.close()
        print("数据库会话已关闭")