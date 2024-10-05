import numpy as np

# Function to create a 2D array with m rows and n columns
def create_array(m, n):
    return [[] for _ in range(m)]

# Function to populate the array with user input
def populate_array(array, m, n):
    counter = 0
    for _ in range(m * n):
        # Prompt the user for input
        element = int(input('Insert element -> '))
        array[counter].append(element)
        # Move to the next row after filling columns
        if (len(array[counter]) == n):
            counter += 1
    return array

# Function to perform Gauss-Jordan elimination on a matrix
def gauss_jordan_elimination(matrix):
    # Convert the matrix to a numpy array of floats
    mat = np.array(matrix, dtype=float)
    rows, cols = mat.shape
    
    # Loop through each column
    for i in range(min(rows, cols)):
        # Find pivot index
        max_row = np.argmax(np.abs(mat[i:, i])) + i
        if mat[max_row, i] == 0:
            continue  # Skip if the pivot is zero
        
        # Swap the current row with the row containing the largest pivot
        mat[[i, max_row]] = mat[[max_row, i]]
        
        # Normalize the pivot row
        mat[i] /= mat[i, i]
        
        # Eliminate the values above and below the pivot
        for j in range(rows):
            if j != i:
                mat[j] -= mat[j, i] * mat[i]
    
    return mat

# Get matrix dimensions from the user
m = int(input('Insert the number of rows -> '))
n = int(input('Insert the number of cols -> '))

# Create and populate the matrix
matrix = create_array(m, n)
matrix = populate_array(matrix, m, n)

# Perform Gauss-Jordan elimination
reduced_matrix = gauss_jordan_elimination(matrix)

# Print the reduced matrix
print("Reduced Matrix:")
print(reduced_matrix)
