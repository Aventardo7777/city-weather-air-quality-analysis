# -*- coding: utf-8 -*-
"""
Python数据分析大作业
多城市天气与空气质量分析
城市：北京、上海、广州、成都、南昌
时间：2025-01-01 ~ 2025-12-31  5×365=1825条数据
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings("ignore")

# =====================全局配置=====================
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

city_list = ["北京", "上海", "广州", "成都", "南昌"]
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
day_count = (end_date - start_date).days + 1

# 各城市基础气候基准值
city_base_temp = {
    "北京": 12,
    "上海": 17,
    "广州": 22,
    "成都": 17,
    "南昌": 18
}
city_base_aqi = {
    "北京": 76,
    "上海": 54,
    "广州": 43,
    "成都": 86,
    "南昌": 61
}

# =====================生成日期序列=====================
date_range = [start_date + timedelta(days=i) for i in range(day_count)]
all_data = []

# =====================逐城市生成模拟气象数据=====================
np.random.seed(66)
for city in city_list:
    base_t = city_base_temp[city]
    base_a = city_base_aqi[city]
    for dt in date_range:
        month = dt.month
        # 季节温度系数
        if month in [12, 1, 2]:
            season_t_offset = -13
        elif month in [3, 4, 5]:
            season_t_offset = -3
        elif month in [6, 7, 8]:
            season_t_offset = 11
        else:
            season_t_offset = 2

        avg_temp = base_t + season_t_offset + np.random.normal(0, 2.2)
        max_temp = avg_temp + np.random.uniform(3.2, 7.5)
        min_temp = avg_temp - np.random.uniform(3.2, 7.5)

        # 降水量（夏季多雨，冬季少雨）
        rain_coef = 1.8 if month in [5, 6, 7, 8] else 0.35
        precipitation = abs(np.random.normal(0, 9.2)) * rain_coef

        humidity = np.clip(np.random.normal(72, 9), 30, 98)
        wind = np.clip(np.random.normal(12, 5.5), 1, 38)
        pressure = np.clip(np.random.normal(1013, 7), 995, 1032)

        # AQI 季节性波动
        season_a_coef = [1.3, 1.24, 1.1, 0.94, 0.84, 0.76, 0.74, 0.79, 0.91, 1.02, 1.16, 1.26][month - 1]
        aqi = base_a * season_a_coef * np.random.normal(1, 0.16)
        aqi = np.clip(aqi, 22, 298)
        pm25 = aqi * 0.74 * np.random.normal(1, 0.11)
        pm10 = aqi * 1.21 * np.random.normal(1, 0.11)

        # 空气质量等级
        if aqi <= 50:
            level = "优"
        elif aqi <= 100:
            level = "良"
        elif aqi <= 150:
            level = "轻度污染"
        elif aqi <= 200:
            level = "中度污染"
        else:
            level = "重度污染"

        row = {
            "日期": dt,
            "城市": city,
            "最高温度(℃)": round(max_temp, 1),
            "最低温度(℃)": round(min_temp, 1),
            "平均温度(℃)": round(avg_temp, 1),
            "降水量(mm)": round(precipitation, 1),
            "平均相对湿度(%)": round(humidity, 1),
            "最大风速(km/h)": round(wind, 1),
            "平均气压(hPa)": round(pressure, 1),
            "AQI": round(aqi, 1),
            "PM2.5(μg/m³)": round(pm25, 1),
            "PM10(μg/m³)": round(pm10, 1),
            "空气质量等级": level
        }
        all_data.append(row)

# =====================构造总数据表=====================
total_df = pd.DataFrame(all_data)
print(f"总数据行数：{len(total_df)} （5城市×365天=1825行，符合要求）")

# 新增衍生字段
total_df["温度日较差(℃)"] = round(total_df["最高温度(℃)"] - total_df["最低温度(℃)"], 1)
total_df["月份"] = total_df["日期"].dt.month


def get_season(m):
    if m in [12, 1, 2]:
        return "冬季"
    elif m in [3, 4, 5]:
        return "春季"
    elif m in [6, 7, 8]:
        return "夏季"
    else:
        return "秋季"


total_df["季节"] = total_df["月份"].apply(get_season)

# =====================导出Excel（1825条完整数据）=====================
total_df.to_excel("weather_total_data.xlsx", index=False, sheet_name="完整天气数据集")
print("✅ 已生成文件：weather_total_data.xlsx")

# =====================作业要求四项数据分析=====================
print("\n==========【分析1：各城市年度温度统计】==========")
temp_stat = total_df.groupby("城市")["平均温度(℃)"].agg(["mean", "max", "min"]).round(2)
print(temp_stat)

print("\n==========【分析2：各城市全年总降水量】==========")
rain_sum = total_df.groupby("城市")["降水量(mm)"].sum().round(1)
print(rain_sum)

print("\n==========【分析3：极端高温/低温天数统计】==========")
hot_days = total_df[total_df["最高温度(℃)"] >= 35].groupby("城市").size()
cold_days = total_df[total_df["最低温度(℃)"] <= 0].groupby("城市").size()
print("高温天数(≥35℃):")
print(hot_days)
print("低温天数(≤0℃):")
print(cold_days)

print("\n==========【分析4：空气质量全年优良率】==========")
good_days = total_df[total_df["空气质量等级"].isin(["优", "良"])].groupby("城市").size()
total_days = total_df.groupby("城市").size()
good_rate = (good_days / total_days * 100).round(1)
print(good_rate)

# =====================四张可视化图表=====================
# 图1 温度趋势
fig1, ax1 = plt.subplots(figsize=(12, 6))
for city in city_list:
    sub = total_df[total_df["城市"] == city].sort_values("日期")
    smooth_temp = sub["平均温度(℃)"].rolling(7).mean()
    ax1.plot(sub["日期"], smooth_temp, label=city)
ax1.set_title("五大城市2025年日均温度变化趋势（7日平滑）")
ax1.set_xlabel("日期")
ax1.set_ylabel("平均温度 ℃")
ax1.legend()
ax1.grid(alpha=0.3)
plt.savefig("1_温度趋势图.png", dpi=150, bbox_inches="tight")
plt.show()

# 图2 全年降水总量
fig2, ax2 = plt.subplots(figsize=(10, 5))
colors = ["#f44336", "#2196f3", "#4caf50", "#ff9800", "#9c27b0"]
ax2.bar(rain_sum.index, rain_sum.values, color=colors)
ax2.set_title("各城市2025年全年总降水量")
ax2.set_ylabel("总降水量 mm")
ax2.grid(axis="y", alpha=0.3)
plt.savefig("2_降水总量对比图.png", dpi=150, bbox_inches="tight")
plt.show()

# 图3 极端天气天数
fig3, ax3 = plt.subplots(figsize=(10, 5))
x_axis = np.arange(len(city_list))
w = 0.35
y_hot = [hot_days.get(c, 0) for c in city_list]
y_cold = [cold_days.get(c, 0) for c in city_list]
ax3.bar(x_axis - w / 2, y_hot, w, label="高温天数≥35℃", color="#ff6666")
ax3.bar(x_axis + w / 2, y_cold, w, label="低温天数≤0℃", color="#66ccff")
ax3.set_xticks(x_axis)
ax3.set_xticklabels(city_list)
ax3.set_title("各城市极端高温、低温天数统计")
ax3.set_ylabel("天数")
ax3.legend()
plt.savefig("3_极端天气统计图.png", dpi=150, bbox_inches="tight")
plt.show()

# 图4 AQI优良率
fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.bar(good_rate.index, good_rate.values, color="#36bc91")
ax4.set_title("五大城市全年空气质量优良率")
ax4.set_ylabel("优良率 %")
ax4.grid(axis="y", alpha=0.3)
plt.savefig("4_AQI优良率对比图.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n🎉 运行完成！输出文件清单：")
print("1. weather_total_data.xlsx （1825条完整数据集）")
print("2. 1_温度趋势图.png")
print("3. 2_降水总量对比图.png")
print("4. 3_极端天气统计图.png")
print("5. 4_AQI优良率对比图.png")