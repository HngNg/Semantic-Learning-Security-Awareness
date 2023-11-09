import matplotlib.pyplot as plt
import csv

# Initialize lists to store epoch and accuracy values
epochs = []
train_acc = []
train_loss = []
train_psnr = []

# Path to your CSV file
cifar_csv = ['semantic_extraction/CIFAR/MLP_sem_CIFAR/acc_semantic_combining_0.10_lambda_0.90', 
           'results/MLP_sem_MNIST/cifar_loss_semantic_combining_']

eve_csv = ['results/MLP_sem_MNIST/eve_acc_semantic_combining_',
           'results/MLP_sem_MNIST/eve_loss_semantic_combining_']

plt.figure(figsize=(10, 6))
color_cnt = 0
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '#FF5733', '#33FF57', '#5733FF', '#33FFC3' ]

#cifar
# for snr_ in range (3, 11):
for snr_ in range (-5, 21, 5):
# for cr in range (1, 10):
    epochs = []
    train_acc = []
    train_loss = []
    train_psnr = []
    for file_name in cifar_csv:
        with open('semantic_extraction/CIFAR/MLP_sem_CIFAR/acc_semantic_combining_1.00_lambda_0.00' + ".csv", 'r') as file:
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
        
    plt.plot(epochs, train_acc, marker='o')
    # plt.plot(epochs, train_loss, label='cifar - Loss, SNR ' + str(snr_), marker='o')
    # plt.plot(epochs, train_psnr, label='cifar - Train PSNR', marker='o')


# Add labels and a legend
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
