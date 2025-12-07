# Battery Aging Analysis

## Overview
This project analyzes battery aging behavior through comprehensive data processing and visualization of battery cycle data. The analysis extracts voltage, current, and capacity metrics from experimental battery test data stored in MATLAB .mat format, enabling detailed performance degradation studies.

## Project Objectives
- Process and analyze battery cycle data from experimental testing
- Extract key electrochemical parameters (voltage, current, capacity) from raw test data
- Visualize battery performance metrics across multiple charge-discharge cycles
- Support battery degradation research and State of Charge (SOC) analysis

## Technical Stack
- **Python 3.x**: Primary programming language
- **MATLAB**: Data source format (.mat files)
- **NumPy**: Numerical computing and array operations
- **Pandas**: Data manipulation and time series analysis
- **Matplotlib**: Data visualization and plotting
- **SciPy**: Scientific computing and .mat file handling

## Key Features
- ✅ MATLAB .mat file parsing and data extraction
- ✅ Battery cycle data processing (voltage, current, time series)
- ✅ Capacity computation from current-time integration
- ✅ Multi-cycle visualization and comparison
- ✅ Automated data analysis pipeline
- ✅ Modular code structure for scalability

## Project Structure
```
battery-aging-analysis/
│
├── Data/                          # Raw battery test data (.mat files)
├── BatteryAnalysis_main.ipynb     # Main Jupyter notebook for analysis
├── batteryData.py                 # Data processing and extraction module
├── batteryPlots.py                # Visualization module
├── mat2csv_all_cycles.mlx         # MATLAB script for data conversion
└── README.md                      # Project documentation
```

## Installation

### Prerequisites
```bash
python >= 3.8
```

### Required Libraries
```bash
pip install numpy pandas matplotlib scipy
```

For Jupyter Notebook support:
```bash
pip install jupyter
```

## Usage

### Basic Analysis
1. Place your battery test data (.mat files) in the `Data/` directory
2. Open the Jupyter notebook:
   ```bash
   jupyter notebook BatteryAnalysis_main.ipynb
   ```
3. Run the cells sequentially to:
   - Load and parse .mat files
   - Extract voltage, current, and time data
   - Compute discharge/charge capacity
   - Generate visualization plots

### Python Module Usage
```python
import batteryData as bd
import batteryPlots as bp

# Load battery cycle data
cycle_data = bd.load_mat_file('Data/battery_cycle.mat')

# Extract parameters
voltage = bd.extract_voltage(cycle_data)
current = bd.extract_current(cycle_data)

# Compute capacity
capacity = bd.compute_capacity(current, time)

# Visualize results
bp.plot_voltage_profile(voltage, time)
bp.plot_capacity_fade(capacity_values, cycle_numbers)
```

## Analysis Capabilities

### Data Extraction
- Parse MATLAB .mat structured arrays
- Extract voltage, current, temperature, and time data
- Handle multiple cycles within single data file

### Capacity Analysis
- Coulomb counting (current integration over time)
- Charge/discharge capacity separation
- Coulombic efficiency calculation

### Visualization
- Voltage vs. time profiles
- Current vs. time profiles
- Capacity fade over cycle number
- Voltage-capacity curves (dQ/dV analysis)

## Example Results
The analysis generates comprehensive plots including:
- Individual cycle voltage profiles
- Capacity retention curves
- Cycle-to-cycle comparison
- Statistical performance metrics

## Applications
- Battery degradation research
- State of Charge (SOC) estimation
- Battery Management System (BMS) development
- Electrochemical modeling validation
- Battery aging mechanism studies

## Future Development
- [ ] Implement advanced SOC estimation algorithms
- [ ] Add machine learning models for degradation prediction
- [ ] Integrate PyBaMM for physics-based modeling
- [ ] Expand support for additional data formats
- [ ] Add automated report generation
- [ ] Implement real-time data streaming analysis

## About
This project was developed as part of battery systems research in Clean Energy Processes. It demonstrates practical data analysis skills applicable to battery technology, energy storage systems, and electrochemical engineering.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or collaboration opportunities:
- GitHub: [@soorajsrajan97](https://github.com/soorajsrajan97)
- University: Friedrich-Alexander-Universität Erlangen-Nürnberg
- Focus: Battery Systems, Energy Storage, Python Data Analysis

## Acknowledgments
- Battery test data obtained from laboratory experiments
- Analysis techniques based on established electrochemical methods
- Developed for research and educational purposes
