def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    result = []
    import numpy as np

    def mean(list_a:list[int|float])-> float:
        temp = 0
        for i in range(len(list_a)):
            temp+=list_a[i]
        temp/=len(list_a)
        return temp

    def cova(i: int, j: int) -> float:
        sum = 0
        for m in range(len(vectors[i])):
            sum += (vectors[i][m]-mean(vectors[i]))*(vectors[j][m]-mean(vectors[j]))
        sum/=(len(vectors[i])-1)
        return sum

    temp = [] 
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            temp.append(cova(i,j))
        result.append(temp)
        temp = []


    return result