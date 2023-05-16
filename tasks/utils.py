# Álgebra Linear Computacional - 2023.1
# Trabalho 01
# Task selecionadas: 1 e 2
# Aluna: Lidiana Souza dos Anjos

def back_mult(A, i, l, c):
    if i==0:
        return A.loc[i, c]*A.loc[l, i]
    else: 
        return A.loc[i, c]*A.loc[l, i] + back_mult(A, i-1, l, c)

def sym(M):
    sim = True
    j = 0
    for i in range(len(M)-1):
        while (j < (len(M))-1):
            if M[i][j+1] != M[j+1][i]:
                sim = False
            j+=1
        j = j - (j - 1)
            
    return sim
            
def diagDom(M):
    sumL = 0
    sumC = 0
    for i in range(len(M)-1):
        for j in range(len(M)-1):
            if i != j:
                sumL = sumL + M[i][j]
                sumC = sumC + M[j][i]
        if M[i][i] < sumL or M[i][i] < sumC:
            print("Possibilidade de não convergência pois a matriz não é diagonal dominante.")
            return 0
    return 1

def residuo(X, Xold, mod=2):

    if mod==2:
        r = ((sum((X[i]-Xold[i])**2 for i in range(len(X))))**(1/2))/(sum(X[i]**2 for i in range(len(X)))**(1/2))
        return r
    if mod==1:
        r = abs(X-Xold)/abs(X)
        return r

def matrixVector_product(A, X):

    Y = [0]*len(X)
    for i in range(len(X)):
        Y[i] = sum(A.loc[i, j]*X[j] for j in range(len(X)))

    return Y