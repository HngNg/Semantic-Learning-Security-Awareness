import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values

# Path to your CSV file
bob_csv = ['results/MLP_sem_MNIST/Bob_acc_semantic_combining_']
eve_csv = ['results/MLP_sem_MNIST/eve_acc_semantic_combining_']

plt.figure(figsize=(10, 6))
color_cnt = 0
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '#FF5733', '#33FF57', '#5733FF', '#33FFC3' ]

#Bob
# for snr_ in range (3, 11):
snr = []
train_acc = []
train_loss = []
train_psnr = []
for snr_ in range (-5, 21, 5):
    for file_name in bob_csv:
        with open(file_name + str(snr_) + ".csv", 'r') as file:
            csv_reader = csv.reader(file)
            cnt = 0
            snr.append(snr_)
            rows = []
            for row in csv_reader:
                rows.append(row)
            last_row = rows[-5]
            if row and ("acc" in file_name):
                epoch_info = last_row[0]
                train_accuracy__ = float(epoch_info)
                train_acc.append(train_accuracy__)
                
        
plt.plot(snr, train_acc, label='Bob - Accuracy', marker='o', color = colors[color_cnt])
color_cnt+=1
    # plt.plot(epochs, train_loss, label='Bob - Loss, SNR ' + str(snr_), marker='o')
    # plt.plot(epochs, train_psnr, label='Bob - Train PSNR', marker='o')

#Eve
# for snr_ in range (3, 11):
snr = []
train_acc = []
train_loss = []
train_psnr = []

for snr_ in range (-5, 21, 5):
    for file_name in eve_csv:
        with open(file_name + str(snr_) + ".csv", 'r') as file:
            csv_reader = csv.reader(file)
            cnt = 0
            snr.append(snr_)
            rows = []
            for row in csv_reader:
                rows.append(row)
            last_row = rows[-5]
            if row and ("acc" in file_name):
                epoch_info = last_row[0]
                train_accuracy__ = float(epoch_info)
                train_acc.append(train_accuracy__)
                
# train_acc = [0.098697,0.098681,0.100213,0.105061,0.124967,0.171042]
plt.plot(snr, train_acc, label='Eve - Accuracy', marker='o', color = colors[color_cnt])
color_cnt+=1
    # plt.plot(epochs, train_loss, label='Eve - Loss, SNR ' + str(snr_), marker='o')
    # plt.plot(epochs, train_psnr, label='Eve - Train PSNR', marker='o')

                    
# Create the accuracy plot



# Add labels and a legend
plt.xlabel('SNR')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over SNR')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
