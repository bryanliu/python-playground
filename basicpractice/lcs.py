# coding=utf-8

def printmatrix(matrix):
    for i in range(len(matrix)):
        print matrix[i]

    print("\n")

def lcs(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    mindist = [[0 for i in range(l1)] for j in range(l2)]

    #初始化第一行
    for i in range(l1):
        if s2[0] == s1[i]:
            mindist [0][i] = 1
        else:
            if i != 1:
                mindist[0][i] = mindist[0][i-1]

    #printmatrix(mindist)
    #初始化第一列
    for j in range(l2):
        if s1[0] == s2[j]:
            mindist[j][0] = 1
        else:
            if j != 1:
                mindist[j][0] = mindist[j-1][0]


    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i] == s2[j]:
                mindist[i][j] = max(mindist[i-1][j], mindist[i][j-1], mindist[i-1][j-1]+1)
            else:
                mindist[i][j] = max(mindist[i-1][j], mindist[i][j-1], mindist[i-1][j-1])



    printmatrix(mindist)






lcs("mtacnu", "mitcmu")