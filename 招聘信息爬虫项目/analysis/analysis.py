
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw_jobs.csv")

# 统计岗位数量
job_count = df.groupby("公司名称").size().sort_values(ascending=False).head(5)
job_count.plot(kind="bar", title="公司岗位数量统计")
plt.tight_layout()
plt.savefig("company_job_count.png")
plt.show()
