### Python Lists: Takeaways

#### Creating a list of data points:

`row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]`
`row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]`

#### Creating a list of lists:

`data = [row_1, row_2]`

#### Retrieving an element of a list:

`first_row = data[0]`
`first_element_in_first_row = first_row[0]`
`first_element_in_first_row = data[0][0]`
`last_element_in_first_row = first_row[-1]`
`last_element_in_first_row = data[0][-1]`

#### Retrieving multiple list elements and creating a new list:

`row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]`
`rating_data_only = [row_1[3], row_1[4]]`

#### Performing list slicing:

`pythonrow_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]`
`second_to_fourth_element = row_1[1:4]`

A data point is a value that offers us some information.
A set of data points make up a dataset. 
A table is an example of a dataset.
Lists are data types that can store datasets.
