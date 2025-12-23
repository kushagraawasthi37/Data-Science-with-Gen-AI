"""
===========================================================
BOKEH COMPLETE NOTES – SINGLE FILE (REVISION + INTERVIEW)
===========================================================

Author: Kushagra Awasthi
Purpose:
- Learn Bokeh from scratch
- Interview-ready notes
- Web-friendly interactive plots

WHAT IS BOKEH?
-----------------------------------------------------------
Bokeh is a Python INTERACTIVE visualization library
designed mainly for WEB applications.

Bokeh renders plots using HTML + JavaScript
→ very useful for dashboards and browsers.

-----------------------------------------------------------
"""

# =========================
# 1️⃣ IMPORTS
# =========================

from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource
import numpy as np
import pandas as pd

# Use this if running in Jupyter Notebook
output_notebook()

# Use this if running as .py file (browser output)
# output_file("bokeh_output.html")


# =========================
# 2️⃣ LINE PLOT
# =========================
"""
Use Case:
- Trend analysis
- Time series visualization

Key Points:
- figure() creates the canvas
- line() draws line plot
"""

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

p_line = figure(
    title="Line Plot",
    x_axis_label="X Axis",
    y_axis_label="Y Axis"
)

p_line.line(
    x,
    y,
    line_width=2,
    color="blue",
    legend_label="Trend Line"
)

show(p_line)


# =========================
# 3️⃣ SCATTER PLOT
# =========================
"""
Use Case:
- Relationship between variables
- Correlation visualization
"""

p_scatter = figure(
    title="Scatter Plot",
    x_axis_label="X",
    y_axis_label="Y"
)

p_scatter.circle(
    x,
    y,
    size=10,
    color="red",
    alpha=0.6
)

show(p_scatter)


# =========================
# 4️⃣ BAR CHART
# =========================
"""
Use Case:
- Category comparison
IMPORTANT:
Bokeh bars need categorical x-axis
"""

categories = ["A", "B", "C"]
values = [10, 20, 30]

p_bar = figure(
    x_range=categories,
    title="Bar Chart",
    y_axis_label="Values"
)

p_bar.vbar(
    x=categories,
    top=values,
    width=0.5,
    color="green"
)

show(p_bar)


# =========================
# 5️⃣ HISTOGRAM
# =========================
"""
Use Case:
- Data distribution
- Frequency analysis
"""

data = np.random.randn(1000)

hist, edges = np.histogram(data, bins=30)

p_hist = figure(
    title="Histogram",
    x_axis_label="Value",
    y_axis_label="Frequency"
)

p_hist.quad(
    top=hist,
    bottom=0,
    left=edges[:-1],
    right=edges[1:],
    fill_color="purple",
    line_color="white",
    alpha=0.7
)

show(p_hist)


# =========================
# 6️⃣ BOX PLOT (MANUAL)
# =========================
"""
NOTE:
Bokeh does NOT have built-in boxplot
We manually compute quartiles

Interview Tip:
This shows low-level control of Bokeh
"""

data = np.array([1, 2, 3, 4, 100])

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)  # median
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

p_box = figure(title="Box Plot", x_range=["Data"])

# Box
p_box.vbar(x=["Data"], width=0.5, top=q3, bottom=q1)

# Median line
p_box.segment(
    x0=["Data"], y0=q2,
    x1=["Data"], y1=q2,
    line_width=2
)

# Whiskers
p_box.segment(x0=["Data"], y0=upper, x1=["Data"], y1=q3)
p_box.segment(x0=["Data"], y0=lower, x1=["Data"], y1=q1)

show(p_box)


# =========================
# 7️⃣ PANDAS + BOKEH
# =========================
"""
Real-world usage:
- DataFrames with ColumnDataSource
"""

df = pd.DataFrame({
    "Year": [2020, 2021, 2022],
    "Sales": [100, 200, 300]
})

source = ColumnDataSource(df)

p_df = figure(
    title="Bokeh with Pandas",
    x_axis_label="Year",
    y_axis_label="Sales"
)

p_df.line(
    x="Year",
    y="Sales",
    source=source,
    line_width=2,
    color="orange"
)

show(p_df)


# =========================
# 8️⃣ MULTIPLE PLOTS (LAYOUT)
# =========================
"""
Bokeh layouts:
- row()
- column()
Used heavily in dashboards
"""

layout = row(p_line, p_scatter)
show(layout)


# =========================
# 9️⃣ INTERVIEW QUICK NOTES
# =========================
"""
BOKEH HIGHLIGHTS:
- Web-first visualization library
- Interactive by default
- Uses HTML + JavaScript
- Excellent for dashboards

Bokeh vs Matplotlib:
- Bokeh → interactive, web-based
- Matplotlib → static, research-focused

Bokeh vs Plotly:
- Bokeh → Python-centric, server-based
- Plotly → JS + Python, easier charts

Common Interview Question:
Q: Why Bokeh?
A: When building interactive browser-based dashboards in Python.
"""

print("✅ Bokeh complete notes executed successfully!")