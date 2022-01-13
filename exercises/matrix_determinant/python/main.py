from copy import copy, deepcopy

def get_dim():
    # Get number of rows and columns from user
    while (True):
        try:
            dim = int(input("Enter number of rows/columns: "))
            if (dim <= 0):
                raise ValueError
            break
        except ValueError:
            print("Please enter positive integer")
    return dim

# Gets a real-valued square matrix from the user
def get_square_matrix():
    dim = get_dim()

    # Get matrix values
    matrix = []
    print("Enter entries rowwise with enters in between: ")

    for i in range(dim):
        print("Row %d:" %(i+1))
        row = []
        while (len(row) < dim):
            try:
                row.append(float(input()))
            except ValueError:
                print("Please enter real numbers")
        matrix.append(row)

    return matrix

# Computer the determinant of a real-valued square matrix
def det(matrix):
    dim = len(matrix)
    if (dim == 1):
        return matrix[0][0]
    else:
        ret = 0
        for i in range(dim):
            ret += ((-1) ** i) * matrix[0][i] * det(first_minor(matrix,0,i))
        return ret

# Returns a copy of the inputted matrix with the specified row and column removed
def first_minor(matrix,r,c):
    matrix_copy = deepcopy(matrix)
    del matrix_copy[r]
    for i in range(len(matrix_copy)):
        del matrix_copy[i][c]
    return matrix_copy

# Prints the given matrix (from https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python/36538558)
def print_matrix(matrix):
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))

# Main
if __name__ == '__main__':
    matrix = get_square_matrix()
    print("The determinant of\n")
    print_matrix(matrix)
    print("\nis %.2f" % det(matrix))