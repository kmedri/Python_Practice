def open_dataset(file_name='AppleStore.csv', header=True):
    '''
    Opens a .csv file.

    Args:
        file_name (str, optional): Name of .csv file to open. Defaults to 'AppleStore.csv'.
        header (bool, optional): Has a header or not. Defaults to True.

    Returns:
        Lists: Opens the .csv file and converts to a list or list of lists
    '''          
    opened_file = open(file_name, encoding="utf8")
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    # Left this in to create two datasets if header is True.
    if header:
        return data[1:], data[0]
    else:
        return data
  
def explore_data(dataset, start, end, rows_and_columns=False):
    '''
    Explores a data set and returns a slice of the data. If rows and columns is set to True will return the number of rows and columns.

    Args:
        dataset (variable): Name of variable holding the data.
        start (int): Index of first row to slice.
        end (int): Index of last row to slice.
        rows_and_columns (bool, optional): Set to True if the data has a header. Defaults to False.
    '''
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
apple_data, apple_data_header = open_dataset()
apple_data_header
explore_data(apple_data, 0, 4, rows_and_columns=True)

print('header:', apple_data_header)
print(apple_data[0:2])