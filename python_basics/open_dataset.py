# opens dataset w/header
def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:  # if data has a header, opens data with header, else returns with no header
        return data[1:], data[0]
    else:
        return data


all_data = open_dataset()  # opens dataset
header = all_data[1]  # opens just the headers
apps_data = all_data[0]  # opens just the data
