class Model:
    def __init__(self):
        self._context = None
        self._fname = None
        self._train = None
        self._test = None
        self._id = None

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> object: return self._id

    @id.setter
    def id(self, testId): self._id = id

