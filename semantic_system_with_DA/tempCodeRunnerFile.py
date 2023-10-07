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