
import requests
import time
from config import HEADERS, BASE_URL

def crawl_jobs(pages=3):
    html_list = []
    for i in range(1, pages + 1):
        url = f"{BASE_URL}/page/{i}/"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            html_list.append(r.text)
            print(f"成功抓取第 {i} 页")
        time.sleep(1)  # 合规延时
    return html_list
