import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []

# Path to your CSV file
csv_file = 'results/acc_svhn_mnist_0.80.csv'

cnt = 0

# Read the CSV file and extract data
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # if cnt > 1: break
        # cnt += 1
        if row:
            # Split the row by commas and extract relevant information
            epoch_info = row[0]
            epoch_number = cnt 
            train_accuracy = float(epoch_info)
            cnt += 1

            # Append data to the lists
            epochs.append(epoch_number)
            train_acc.append(train_accuracy)

# Create the accuracy plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_acc, label='Train Accuracy', marker='o')

# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
