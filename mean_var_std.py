import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array([list[:3], list[3:6], list[6:]])
    calculations = {'mean':[], 'variance':[], 'standard deviation':[], 'max': [], 'min': [], 'sum': []}
    calculations['mean'].append(np.mean(arr, axis=0).tolist())
    calculations['mean'].append(np.mean(arr, axis=1).tolist())
    calculations['mean'].append(np.mean(arr).tolist())
    calculations['variance'].append(np.var(arr, axis=0).tolist())
    calculations['variance'].append(np.var(arr, axis=1).tolist())
    calculations['variance'].append(np.var(arr).tolist())
    calculations['standard deviation'].append(np.std(arr, axis=0).tolist())
    calculations['standard deviation'].append(np.std(arr, axis=1).tolist())
    calculations['standard deviation'].append(np.std(arr).tolist())
    calculations['max'].append(np.max(arr, axis=0).tolist())
    calculations['max'].append(np.max(arr, axis=1).tolist())
    calculations['max'].append(np.max(arr).tolist())
    calculations['min'].append(np.min(arr, axis=0).tolist())
    calculations['min'].append(np.min(arr, axis=1).tolist())
    calculations['min'].append(np.min(arr).tolist())
    calculations['sum'].append(np.sum(arr, axis=0).tolist())
    calculations['sum'].append(np.sum(arr, axis=1).tolist())
    calculations['sum'].append(np.sum(arr).tolist())
    return calculations
