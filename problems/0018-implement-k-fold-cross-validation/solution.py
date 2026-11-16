import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    
    result = []
    arr = np.arange(0,n_samples)

    if(shuffle):
        np.random.shuffle(arr)

    div = n_samples//k
    dif = n_samples-div*k
    m = 0
    for i in range(k):
        n = m+div
        left = []
        right = []
        new_arr = arr
        if(dif!=0):
            n+=1
            
        for j in range(m,n):
            left.append(arr[j])
        for j in range(m,n):
            new_arr=np.delete(new_arr,m) 
        if(dif!=0):
            dif-=1
        m=n
        right = new_arr.tolist()
        
        temp = (right,left)
        result.append(temp)
        
    return result