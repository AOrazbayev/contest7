def _print(matrix, N):
    for i in range(N):
        print(*matrix[i])
    print()


def bubble_sort2d(matrix, N, M):
    _print(matrix, N)
    for i in range(N*M - 1):
        for j in range(N*M - i - 1):
            current_row = j // M
            current_column = j % M
            next_row = (j+1) // M
            next_column = (j+1) % M
            if matrix[current_row][current_column] > matrix[next_row][next_column]:
                matrix[current_row][current_column], matrix[next_row][next_column] = matrix[next_row][next_column], matrix[current_row][current_column]
                _print(matrix, N)


bubble_sort2d([[0, 3, 4], [1, 0, 2]], 2, 3)
