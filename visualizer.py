import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []
eval_acc = []

# Path to your CSV file
csv_file = 'results/MLP_sem_MNIST/loss_semantic_combining_1.csv'

# Read the CSV file and extract data
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row:
            epoch_number = int(row[0].split(': ')[1])
            train_accuracy = float(row[2].split(': ')[1])
            eval_accuracy = float(row[3].split(': ')[1])
            
            # Append data to the lists
            epochs.append(epoch_number)
            train_acc.append(train_accuracy)
            eval_acc.append(eval_accuracy)

# Create the accuracy plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_acc, label='Train Accuracy', marker='o')
plt.plot(epochs, eval_acc, label='Eval Accuracy', marker='o')

# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
