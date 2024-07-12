import numpy as np
from hmmlearn import hmm

startprob = np.array([0.6, 0.3, 0.1])
transmat = np.array([[0.7, 0.2, 0.1], [0.3, 0.5, 0.2], [0.3, 0.3, 0.4]])
means = np.array([[0.0, 0.0], [3.0, -3.0], [5.0, 10.0]])
covars = np.tile(np.identity(2), (3, 1, 1))
model = hmm.GaussianHMM(3, "full", startprob, transmat)
model.means_ = means
model.covars_ = covars
X = np.random.randint(0,3,(100,20))

model2 = hmm.GaussianHMM(3, "full")
model2.fit(X)
Z2 = model2.predict(X)
print(Z2)