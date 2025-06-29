# Data Visualization Project

This project is a collection of Python scripts that demonstrate various types of data visualizations using `matplotlib`, `geopandas`, and other libraries. Each script is designed to showcase a specific chart or plot type, along with example data and use cases. The project is organized for easy exploration and extension.

## Project Structure

```
PY/
  ani/                # Animation and 3D demo scripts (e.g., FPS demo)
  anima/              # (Reserved for animation scripts)
  animation/          # (Reserved for animation scripts)
  anm/                # (Reserved for animation scripts)
  chart/              # All chart and plot scripts
    bar_chart.py
    box_whisker_plot.py
    bubble_chart.py
    gantt.py
    highlight_table.py
    histogram_chart.py
    line_chart.py
    maps_example.py
    pie_chart.py
    scatter_plot.py
    treemap.py
    waterfall_chart.py
  watch/              # (Reserved for watch/3-body problem scripts)
  Natural_Earth_quick_start/ # Contains shapefiles for map visualizations
```

## Chart & Visualization Scripts

- 📅 **Gantt Chart (`gantt.py`)**
  - Visualizes project schedules over time.
  - Use: Project management and planning.

- 📈 **Line Chart (`line_chart.py`)**
  - Shows trends over time with lines.
  - Use: Tracking stock market performance.

- 🫧 **Bubble Chart (`bubble_chart.py`)**
  - Displays data in bubble size variations (3D data).
  - Use: Comparing social media engagement metrics.

- 🔵 **Scatter Plot (`scatter_plot.py`)**
  - Plots data points on two axes.
  - Use: Analyzing the relationship between variables.

- 📊 **Bar Chart (`bar_chart.py`)**
  - Visualizes data with rectangular bars.
  - Use: Comparing sales across different regions.

- 🥧 **Pie Chart (`pie_chart.py`)**
  - Represents data in circular segments.
  - Use: Displaying market share distribution.

- 📦 **Box & Whisker Plot (`box_whisker_plot.py`)**
  - Summarizes data distribution and outliers.
  - Use: Comparing exam scores across classes.

- 📉 **Histogram Chart (`histogram_chart.py`)**
  - Visualizes data distribution in bins.
  - Use: Understanding age distribution in a survey.

- 🟩 **Highlight Table (`highlight_table.py`)**
  - Tabular data coloring based on values (heatmap).
  - Use: Heatmapping survey responses.

- 🗂️ **Treemap (`treemap.py`)**
  - Hierarchical data with nested rectangles.
  - Use: Displaying file system usage.

- 🎯 **Bullet Chart (`bullet_chart.py`)**
  - Measures performance against a target.
  - Use: Tracking sales performance against quotas.

- 🪜 **Waterfall Chart (`waterfall_chart.py`)**
  - Visualizes sequential cumulative effect.
  - Use: Understanding profit and loss components.

- 🗺️ **Maps (`maps_example.py`)**
  - Geographic data representation on maps.
  - Use: Visualizing population density by area. Requires Natural Earth shapefiles (see below).

## Map Data
- The `maps_example.py` script uses Natural Earth shapefiles located in `Natural_Earth_quick_start/packages/Natural_Earth_quick_start/10m_cultural/`.
- Update the path in the script if your shapefile is located elsewhere.

## Requirements
- Python 3.7+
- matplotlib
- numpy
- geopandas (for maps)
- squarify (for treemaps)

Install all requirements with:
```bash
pip install matplotlib numpy geopandas squarify
```

## Usage
Run any script from the `chart/` directory, for example:
```bash
python chart/bar_chart.py
```

Each script will open a window displaying the corresponding chart or visualization.

---

Feel free to extend this project with your own data or new chart types! 