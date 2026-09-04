import sys
from playwright.sync_api import sync_playwright

def main():
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python get_m3u8.py <网页URL>")
        print("示例: python get_m3u8.py https://www.duboku.lv/p/95899-1-2.html")
        sys.exit(1)
        
    url = sys.argv[1]
    
    with sync_playwright() as p:
        # 启动 Chromium 无头浏览器
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        m3u8_urls = []
        
        # 监听所有网络请求的事件回调
        def on_request(request):
            # 过滤包含 .m3u8 的请求 (包括 index.m3u8, master.m3u8 等)
            if ".m3u8" in request.url:
                m3u8_urls.append(request.url)
                print(f"[拦截到请求] -> {request.url}")
        
        # 绑定监听器
        page.on("request", on_request)
        
        print(f"正在加载网页: {url} ...")
        try:
            # 视频网站由于有持续的数据流，不建议使用 networkidle，使用 domcontentloaded 即可
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            
            # 额外等待5秒，确保网页的 JS 播放器加载完毕并发出 m3u8 请求
            print("页面加载完成，等待播放器初始化...")
            page.wait_for_timeout(5000)
        except Exception as e:
            print(f"提示 (可忽略): {e}")
            
        browser.close()
        
        # 总结输出
        if not m3u8_urls:
            print("\n未能拦截到任何 m3u8 链接，可能是页面结构已更改或需要验证码。")
        else:
            print("\n================ 抓取结果 ================")
            # 使用 set 去重（有时候播放器会重复请求同一个 m3u8）
            for idx, link in enumerate(set(m3u8_urls), 1):
                print(f"{idx}. {link}")

if __name__ == "__main__":
    main()
