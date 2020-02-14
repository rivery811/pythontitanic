from titanic.model import Model
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
"""
['PassengerId' 고객ID,
'Survived', 생존여부
'Pclass', 승선권 1 = 1st 2 = 2nd 3 = 3rd
'Name',
'Sex',
'Age',
'SibSp',동반한 형제, 자매, 배우자
'Parch', 동반한 부모, 자식
'Ticket', 티켓번호
'Fare', 요금
'Cabin', 객실번호
'Embarked'] 승선한 항구명 C = 쉐부로, Q = 퀸즈타운, S = 사우스햄톤
self._test_id = test['PassengerId']
"""
class Service:
    def __init__(self):
        self._this = Model()


    def new_model(self, param):
        this = self._this
        this.context='./data'
        this.fname=param
        return pd.read_csv(this.context+'/'+this.fname)


    def create_train(self, this):
        return this.train.drop('Survived', axis=1)


    def create_dummy(self, this):
        return this.train['Survived']


    def create_kfold(self):
        return KFold(n_splits=10, shuffle=True, random_state=0)


    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this


    @staticmethod
    def embarked_norminal(this) -> object:
        this.train = this.train.fillna({"Embarked": "S"})
        this.train['Embarked'] = this.train['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        this.test = this.test.fillna({"Embarked": "S"})
        this.test['Embarked'] = this.test['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        return this


    @staticmethod
    def fareBand_norminal(this) -> object:
        this.train = this.train.fillna({"FareBand": 1})
        this.test = this.test.fillna({"FareBand": 1})
        return this


    @staticmethod
    def title_nominal(this) -> []:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)


        for dataset in combine:
            dataset['Title'] \
                = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] \
                = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] \
                = dataset['Title'].replace('Mlle', 'Miss')
            dataset['Title'] \
                = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] \
                = dataset['Title'].replace('Mme', 'Mrs')
        this.train[['Title', 'Survived']].groupby(['Title'], as_index=False).mean()
        """
            Title  Survived
        0  Master  0.575000
        1    Miss  0.701087
        2      Mr  0.156673
        3     Mrs  0.793651
        4      Ms  1.000000
        5    Rare  0.250000
        6   Royal  1.000000
        """


        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)
        this.train = this.train
        this.test = this.test
        return this


    @staticmethod
    def sex_nominal(this) -> []:
        combine = [this.train, this.test]
        sex_mapping = {"male": 0, "female": 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = this.train
        this.test = this.test
        return this


    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)
        age_title_mapping = {0: 'Unknown', 1: 'Baby', 2: 'Child',
                             3: 'Teenager', 4: 'Student', 5: 'Young Adult', 6: 'Adult', 7: 'Senior'}
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]


        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2,
                       'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6, 'Senior': 7}


        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        return this


    @staticmethod
    def fare_ordinal(this) -> []:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        return this


    # 검증 알고리즘 작성


    def accuracy_by_knn(self, this):
        score = cross_val_score(KNeighborsClassifier(n_neighbors=13),
                                this.train,
                                this.dummy,
                                cv=this._kfold,
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_dtree(self,this):
        score = cross_val_score(DecisionTreeClassifier(),
                                this.train,
                                this.dummy,
                                cv=this.kfold,
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_rforest(self,this):
        score = cross_val_score(RandomForestClassifier(n_estimators=13),
                                this.train,
                                this.dummy,
                                cv=this.kfold,
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_nb(self, this):
        score = cross_val_score(GaussianNB(),
                                this.train,
                                this.dummy,
                                cv=this.kfold,
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def accuracy_by_svm(self, this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.dummy,
                                cv=this.kfold,
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


    def submit(self, this):
        train = this.train
        test = this.test
        dummy = this.dummy
        id = this.id
        context = this.context
        clf = SVC()
        clf.fit(train, dummy)
        prediction = clf.predict(test)
        submission = pd.DataFrame(
            {'PassengerId': id,
             'Survived': prediction}
        )
        print(submission.head())
        submission.to_csv(context + '/submission.csv', index=False)