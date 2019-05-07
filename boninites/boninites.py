# to impute missing values
from sklearn import impute#SimpleImputer, MissingIndicator
from sklearn import preprocessing
import numpy as np

class boninite():
    
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