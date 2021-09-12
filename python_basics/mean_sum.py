from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

# Method to grab column in dataset, and append to an empty list


def extract(data_set, index):
    column = []

    for row in data_set[1:]:
        # For each row in the dataset (excluding the header), assign to the variable called "value"
        value = row[index]
        column.append(value)  # Append the data in the variable "value"
    return column

# Calculate the sum of a list


def find_sum(a_list):
    a_sum = 0
    for element in a_list:  # Iterate through each row of the list
        # For each row, add the numbers together and convert to a float type
        a_sum += float(element)
    return a_sum

# Calculate the length


def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

# Calculate the mean based on the dataset and index. Execute the find_sum and find_length methods


def mean(data, index_v):
    mean_list = extract(data, index_v)
    return find_sum(mean_list) / find_length(mean_list)


avg_price = mean(apps_data, 4)
