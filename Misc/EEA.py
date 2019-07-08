
def eea(a, b):
    r = 1
    z = 0
    matrix = []

    while r != 0:
        r = a % b
        matrix.append([])
        matrix[z].append(a)
        matrix[z].append(b)
        matrix[z].append(a // b)
        matrix[z].append(r)
        z += 1

        if r == 0:
            ggt = b

        a = b
        b = r
    z -= 2

    matrix[z + 1].append(0)
    matrix[z + 1].append(1)

    while z > -1:
        ai = matrix[z][0]
        bi = matrix[z][1]
        matrix[z].append(matrix[z + 1][5])
        si = matrix[z][4]

        matrix[z].append((ggt - si * ai) // bi)

        z -= 1

    return matrix
    
    
    def main():
    a = int(input(" Bidde erste Zahl eingeben: "))
    b = int(input(" Bidde zweite Zahl eingeben: "))

    matrix = eea(a, b)
    l = len(matrix) - 1

    print("\n")
    print(" Extended Euclidian Algorithm (it's #EEA) \n")

    print(" ggT von " + str(a) + " und " + str(b) + " lautet: " + str(matrix[l][1]) + "\n")
    print(" Zugehoerige Linear-Kombination LKB: " + str(matrix[0][4]) + " * " + str(a) + " + " + str(matrix[0][5]) + " * " + str(b) + " = " + str(matrix[l][1]))
    print("\n")

    for i in range(l + 1):
        print((str(matrix[i][0]).center(6) + " mod " + str(matrix[i][1]).center(6) + " = " + str(matrix[i][3]).center(6)).ljust(25) + " --->   zugehoerige LKB:   " + str(matrix[i][4]).center(4) + " * " + str(matrix[i][0]).center(4) + " + " + str(matrix[i][5]).center(4) + " * " + str(matrix[i][1]).center(4) + " =  " + str(matrix[l][1]))

    print("\n\n")
    print(" Copyright © 2018 by Robert Eikmanns")
    print("\n\n")


if __name__ == '__main__':
    main()

