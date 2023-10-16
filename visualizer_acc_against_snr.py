import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []

plt.figure(figsize=(10, 10))
for snr_ in range (3, 4):
    csv_file = 'results/training_outcome_' + str(snr_) + '.csv'
    # Read the CSV file and extract data
    cnt = 0
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cnt += 1
            content = row[0].split(", ")
            if content and cnt > 3:
                try:
                    epoch_number = int(content[0].split(': ')[1])
                    train_accuracy = float(content[2].split(': ')[1])
                    
                    # Append data to the lists
                    epochs.append(epoch_number)
                    train_acc.append(train_accuracy)
                except IndexError: 
                    pass
            
                # print (int(content[0].split(': ')[1]))
                # # print()

    plt.plot(epochs, train_acc, label='SNR = ' + str(snr_), marker='o')
    train_acc = []
    epochs = []

# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
