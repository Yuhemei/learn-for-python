import pandas as pd

df = pd.read_excel("网易云课堂的套餐课信息.xlsx")
print(df.info())

df = df[df["时长秒数（秒）"] != '无秒数'].copy()
df["时长秒数（秒）"] = df["时长秒数（秒）"].astype(int)

# 全部统计
df_total_agg = pd.DataFrame({
    "课时数": [len(df)],
    "总时长-小时": [round(df["时长秒数（秒）"].sum() / 3600, 2)],
    "单课时平均分钟": [round(df["时长秒数（秒）"].mean() / 60, 2)],
}).transpose()
df_total_agg.columns = ['统计指标']

df_course_agg = df.groupby(["课程序号", "课程名字"]).apply(
    lambda x: pd.Series({
        "课时数": len(x),
        "总时长-小时": round(x["时长秒数（秒）"].sum() / 3600, 2),
        "单课时平均分钟": round(x["时长秒数（秒）"].mean() / 60, 2),
    })).sort_index()

with pd.ExcelWriter("结果数据统计.xlsx") as writer:
    df_total_agg.to_excel(writer, sheet_name="总统计")
    df_course_agg.to_excel(writer, sheet_name="单课统计")
