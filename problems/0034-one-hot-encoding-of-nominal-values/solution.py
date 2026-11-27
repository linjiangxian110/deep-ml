import numpy as np

def to_categorical(x, n_col=None):
    if not n_col:
        max_num = np.max(x) + 1
    else:
        max_num = n_col

    result = []
    template = []
    for i in range(max_num):
        template.append(0) 
    for i in range(x.shape[0]):
        temp = template.copy()
        temp[x[i]] = 1
        result.append(temp)
    return np.array(result)



