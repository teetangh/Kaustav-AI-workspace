# WORK IN PROGRESS
import numpy as np


def main():
    n = int(input("Enter number of nodes"))

    matrix = [[0 for j in range(n)] for i in range(n)]
    print(matrix)

    for i in range(n):
        matrix[i] = [int(i) for i in input().split()]

    # matrix = [list(map(int, input().split())) for i in range(n + 1)]

    print(matrix)

    visited = [False for i in range(n)]
    print(visited)

    s = 0
    visited[s] = True
    current = s
    path = []

    for i in range(0, n):
        best_distance = 99999999
        for j in range(1, n):
            if j != i and visited[j] == False and matrix[i][j] < best_distance:
                current = j
                visited[j] = True
                path.append(j)
                best_distance = matrix[i][j]

    path.append(s)
    print(path)


if __name__ == "__main__":
    main()
