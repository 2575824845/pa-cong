
from bs4 import BeautifulSoup
import csv

def parse_jobs(html_list, save_path):
    rows = []
    for html in html_list:
        soup = BeautifulSoup(html, "html.parser")
        quotes = soup.select(".quote")
        for q in quotes:
            job = q.select_one(".text").get_text(strip=True)
            company = q.select_one(".author").get_text(strip=True)
            city = "示例城市"
            salary = "8k-12k"
            rows.append([job, company, city, salary])

    with open(save_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["岗位名称", "公司名称", "城市", "薪资"])
        writer.writerows(rows)
