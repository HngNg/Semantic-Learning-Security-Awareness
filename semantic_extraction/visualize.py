import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []
train_loss = []
train_psnr = []

# Path to your CSV file
bob_csv = ['results/MLP_sem_MNIST/Bob_acc_semantic_combining_', 
           'results/MLP_sem_MNIST/Bob_loss_semantic_combining_', 
           'results/MLP_sem_MNIST/Bob_psnr_semantic_combining_']

eve_csv = ['results/MLP_sem_MNIST/eve_acc_semantic_combining_',
           'results/MLP_sem_MNIST/eve_loss_semantic_combining_', 
           'results/MLP_sem_MNIST/eve_psnr_semantic_combining_']

plt.figure(figsize=(10, 6))

#Bob
# for snr_ in range (3, 11):
for snr_ in range (3, 5):
    if (snr_ == 4): snr_ = 10

    epochs = []
    train_acc = []
    train_loss = []
    train_psnr = []
    for file_name in bob_csv:
        with open(file_name + str(snr_) + ".csv", 'r') as file:
            csv_reader = csv.reader(file)
            cnt = 0
            for row in csv_reader:
                if row and ("acc" in file_name):
                    epoch_num = cnt
                    cnt += 1
                    epochs.append(epoch_num)

                    epoch_info = row[0]
                    train_accuracy__ = float(epoch_info)
                    train_acc.append(train_accuracy__)

                if row and ("loss" in file_name):
                    epoch_info = row[0]
                    train_loss__ = float(epoch_info)
                    train_loss.append(train_loss__)

                # if row and ("psnr" in file_name):
                #     epoch_info = row[0]
                #     train_psnr__ = float(epoch_info)
                #     train_acc.append(train_psnr__)
        
    plt.plot(epochs, train_acc, label='Bob - Accuracy, SNR ' +str(snr_), marker='o')
    # plt.plot(epochs, train_loss, label='Bob - Loss, SNR ' + str(snr_), marker='o')
    # plt.plot(epochs, train_psnr, label='Bob - Train PSNR', marker='o')

#Eve
# for snr_ in range (3, 11):
for snr_ in range (3, 5):
    if (snr_ == 4): snr_ = 10

    epochs = []
    train_acc = []
    train_loss = []
    train_psnr = []
    for file_name in eve_csv:
        with open(file_name + str(snr_) + ".csv", 'r') as file:
            csv_reader = csv.reader(file)
            cnt = 0
            for row in csv_reader:
                if row and ("acc" in file_name):
                    epoch_num = cnt
                    cnt += 1
                    epochs.append(epoch_num)

                    epoch_info = row[0]
                    train_accuracy__ = float(epoch_info)
                    train_acc.append(train_accuracy__)

                if row and ("loss" in file_name):
                    epoch_info = row[0]
                    train_loss__ = float(epoch_info)
                    train_loss.append(train_loss__)

                # if row and ("psnr" in file_name):
                #     epoch_info = row[0]
                #     train_psnr__ = float(epoch_info)
                #     train_acc.append(train_psnr__)
        
    plt.plot(epochs, train_acc, label='Eve - Accuracy, SNR ' +str(snr_), marker='o')
    # plt.plot(epochs, train_loss, label='Eve - Loss, SNR ' + str(snr_), marker='o')
    # plt.plot(epochs, train_psnr, label='Eve - Train PSNR', marker='o')

                    
# Create the accuracy plot



# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
