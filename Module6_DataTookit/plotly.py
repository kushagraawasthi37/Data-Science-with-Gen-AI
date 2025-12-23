"""
===========================================================
PLOTLY COMPLETE NOTES – SINGLE FILE (REVISION + INTERVIEW)
===========================================================

Author: Kushagra Awasthi
Purpose:
- Learn Plotly from scratch
- Quick revision before interviews
- Ready-to-use examples for projects

IMPORTANT:
Plotly is an INTERACTIVE visualization library.
Charts support zoom, pan, hover, export automatically.

-----------------------------------------------------------
"""

# =========================
# 1️⃣ IMPORTS
# =========================

import plotly.express as px          # High-level API (fast, simple)
import plotly.graph_objects as go   # Low-level API (full control)
import pandas as pd
import numpy as np


# =========================
# 2️⃣ LINE PLOT
# =========================
"""
Use Case:
- Trend analysis
- Time-series data
"""

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

fig_line = px.line(
    x=x,
    y=y,
    title="Line Plot",
    labels={"x": "X Axis", "y": "Y Axis"}
)
fig_line.show()


# =========================
# 3️⃣ SCATTER PLOT
# =========================
"""
Use Case:
- Relationship between two variables
- Correlation detection
"""

fig_scatter = px.scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    size=[10, 20, 30, 40],  # bubble size
    color=[1, 2, 3, 4],    # color mapping
    title="Scatter Plot"
)
fig_scatter.show()


# =========================
# 4️⃣ BAR CHART
# =========================
"""
Use Case:
- Category comparison
- Aggregated values
"""

fig_bar = px.bar(
    x=["A", "B", "C"],
    y=[10, 20, 30],
    title="Bar Chart"
)
fig_bar.show()


# =========================
# 5️⃣ PIE CHART
# =========================
"""
Use Case:
- Percentage contribution
- Avoid if categories > 5
"""

fig_pie = px.pie(
    names=["Apple", "Banana", "Mango"],
    values=[30, 40, 30],
    title="Pie Chart"
)
fig_pie.show()


# =========================
# 6️⃣ HISTOGRAM
# =========================
"""
Use Case:
- Distribution of data
- Skewness & outliers
"""

data = np.random.randn(1000)

fig_hist = px.histogram(
    data,
    nbins=30,
    title="Histogram"
)
fig_hist.show()


# =========================
# 7️⃣ BOX PLOT
# =========================
"""
Use Case:
- Outlier detection
- Median & quartiles
"""

fig_box = px.box(
    y=[1, 2, 3, 4, 100],
    title="Box Plot"
)
fig_box.show()


# =========================
# 8️⃣ 3D SCATTER PLOT
# =========================
"""
Use Case:
- 3-variable relationship
- ML visualization
"""

fig_3d = px.scatter_3d(
    x=[1, 2, 3],
    y=[4, 5, 6],
    z=[7, 8, 9],
    title="3D Scatter Plot"
)
fig_3d.show()


# =========================
# 9️⃣ GRAPH OBJECTS (ADVANCED)
# =========================
"""
Graph Objects give FULL control.
Used in dashboards and production apps.
"""

fig_go = go.Figure()

fig_go.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[10, 20, 30],
        mode="lines+markers",
        name="Sales Trend"
    )
)

fig_go.update_layout(
    title="Graph Objects Example",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    template="plotly_dark",  # styling
    width=800,
    height=400
)

fig_go.show()


# =========================
# 🔟 PLOTLY WITH PANDAS
# =========================
"""
Most common real-world usage
"""

df = pd.DataFrame({
    "Year": [2020, 2021, 2022],
    "Sales": [100, 200, 300]
})

fig_df = px.line(
    df,
    x="Year",
    y="Sales",
    title="Plotly with Pandas DataFrame"
)
fig_df.show()


# =========================
# 1️⃣1️⃣ SAVE PLOTLY FIGURES
# =========================
"""
HTML → Interactive
PNG → Static (needs kaleido)
"""

# fig_df.write_html("plotly_chart.html")
# fig_df.write_image("plotly_chart.png")  # pip install kaleido


# =========================
# 1️⃣2️⃣ INTERVIEW QUICK NOTES
# =========================
"""
Plotly Highlights:
- Interactive charts
- Browser-based rendering
- Supports 2D, 3D, animation
- Ideal for dashboards & analytics apps

Plotly Express:
- One-line plots
- Rapid EDA

Graph Objects:
- Fine-grained control
- Production dashboards

Common Interview Question:
Q: Why Plotly over Matplotlib?
A: Plotly supports interaction, web integration, and dashboards.
"""

print("✅ Plotly complete notes executed successfully!")
