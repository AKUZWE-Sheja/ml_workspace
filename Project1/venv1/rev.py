# Categorical data: nominal(no order) & ordinal(order)
# Encoding techniques: one-hot, label(ordinal), binary(nominal), frequency & target (both)
# https://www.datacamp.com/tutorial/python-data-profiling?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157098106975&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=720362650696&utm_targetid=dsa-2264919291789&utm_loc_interest_ms=&utm_loc_physical_ms=9070182&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-bfcm24&gad_source=1&gclid=Cj0KCQiA6Ou5BhCrARIsAPoTxrDkP79r1St0qNGNQciTiIdKktnIvXJnTwPxCXuWBJ5VAZ_NJiBMOn4aAokwEALw_wcB
# https://www.analyticsvidhya.com/blog/2022/07/step-by-step-exploratory-data-analysis-eda-using-python/

import pandas as pd
import sklearn.linear_model as LinearRegression
import requests

db_username = 'postgres'
db_port = ''


# data = {
#     'X': [1, 2, 3, 4, 5],
#     'Y': [6, None, 5, 4, 2]
# }

# df = pd.DataFrame(data)

# train = df[df['Y'].notnull()]
# X_train = train[['X']]
# Y_train = train['Y']

# model = LinearRegression()
# model.fit(X_train, Y_train)

# missing = df[df['Y'].isnull()]
# X_missing = missing[['X']]
# df.loc[df['Y'].isnull(), 'Y'] - model.predict(X_missing)
print(df)