# 🌦️ Weather Forecast Dashboard (Streamlit)
## 🧭 Project Overview
An interactive Streamlit dashboard that visualises temperature data collected from multiple campus areas, enabling quick comparison through charts and dashboard summaries.

## 🎯 Objective
This project aims to represent temperature data gathered from environmental sensors in an intuitive and analytical way. It allows users to explore, compare, and interpret weather conditions across different campus locations using **interactive charts** and **CSV-based data integration**.

## 🧠 Key Features
1. 📊 **Interactive Dashboard** – Displays temperature data in charts and tables.
2. 🧩 **Multiple Visualization Modes** – Users can navigate between Dashboard, Pie Chart, Bar Chart, and Area views.
3. 🌍 **Area-Based Analysis** – Temperature readings categorized by campus zones:
         a. SPCAI
         b. A2 Block
         c. STC
         d. Hostel
5. 📈 **CSV Data Processing** – Reads data from CSV files and visualizes results dynamically.
6. 🧭 **User-Friendly Navigation** – Sidebar with navigation tabs for effortless exploration.

## 🧩 Project Workflow
1. **Data Collection:**
   Temperature readings are collected through sensors installed in four university areas.

2. **Data Storage:**
   The readings are stored in a structured CSV file, containing records of temperature values for each area.

3. **Data Visualization:**
   Using **Streamlit** and **Pandas**, the dashboard processes the CSV data and presents it through:

   1. Bar charts for area-wise comparisons
   2. Pie charts for distribution analysis
   3. Dashboard summary for overall insights

4. **Analysis:**
   Users can easily identify temperature variations and compare readings across all areas.

## 🏗️ System Architecture
- **Data layer:** CSV file(s) (e.g., `Weather_Forecast/sensor_data.csv`)
- **Processing:** Python modules for reading/transforming data
- **Visualisation:** Streamlit UI + charts (`Charts.py`)
- **Navigation:** Sidebar/menu routing via `Menu.py`

**Architecture flow (text):**  
`Sensor CSV → Python Processing → Streamlit UI → Charts/Insights`

## 🧰 Technologies & Tools
**Languages & Libraries:**
'Python', 'Streamlit', 'Pandas', 'Matplotlib'
**Development & Deployment Tools:**
'VS Code', 'GitHub'
**Data Handling:**
'CSV' 'Kaggle Datasets'

## ⚙️ Installation and Setup

### 1) Clone
```bash
git clone https://github.com/HamnaIqbal44/Weather-Forecast-Dashboard.git
cd Weather-Forecast-Dashboard
```

### 2) Create and activate a virtual environment
```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

### 3) Install dependencies
> This repository currently does not include a `requirements.txt`.  
> Option A (recommended): create `requirements.txt` and install from it.  
> Option B (quick start): install minimal dependencies directly.

**Option B (quick start)**
```bash
pip install streamlit pandas plotly
```

### 4) Run the Streamlit app (actual entrypoint)
```bash
streamlit run Weather_Forecast/main.py
```

## 🗃️ Dataset
- Primary dataset file: `Weather_Forecast/sensor_data.csv`

## 🧪 Usage / Demo
1. Run the Streamlit app.
2. Use the sidebar/menu to switch views.
3. Compare area-wise temperature patterns and trends.

   
## 👩‍💻 Author
**Hamna Iqbal**
