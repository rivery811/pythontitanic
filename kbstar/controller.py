from kbstar.service import Service
from kbstar.model import Model
class Controller:

    def __init__(self):
        self._service = Service()
        self._model = Model()

    def preprocess(self, train, test) -> object:
        service = self._service
        this = self._model

    def modeling(self,train, test):
        service = self._service
        this = self.preprocess(train, test)

    def learning(self, train, test):
        service = self._service
        this = self.modeling(train, test)

    def submit(self, train, test):
        service = self._service
        this = self.modeling(train, test)