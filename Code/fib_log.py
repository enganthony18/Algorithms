base_matrix = [ [0,1], [1,1] ]
identity_matrix = [ [1,0], [0,1] ]

def mul_square_matrix(A, B):
    C = [ [0,0], [0,0] ]
    C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
    return C

def exp_square(base, n):
    if n == 0 :
        return identity_matrix
    while n > 0 :
        if n % 2 == 1:
            return mul_square_matrix(base, exp_square(\
                    mul_square_matrix(base, base), (n - 1)/2 ) )
        else:
            return exp_square( mul_square_matrix(base, base), n / 2 )

def fibonacci(n):
    return exp_square(base_matrix, n)[1][0]
