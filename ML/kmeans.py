import numpy as np

def main():
    En = int(input("enter the number of entities"))
    
    E = [ ]
    for i in range(En):
        E.append(tuple([int(x) for x in input().split()]))

    
    print(E)

    for i in range(En):
        

if __name__ == "__main__":
    main()
