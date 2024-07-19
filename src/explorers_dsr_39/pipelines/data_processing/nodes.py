import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def get_train_data(features, labels):
    """ 
    Input:
        str to csv with train features and labels

    Output:
        data_clean_dt, X, y
    
    """
    data = features.merge(labels)

    data_clean = data.dropna()
    print("Droped {:.2f}% of rows.".format((1 - data_clean.shape[0]/data.shape[0])*100))

    data_clean.loc[:,'log_total_cases'] = np.log1p(data_clean['total_cases'])
    data_clean_dt = get_dt_col(data_clean)

    y = data_clean_dt['log_total_cases']
    X = data_clean_dt.drop(columns=['total_cases','log_total_cases'])

    
    return data_clean_dt, X, y


def get_dt_col(X , column='week_start_date', format='%Y-%m-%d'):
    """
    Input:
        X
        col = weekofx

    Returns:
        X with X[col].dtype = datetime

    """
    X_new = X.copy()
    X_new[column] = pd.to_datetime(X_new[column], format=format)

    return X_new

def get_model(X, y, feats):
    regr = RandomForestRegressor(random_state=0)
    regr.fit(X[feats], y)
    return regr

def get_pred(regr, test_data, feats):
    predictions = regr.predict(test_data[feats])
