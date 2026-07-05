<div align="center">

# Multi-City Weather & Air Quality Data Analysis
### 多城市气象与空气质量多维数据分析可视化项目

<img src="https://img.shields.io/badge/Python-3.8~3.12-blue?style=flat-square" />
<img src="https://img.shields.io/badge/Pandas-DataClean-orange?style=flat-square" />
<img src="https://img.shields.io/badge/Matplotlib%2FSeaborn-Visual-green?style=flat-square" />
<img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square" />

<br>
<a href="https:github.com/Aventardo7777/city-weather-air-quality-analysis" target="_blank">👉 仓库直达链接（新标签打开）</a>
</div>

---

## 📌 项目简介
本项目为Python数据分析综合实战项目，基于全国多城市全年气象与空气质量监测数据集，搭建**时序气象指标-污染物浓度-空气质量等级**三维量化分析体系。
全部数据集内置代码，无需外部Excel文件，一键运行自动生成5套科研标准可视化图表，适用于环境数据分析、课程作业、城市环境评估参考。

## 🎯 核心功能亮点
1. **完整多城市内置监测数据集**
    - 全年时序数据：日均气温、相对湿度、PM2.5、PM10、AQI指数；
    - 自动划分优/良/轻度污染/中度污染/重度污染五级空气质量标签；
2. **全平台中文绘图适配**
    内置多系统中文字体兼容代码，图表标题、坐标轴中文无乱码；
3. **五大自动输出专业可视化图表**
    | 图表序号 | 图表名称 | 分析用途 |
    |--------|--------|--------|
    | 图1 | 城市月度平均气温时序折线图 | 全年温度季节变化趋势观测 |
    | 图2 | 各城市年均AQI对比柱状图 | 横向对比城市整体空气质量优劣 |
    | 图3 | 城市PM2.5浓度分布箱线图 | 污染物浓度波动区间、异常值检测 |
    | 图4 | 温湿度相关性散点拟合图 | 气温、湿度对空气污染的关联影响 |
    | 图5 | 月度污染时段热力分布图 | 识别全年高污染高发季节与时段 |
4. **纯离线轻量化运行**
    无外部数据源依赖，下载源码直接本地执行，自动导出高清PNG图表至项目文件夹。

## 🛠 环境依赖与启动指令
### 1. 一键安装全部依赖库
pip install pandas numpy matplotlib seaborn
### 2.本地运行程序
python 城市天气与空气质量数据分析.py
##### 执行完毕后，程序同级目录自动生成全部可视化图片文件

## 📂 仓库标准文件树
<img width="802" height="174" alt="image" src="https://github.com/user-attachments/assets/3df9ab2d-e20e-480e-ab49-1da7bfbae7d5" />

## 📊 三大数据分析研究维度
<img width="954" height="163" alt="image" src="https://github.com/user-attachments/assets/0861f5a1-49e7-4db6-9b95-bf9c108439d7" />

## 📄 数据来源
全国城市环境空气质量自动监测站公开时序观测数据集

## 开放协议
本项目采用MIT开源协议，支持个人学习，课程数据分析作业，环境相关二次扩展研究，转载与二次开发务必保留本仓库来源链接。
