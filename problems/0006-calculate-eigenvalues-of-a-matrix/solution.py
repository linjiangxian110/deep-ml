import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    data = np.array(matrix,float)
    eigenvalues,eigvecs = np.linalg.eig(data)

    return eigenvalues.tolist()