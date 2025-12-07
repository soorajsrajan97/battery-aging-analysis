import matplotlib.pyplot as plt
import seaborn as sns
import batteryData



def degradation_capacity_plot(batterycapacity, yvalue, xlabel,ylabel, title):
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot using seaborn with hue for battery_id (automatic color assignment)
    sns.lineplot(data = batterycapacity, x ='cycle number', y =yvalue, hue ='batteryID', linewidth = 2, ax = ax)

    # Set axis labels and title with larger, readable fonts
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15)
    ax.set_title(title, fontsize=17, fontweight='bold')

    # Show grid, legend with frame
    ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
    ax.legend(title="Cell ID", fontsize=13, title_fontsize=14, loc='best', frameon=True)

    plt.tight_layout()
    plt.show()

def quickPlotAll(batteries_dict):
    """Ultra-compact plotting"""
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    titles = ['Voltage', 'Current', 'Temperature', 'Voltage Charge']
    
    for i, battery in enumerate(batteries_dict):
        data = batteryData.getChargingValues(batteries_dict, battery, 0)
        idx, V, I, T, Vc, _ = data
        
        axs[0,0].plot(idx, V, label=battery)
        axs[0,1].plot(idx, I)
        axs[1,0].plot(idx, T) 
        axs[1,1].plot(idx, Vc)
    
    for ax, title in zip(axs.flat, titles):
        ax.set_title(title)
        ax.set_xlabel('Time Index')
    
    axs[0,0].legend()
    plt.tight_layout()
    plt.show()
