from app.scraper import BaiduNewsScraper

# 测试百度新闻抓取功能
def test_baidu_news_scraper():
    try:
        # 创建抓取器实例
        scraper = BaiduNewsScraper()
        
        # 测试抓取新闻
        keyword = '科技'
        page = 1
        print(f"正在抓取关键词 '{keyword}' 的百度新闻...")
        
        # 抓取新闻数据
        news_items = scraper.fetch_news(keyword, page)
        
        if news_items:
            print(f"成功抓取到 {len(news_items)} 条新闻")
            print("\n前3条新闻详情：")
            for i, news in enumerate(news_items[:3]):
                print(f"\n新闻 {i+1}:")
                print(f"标题: {news['title']}")
                print(f"摘要: {news['summary']}")
                print(f"来源: {news['source']}")
                print(f"原始URL: {news['original_url']}")
                print(f"封面URL: {news['cover']}")
        else:
            print("未抓取到新闻数据")
            
    except Exception as e:
        print(f"测试失败: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_baidu_news_scraper()
