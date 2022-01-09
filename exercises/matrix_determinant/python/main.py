from copy import copy, deepcopy

# Gets a real-valued square matrix from the user
def get_square_matrix():
    # Get number of rows and columns from user
    while (True):
        try:
            dim = int(input("Enter number of rows/columns: "))
            if (dim <= 0):
                raise Exception
            break
        except:
            print("Please enter positive integer")

    # Get matrix values
    matrix = []
    print("Enter entries rowwise: ")

    for i in range(dim):
        row = []
        while (True):
            try:
                for j in range(dim):
                    row.append(float(input()))
                break
            except:
                print("Please enter real numbers")
        matrix.append(row)

    return matrix

# Computer the determinant of a real-valued square matrix
def det(matrix):
    dim = len(matrix)
    if (dim == 1):
        return matrix[0][0]
    elif (dim == 2):
        return (matrix[0][0] * matrix [1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        ret = 0
        for i in range(dim):
            ret += ((-1) ** i) * matrix[0][i] * det(remove_row_col(matrix,1,i+1))
        return ret

# Removes the specified row and column from the given matrix
def remove_row_col(matrix,r,c):
    matrix_copy = deepcopy(matrix)
    del matrix_copy[r-1]
    for i in range(len(matrix_copy)):
        del matrix_copy[i][c-1]
    return matrix_copy

# Prints the given matrix
def print_matrix(matrix):
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                     for row in matrix]))

# Main
if __name__ == '__main__':
    matrix = get_square_matrix()
    print("The determinant of\n")
    print_matrix(matrix)
    print("\nis %.2f" % det(matrix))