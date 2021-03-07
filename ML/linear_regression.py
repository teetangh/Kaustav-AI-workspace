import numpy as np


def main():
    n = int(input("Enter number of data points"))

    X = []
    Y = []
    for i in range(n):
        txt = "Enter the {value}th example in the training set."
        xi, yi = input(txt.format(value=i)).split()

        X.append(int(xi))
        Y.append(int(yi))

    print("The dataset contains the values")
    print(X)
    print(Y)

    sumX, sumX2, sumY, sumXY = 0, 0, 0, 0

    for i in range(0, n):
        sumX = sumX + X[i]
        sumX2 = sumX2 + (X[i] * X[i])

        sumY = sumY + Y[i]
        sumXY = sumXY + (X[i] * Y[i])

    m = ((n * sumXY) - (sumX * sumY))/((n*sumX2) - (sumX*sumX))
    c = (sumY - m * sumX)/n

    print("y = mx + c with c and m values respectively are:")
    print(c, m)


if __name__ == '__main__':
    main()
