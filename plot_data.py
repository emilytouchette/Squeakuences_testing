import matplotlib.pyplot as plt
import pandas as pd

# Create a pandas dataframe from a .tsv file (read .tsv into a dataframe)

df = pd.read_csv("/scratch/touchete/Final_Project/Squeakuences_testing/data.tsv", delimiter='\t')


# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df["Cores Used"], df["Processing Time (hours)"], marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Processing Time vs. Number of Cores Used')
plt.xlabel('Cores Used')
plt.ylabel('Processing Time (hours)')
plt.grid(True)
plt.xticks(df["Cores Used"])  # Ensure x-ticks match the number of cores
plt.savefig("processing_time_vs_cores_used.pdf")
plt.show()
