import pandas as pd
df = pd.read_csv('results/MLP_sem_MNIST/Training_for_Eve.csv')
lines_per_file = 100  # Number of lines per smaller file
num_files = 6

for i in range(num_files):
    start_idx = i * lines_per_file
    end_idx = (i + 1) * lines_per_file
    smaller_df = df.iloc[start_idx:end_idx]
    smaller_df.to_csv(f'Eve_outcome{-5 + 5*i}.csv', index=False)
