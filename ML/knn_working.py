#!/usr/bin/env python3
import numpy as np
import functools 
def distance(X, Y):
    return np.sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)

def sort_distances(item1 , item2):
    if item1[1] < item2[1]:
        return -1
    elif item1[1] == item2[1]:
        return 0
    else:
        return 1

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
    Q = []
    for i in range(Qn):
        Xi, Yi = input().split()

        point = (int(Xi), int(Yi))
        Q.append(point)

    print(Q)

    for q in Q:
        distances = []
        for i in range(len(R)):
                distances.append([i,distance(q,R[i])])
    
        print("unsorted Distances: " , distances)
        # distances.sort(key=sort_distances)
        distances = sorted(distances , key = functools.cmp_to_key(sort_distances))
        print("Sorted distances:" , distances)

        k_nearest_neighbours = [ distances[i] for i in range(k) ]
        print("k_nearest_neighbours:",  k_nearest_neighbours )
    

if __name__ == "__main__":
    main()
