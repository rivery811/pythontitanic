from titanic.service import Service
from titanic.model import Model
class Controller:
    def __init__(self):
        self._service = Service()
        self._model = Model()


    def preprocess(self, train, test) -> object:
        service = self._service
        this = self._model
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        this = service.embarked_norminal(this)
        this = service.title_nominal(this)
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        this = service.drop_feature(this, 'Fare')
        this = service.sex_nominal(this)
        this = service.fareBand_norminal(this)
        print('트레인 컬럼 {}'.format(this.test.columns))
        print('널의 수량 {}  개'.format(this.test.isnull().sum()))
        return this


    def modeling(self,train, test):
        service = self._service
        this = self.preprocess(train, test)
        this.dummy = service.create_dummy(this)
        this.train = service.create_train(this)
        this.kfold = service.create_kfold()
        this.context = './data'
        print('<<<< MODELING SUCCESS >>>>')
        return this


    def learning(self, train, test):
        service = self._service
        this = self.modeling(train, test)
        print('KNN 활용한 검증 정확도 {} %'.format(service.accuracy_by_knn(this)))
        print('결정트리 활용한 검증 정확도 {} %'.format(service.accuracy_by_dtree(this)))
        print('랜덤포리스트 활용한 검증 정확도 {} %'.format(service.accuracy_by_rforest(this)))
        print('나이브베이즈 활용한 검증 정확도 {} %'.format(service.accuracy_by_nb(this)))
        print('SVM 활용한 검증 정확도 {} %'.format(service.accuracy_by_svm(this)))
        print('<<<< TEST SUCCESS >>>>')


    def submit(self, train, test):
        service = self._service
        this = self.modeling(train, test)
        service.submit(this)
        print('<<<< SUBMIT SUCCESS >>>>')