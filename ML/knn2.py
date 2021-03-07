import numpy as np


def distance(X, Y):
    return np.sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)


def main():
    Rn = int(input("Enter number of reference points"))
    Qn = int(input("Enter number of Query points"))
    k = int(input("Enter the value of k"))

    R = []
    for i in range(Rn):
        Xi, Yi = input().split()

        point = (int(Xi), int(Yi))
        R.append(point)

    print(R)
    for i in range(Qn):
        Xi, Yi = input().split()

        point = (int(Xi), int(Yi))
        Q.append(point)

    print(Q)

    distances = []
    for q in Q:
        visited = [False for i in Rn]
        distance.append()

    print(distances)


if __name__ == "__main__":
    main()
