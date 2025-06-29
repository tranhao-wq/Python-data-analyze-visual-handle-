![image](https://github.com/user-attachments/assets/023c99e2-fbf5-48d1-9cf9-a6f75af3c8fd)# Data Visualization Project

This project is a collection of Python scripts that demonstrate various types of data visualizations using `matplotlib`, `geopandas`, and other libraries. Each script is designed to showcase a specific chart or plot type, along with example data and use cases. The project is organized for easy exploration and extension.
## Pics
![image](https://github.com/user-attachments/assets/a88ac727-1b11-4c04-9310-1abf4f12d47b)
![image](https://github.com/user-attachments/assets/d99ff8b7-f263-462f-b062-580702d29806)
![image](https://github.com/user-attachments/assets/7b7950f8-ba13-4fff-b49d-937ece487747)
![image](https://github.com/user-attachments/assets/efcf7784-624f-41e5-ab98-e861b104a1f3)
![image](https://github.com/user-attachments/assets/96d0f5af-ec65-4989-b29e-68549e7cd029)
![image](https://github.com/user-attachments/assets/c6f44524-26ce-47d3-8486-28b283f7f2c8)
![image](https://github.com/user-attachments/assets/c2830177-f5a7-49e7-8e6c-f89eac609596)
![image](https://github.com/user-attachments/assets/10b2d9a1-5329-4833-820d-24b5b519e6f6)
![image](https://github.com/user-attachments/assets/b1226840-7e08-4500-af0d-2135c4974621)
![image](https://github.com/user-attachments/assets/8739b6cb-be7f-4e1c-8cd3-ff4ef06b8040)
![image](https://github.com/user-attachments/assets/e3885ed0-b598-49ee-9aac-8095cf4bd7aa)
![image](https://github.com/user-attachments/assets/a45c317c-3a22-4717-917e-ed2c6ab07aee)
![image](https://github.com/user-attachments/assets/145e1413-c7f8-454c-b49b-53f229e82f73)
![image](https://github.com/user-attachments/assets/ee21d4a6-1492-48b4-a87d-6c81f4261571)
![image](https://github.com/user-attachments/assets/ddfc7194-f8ad-4a78-b702-93717f3239c6)
![image](https://github.com/user-attachments/assets/9d7463bb-ac38-4c42-a021-524f639fee88)
![image](https://github.com/user-attachments/assets/bba950e9-276f-4bb1-b6af-f04f3ba1dcce)
![image](https://github.com/user-attachments/assets/9e93e11b-9314-4338-8aa0-6dabc25fec23)
![image](https://github.com/user-attachments/assets/52a996dd-80e4-46eb-bcc6-8b502b819d7d)
![image](https://github.com/user-attachments/assets/243f66e8-33ee-473e-8ae8-699972f7ed77)
![image](https://github.com/user-attachments/assets/1b79000d-f329-421d-9878-896dd46d70bb)
![image](https://github.com/user-attachments/assets/b1e4cd2d-2cf3-4ef6-896d-74fcab17a793)
![image](https://github.com/user-attachments/assets/b51e483e-c4c5-4754-9583-a95c056b7f12)
![image](https://github.com/user-attachments/assets/86b1c89c-c3e1-429c-83fa-386afbecbf1c)
![image](https://github.com/user-attachments/assets/0d9671b1-4474-47d8-bb2a-8ab930b42afe)
![image](https://github.com/user-attachments/assets/618898e4-b82f-410d-af95-3bfd250b7fe1)

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
