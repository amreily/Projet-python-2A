import pandas as pd
import matplotlib.pyplot as plt

def plot_cac40_and_mentions(csv_file):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(csv_file)

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot CAC40 Close values (left y-axis) as a line
    ax1.plot(df['Date'], df['Close'], color='blue', label='CAC40 (Close)')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('CAC40 Close', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a second y-axis for Article Count
    ax2 = ax1.twinx()

    # Invert the y-axis for Article Count and plot as bars
    ax2.bar(df['Date'], df['Article Count'], color='orange', alpha=0.6, width=20, label='Article Count')
    ax2.set_ylabel('Article Count', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    ax2.invert_yaxis()

    # Add legends and title
    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
    plt.title('CAC40 Close vs Article Count Over Time')

    # Show the plot
    plt.tight_layout()
    plt.show()

# Call the function with the CSV file name
plot_cac40_and_mentions('jointure_resultat.csv')
