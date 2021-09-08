A=[1,2,3,13,5,9,8,2,0]
B=[1,2,3,5,6,9,8,1,10]

def crunch_matrix(A, B):            #алгоритм Нидлмана—Вунша, снизу гифка как робит
    #https://hsto.org/storage2/4c7/061/02a/4c706102aa8f467337723aa092f4bd5a.gif
    L = [[0]*(len(A)+1) for i in range(len(B)+1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L

def subsequence(A, B):      #проход матрицы из crunch_matrix назад
    L = crunch_matrix(A, B)
    subsequence = []
    x_i,y_i = len(A)-1,len(B)-1
    while x_i >= 0 and y_i >= 0:
        if A[x_i] == B[y_i]:
            subsequence.append(A[x_i])
            x_i, y_i = x_i-1, y_i-1
        elif L[x_i-1][y_i] > L[x_i][y_i-1]:
            x_i -= 1            #x-=y  ~ x=x-y
        else:
            y_i -= 1
    subsequence.reverse()
    return subsequence

print(subsequence(A,B))
