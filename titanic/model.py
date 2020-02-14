class Model:
    def __init__(self):
        self._context = ''
        self._fname = ''
        self._train = None
        self._test = None
        self._id = None
        self._dummy = None
        self._kfold = None


    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context


    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname


    @property
    def train(self) -> object:
        return self._train
    @train.setter
    def train(self,train):
        self._train = train


    @property
    def test(self) -> object : return self._test
    @test.setter
    def test(self, test): self._test = test


    @property
    def id(self) -> object: return self._id
    @id.setter
    def id(self, id): self._id = id


    @property
    def dummy(self) -> object: return self._dummy


    @dummy.setter
    def dummy(self, dummy): self._dummy = dummy


    @property
    def kfold(self) -> object: return self._kfold


    @kfold.setter
    def kfold(self, kfold): self._kfold = kfold