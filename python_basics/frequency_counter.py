# DataQuest - Data Engineering Fundamentals 2
from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

# Method to grab column in dataset, and append to an empty list


def extract(index):
    column = []

    for row in apps_data[1:]:
        # For each row in the dataset (excluding the header), assign to the variable called "value"
        value = row[index]
        column.append(value)  # Append the data in the variable "value"
    return column

# Method to take a list of data, and transform the list into a dict. Count the number of times a value appears w/index and value pairs


def freq_table(freq_list):
    num_dict = {}
    for row in freq_list:  # Iterating through the list.
        # Checking if the row in the list is already in the dict, then adding +1 to the counter, else its a 1.
        if row in num_dict:
            num_dict[row] += 1
        else:
            num_dict[row] = 1
    return num_dict


genres = extract(11)
genres_ft = freq_table(genres)

print(genres_ft)
