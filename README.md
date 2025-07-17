# 🎵 K-pop Comeback Performance Dashboard

A data analytics and visualization project analyzing the digital performance of K-pop comebacks from top JYP artists using both Power BI and a fully coded Streamlit dashboard.

---

## 📁 Dataset

Simulated data representing 50+ comebacks from JYP artists including **TWICE**, **Stray Kids**, **ITZY**, **NMIXX**, **DAY6**, and **Xdinary Heroes**.

### Fields Included:
- Artist  
- MV Title  
- Comeback Date  
- Day (1 to 7)  
- YouTube Views  
- Spotify Streams  
- Country  
- Engagement Score (calculated as likes/comments to views ratio)

📦 **Main file**: `kpop_comeback_day_by_day.csv`

---

## 📊 Power BI Dashboard

A visually rich, interactive dashboard built in **Power BI Desktop** for business storytelling and music performance insights.

### ✅ Features:
- 📈 **Line Chart**: Day-by-day YouTube and Spotify view trends per artist  
- 🎯 **KPI Cards**: Total Streams, Max Engagement Score, Top Artist  
- 📍 **Pie Chart**: Country-wise fanbase engagement  
- 🔥 **Heatmap**: Artist × Day view intensity  
- 🎛️ **Filters**: Artist, Country, MV Title, Date Range

💡 Used to simulate **real-world business insights** for music labels on fan trends, artist performance, and streaming behaviors.

---

## 💻 Streamlit Dashboard (Python + Plotly)

A fully coded, interactive web app version of the dashboard — ideal for technical analysis and deployment.

 Streamlit Features:
🎚️ Sidebar filters: Artist, Country

📈 Interactive line charts for daily views & streams

📊 Grouped bar chart of total streams per artist

🌍 Pie chart of YouTube fanbase by country

🔁 Real-time interactivity & responsive layout

### 🛠 Technologies Used:
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- Python (pandas)

### ▶️ How to Run:

```bash
pip install streamlit plotly pandas
streamlit run kpop_dashboard_streamlit.py



**"All data is simulated and used for educational or demonstration purposes only. No real artist data was used.**



