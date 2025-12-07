import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler

# Function to extract all battery capacities into a single DataFrame
def getAllBatteryCapacities(batteries_dict):

    all_dfs = []
    
    for battery_name, battery_data in batteries_dict.items():
        cycle = []
        capacity = []
        i = 1        
        for Bat in battery_data:
            if Bat['cycle_type'] == 'discharge':
                cycle.append(i)
                capacity.append(Bat['data']['Capacity'][0])
                i += 1
        
        # Create DataFrame for this battery with batteryID column
        df = pd.DataFrame({
            'cycle number': cycle, 
            'capacity': capacity,
            'batteryID': battery_name
        })
        all_dfs.append(df)
    
    # Combine all into single DataFrame
    return pd.concat(all_dfs, ignore_index=True)

# Function to compute RUL for a single battery cell DataFrame
def compute_rul_for_cell(df_cell, eol_threshold):
    # sort by cycle to be safe
    df_cell = df_cell.sort_values('cycle number').copy()

    # find first cycle where SOH < threshold
    below = df_cell['SOH'] < eol_threshold
    if below.any():
        N_eol = df_cell.loc[below, 'cycle number'].iloc[0]
    else:
        # never reaches EOL in this record; you can choose convention
        N_eol = df_cell['cycle number'].max()

    # compute RUL_k = N_eol - k
    df_cell['RUL'] = N_eol - df_cell['cycle number']
    return df_cell

# Function to get charging values for plotting or analysis
def getChargingValues(batteries_dict, battery_name, cycle_index):

    Battery = batteries_dict[battery_name][cycle_index]['data']
    index = list(range(1, len(Battery['Voltage_measured']) + 1))
    
    return [index, Battery['Voltage_measured'], Battery['Current_measured'], 
            Battery['Temperature_measured'], Battery['Voltage_charge'], Battery['Time']]

# Function to get discharging values for plotting or analysis
def getDischargeValues(batteries_dict, battery_name, cycle_index):

    Battery = batteries_dict[battery_name][cycle_index]['data']
    index = list(range(1, len(Battery['Voltage_measured']) + 1))
    
    return [index, Battery['Voltage_measured'], Battery['Current_measured'], 
            Battery['Temperature_measured'], Battery['Voltage_load'], Battery['Time']]

