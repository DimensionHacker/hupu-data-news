# 本脚本的作用：
# 1.生成频道热度统计.xlsx；
# 2.生成标题文本.txt；

import pandas as pd

# 读取 Excel
df = pd.read_excel("hupu.xlsx")

# 按频道统计
result = (
    df.groupby("话题来源")["回复数"]
      .agg(
          新闻数量="count",
          总回复量="sum",
          平均回复量="mean",
          最大回复量="max"
      )
      .reset_index()
)

# 按总回复量降序排列
result = result.sort_values("总回复量", ascending=False)

# 保存结果
result.to_excel("频道热度统计.xlsx", index=False)


# 保存结果
with open("标题文本.txt", "w", encoding="utf-8") as f:
    for title in df["标题"]:
        f.write(str(title) + "\n")

print("\n程序执行完成！\n")