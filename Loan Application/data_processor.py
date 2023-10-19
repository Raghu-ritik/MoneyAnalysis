def ValueCountOfFeatures(DataFrame,FeatureColumn="StageName"):
    return DataFrame[FeatureColumn].value_counts()

def DiscreteFeatures(DataFrame):
    #Lets classify the features into discrete variables
    return [feature for feature in NumericalFeatures(DataFrame) if len(DataFrame[feature].unique())<10 and len(DataFrame[feature].unique())>0]


def NumericalFeatures(DataFrame):
    #Lets classify the features into continuous variables
    # list of numerical variables
    return [feature for feature in DataFrame.columns if DataFrame[feature].dtypes != 'O']
