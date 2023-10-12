import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []

# Create the accuracy plot
plt.figure(figsize=(10, 6))
# Define a colormap for line colors
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple']

for snr_ in range (3, 11):
    # Path to your CSV file
    # csv_file = 'results/acc_svhn_mnist_0.80.csv'
    csv_file = 'results/acc_svhn_mnist_' + str(snr_) + '.csv'
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

    plt.plot(epochs, train_acc, label='SNR = ' + str(snr_), marker='o', color = colors[snr_-3])
    # plt.plot(epochs, train_acc, label='SNR = ' + str(snr_))
    epochs = []
    train_acc = []

# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
