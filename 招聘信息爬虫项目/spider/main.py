
from crawler import crawl_jobs
from html_parser import parse_jobs
from config import DATA_PATH

if __name__ == "__main__":
    print("开始爬取招聘信息...")
    html_list = crawl_jobs()
    print("开始解析数据...")
    parse_jobs(html_list, DATA_PATH)
    print("数据抓取与保存完成")
