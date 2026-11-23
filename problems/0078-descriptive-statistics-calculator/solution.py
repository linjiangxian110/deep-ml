import numpy as np
from collections import Counter


def descriptive_statistics(data: list | np.ndarray) -> dict:
    def get_min_most(lst):
        cnt = Counter(lst)
        max_freq = max(cnt.values())
        candidates = [k for k, v in cnt.items() if v == max_freq]
        return min(candidates)

    length = len (data)

    sum = 0
    for i in range(length):
        sum += data[i]
    mean = sum/length

    if(length%2!=0):
        median = data[int((length-1)/2)]
    else:
        median = (data[int(length/2)] + data[int((length-1)/2)])/2
    
    mode = int(get_min_most(data))

    variance = 0
    for i in range(length):
        variance += (data[i]-mean)**2
    variance/=length

    standard_deviation = variance**0.5

    percentile = np.percentile(data, [25,50,75])

    interquartile_range = percentile[2]-percentile[0]


    result = {'mean':mean,'median':median,'mode':mode,'variance':variance,'standard_deviation':standard_deviation,'25th_percentile':percentile[0],'50th_percentile':percentile[1],'75th_percentile':percentile[2],
    'interquartile_range':interquartile_range}

    return  result