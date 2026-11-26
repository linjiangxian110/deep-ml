import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    

    max = np.max(data,axis=0)

    standardized_data = []
    normalized_data = []
    mean = np.mean(data,axis=0)
    std = np.std(data,axis=0)
    max = np.max(data,axis=0)
    min = np.min(data,axis=0)

    for i in range(len(data)):
        temp1 = []
        temp2 = []
        for j in range(len(data[i])):
            temp1.append(np.round((data[i][j]-mean[j])/std[j],4))
            temp2.append(np.round((data[i][j]-min[j])/(max[j]-min[j]),4))
        standardized_data.append(temp1)
        normalized_data.append(temp2)

    return standardized_data, normalized_data