from numpy import linalg
import numpy as np


class Regression:
    def __init__(self, intercept=None):
        self.beta = None
        self.intercept = intercept

    def fit(self, features, labels):
        features = self._add_bias(features)

        self._fit(features, labels)

    def predict(self, features):
        features = self._add_bias(features)
        return self._predict(features)

    def _add_bias(self, features):
        if self.intercept:
            ones = np.ones((len(features), 1))
            return np.hstack([ones, features])

        return features

    def _fit(self, features, labels):
        raise NotImplementedError

    def _predict(self, features):
        return features @ self.beta


class LeastSquare(Regression):
    def __init__(self, intercept=False):
        super().__init__(intercept)

    def _fit(self, features, labels):
        xx = features.T @ features
        xy = features.T @ labels

        self.beta = linalg.solve(xx, xy)


class Ridge(Regression):
    def __init__(self, intercept=False, _lambda=0.2):
        super().__init__(intercept)

        self._lambda = _lambda

    def _fit(self, features, labels):
        identity = self._lambda * np.identity(features.shape[1])
        xy = features.T @ labels
        xx = features.T @ features
        self.beta = np.linalg.inv(xx + identity) @ xy


class GradientDescent(Regression):
    def __init__(self, intercept=False, learning_rate=0.01, batch=10000,
                 threshold=1e-5, random=False):
        super().__init__(intercept)

        self._learning_rate = learning_rate
        self._batch = batch
        self._threshold = threshold
        self._random = random

    def _fit(self, features, labels):
        observations, dimensions = features.shape

        beta = np.random.randn(dimensions).reshape(-1, 1) if self._random \
            else np.ones(dimensions).reshape(-1, 1)

        for i in range(self._batch):

            error = features @ beta - labels
            update = features.T @ error * (self._learning_rate / observations)
            beta -= update

            if np.abs(update).sum() < self._threshold:
                self.beta = beta
                return
        raise ValueError('Gradient did not converge')
