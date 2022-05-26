n = int(input())
ld = [0 for _ in range(2*n)]
rd = [0 for _ in range(2*n)]
cl = [0 for _ in range(2*n)]

def find_right_solution(board, column):
    if column >= n:
        return True

    for i in range(n):
        if (ld[i - column + n - 1] != 1 and rd[i + column] != 1) and cl[i] != 1:
            board[i][column] = 1
            ld[i - column + n - 1] = rd[i + column] = cl[i] = 1

            if find_right_solution(board, column + 1):
                return True

            board[i][column] = 0
            ld[i - column + n - 1] = rd[i + column] = cl[i] = 0

    return False

board = [[0 for _ in range(n)] for _ in range(n)]
result = find_right_solution(board, 0)

if result:
    for i in board:
        print(*i)
else:
    print(result)
