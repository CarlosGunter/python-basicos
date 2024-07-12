import numpy as np
from main import DH

def testDH():
    array_test = {
        1: [
            np.zeros(6),
            np.array([0.315, 0, 0, 0.5, 0, 0.08]),
            np.array([0, 0.45, 0, 0, 0, 0]),
            np.array([90, 0, 90, 90, 90, 0])
        ],
        2: [
            np.array([45]),
            np.array([2]),
            np.array([3]),
            np.array([90]),
        ],
        3: [
            np.array([45, 60, 90]),
            np.array([1, 0, 0]),
            np.array([0, 2, 3]),
            np.array([90, 0, 0])
        ]
    }
    results = np.zeros((len(array_test), 4, 4))
    for i in range(0, len(array_test)):
        results[i] = DH(
            array_test[i+1][0],
            array_test[i+1][1],
            array_test[i+1][2],
            array_test[i+1][3]
        )

    return results

np.set_printoptions(precision=4)
print(testDH())