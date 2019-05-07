# to impute missing values
from sklearn import impute#SimpleImputer, MissingIndicator
from sklearn import preprocessing
import numpy as np

class boninite():
    """classifies boninite magmas using a dataset of chemical elements

    Attributes
    ----------
    X : Pandas dataframe
        The dataframe containing the chemical analysis
    elements : List
        The name of the first and last element to include in the classification
    imputer : sklearn imputer
        Impute missing values. Default is the sklearn.impute.SimpleImputer() that replaces missing values with the mean of the column
    X_imputed : ndarray
        Imputed X values
    scaler : sklearn scaler
        The scaler to use. Default is the sklearn.preprocessing.StandardScaler()
    X_sc : ndarray
        Scaled and imputed X values
    model : sklearn classification model

    Methods
    -------
    model.fit(self)
        Classifies the X_sc dataset created after initialization
    model.predict(self,data)
        Predictions on new data (Pandas dataframe)
    """
    def __init__(self, model, data, elements,file_format="csv"):

        self.X = data.loc[:,elements[0]:elements[1]] # for training the clustering algo
        self.elements = elements
        # impute
        self.imputer = impute.SimpleImputer(missing_values=np.nan, strategy='mean')
        self.X_imputed = self.imputer.fit_transform(self.X)

        # Standardization
        self.scaler = preprocessing.StandardScaler().fit(self.X_imputed)
        self.X_sc = self.scaler.transform(self.X_imputed)

        self.model = model

    def fit(self):
        self.model.fit(self.X_sc)

    def predict(self,data):
        X_ = data.loc[:,self.elements[0]:self.elements[1]] # for training the clustering algo
        return self.model.predict(self.scaler.transform(self.imputer.transform(X_)))
