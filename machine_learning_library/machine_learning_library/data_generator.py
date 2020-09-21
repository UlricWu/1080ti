import numpy as np


class DGP:
    def __init__(self, observations, dimensions, random_state=1024):
        self._observations = observations
        self._dimensions = dimensions
        self._random_state = random_state
        self._features = None
        self._labels = None
        self._train_x = None
        self._test_x = None
        self._train_y = None
        self._test_y = None

    def generate(self, usage='regression'):
        features, labels = self._generate()

        self._features = features
        self._labels = self._get_labels(labels, usage)

    @staticmethod
    def _get_labels(labels, usage):
        if usage == 'regression':
            return labels

        if usage == 'binaryclassification':
            return np.array([0 if x < 0 else 1 for x in labels]).reshape(-1, 1)

        if usage == 'multiclassification':
            return np.array([0 if x < -1 else 1 if x < 1 else 2 for x in labels]).reshape(-1, 1)

    def _generate(self):
        np.random.seed(self._random_state)
        x = np.random.normal(size=(self._observations, self._dimensions))
        error = np.random.normal(size=(self._observations, 1))
        b = np.random.uniform(size=(self._dimensions, 1))
        y = x @ b + error

        return x, y

    def split(self, rate=0.7, scale=False):

        if scale:
            self._features = (self._features - np.mean(self._features)) / self._features.std()

        index = list(range(self._observations))
        np.random.shuffle(index)

        train = index[:int(rate * self._observations)]
        test = index[int(rate * self._observations):]

        self._train_x = self._features[train]
        self._test_x = self._features[test]
        self._train_y = self._labels[train]
        self._test_y = self._labels[test]

        return self._train_x, self._test_x, self._train_y, self._test_y

    @property
    def feature(self):
        return self._features
