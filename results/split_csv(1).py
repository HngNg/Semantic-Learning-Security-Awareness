import pandas as pd
df = pd.read_csv('results/training_output.csv')
lines_per_file = 103  # Number of lines per smaller file
num_files = 8

for i in range(num_files):
    start_idx = i * lines_per_file
    end_idx = (i + 1) * lines_per_file
    smaller_df = df.iloc[start_idx:end_idx]
    smaller_df.to_csv(f'training_outcome_{i+3}.csv', index=False)
