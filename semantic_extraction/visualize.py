import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []
train_loss = []
train_psnr = []

# Path to your CSV file
csv_file_1 = 'results/MLP_sem_MNIST/acc_semantic_combining_0.100000.csv'
csv_file_2 = 'results/MLP_sem_MNIST/loss_semantic_combining_0.100000.csv'
csv_file_3 = 'results/MLP_sem_MNIST/psnr_semantic_combining_0.100000.csv'

cnt1 = 0
cnt2 = 0
cnt3 = 0

# Read the CSV file and extract data
with open(csv_file_1, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # if cnt > 1: break
        # cnt += 1
        if row:
            # Split the row by commas and extract relevant information
            epoch_info = row[0]
            epoch_number = cnt1 
            train_accuracy__ = float(epoch_info)
            cnt1 += 1

            # Append data to the lists
            epochs.append(epoch_number)
            train_acc.append(train_accuracy__)

with open(csv_file_2, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # if cnt > 1: break
        # cnt += 1
        if row:
            # Split the row by commas and extract relevant information
            epoch_info = row[0]
            train_loss__ = float(epoch_info)
            cnt2 += 1

            # Append data to the lists
            train_loss.append(train_loss__)

with open(csv_file_3, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # if cnt > 1: break
        # cnt += 1
        if row:
            # Split the row by commas and extract relevant information
            epoch_info = row[0]
            train_psnr__ = float(epoch_info)
            cnt3 += 1

            # Append data to the lists
            train_psnr.append(train_psnr__)

# Create the accuracy plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_acc, label='Train Accuracy', marker='o')
# plt.plot(epochs, train_loss, label='Train Loss', marker='o')
# plt.plot(epochs, train_psnr, label='Train PSNR', marker='o')

# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
