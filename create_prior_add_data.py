#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 16:08
# @Author  : LeoGo2017
# @File    : create_prior_add_data.py

#add test

import pandas as pd
import numpy as np
import lightgbm as lgb
from itertools import chain
import gc
from com_util import *
from sklearn.metrics import log_loss
from scipy.stats import mode

path = "output/"
priors = pd.read_csv(path + "order_products__prior.csv")
train = pd.read_csv(path + "order_products__train.csv")
test = pd.read_csv(path + "order_products__test.csv")
all = train.append(test)

orders = pd.read_csv(path + 'orders.csv').fillna(0)
orders = merge_max(orders, ['user_id'], 'order_number', 'order_number_max')
orders['order_dow_days'] = orders['order_dow'].apply(lambda x: 1 if x <= 1 else 0)
orders['order_hour_of_day_split'] = orders['order_hour_of_day'].apply(
    lambda x: 0 if 6 < x <= 12 else (1 if 12 < x <= 18 else 2))

path = 'input/'
products = pd.read_csv(path + 'products.csv')
departments = pd.read_csv(path + 'departments.csv')
aisles = pd.read_csv(path + 'aisles.csv')
# product2vec = pd.read_csv('features/product2vec_begin_1.csv')

#优化内存
print(orders.dtypes)
orders.user_id = orders.user_id.astype(np.int64)
orders.order_dow = orders.order_dow.astype(np.int8)
orders.order_hour_of_day = orders.order_hour_of_day.astype(np.int8)
orders.order_number = orders.order_number.astype(np.int16)
orders.order_id = orders.order_id.astype(np.int32)
orders.days_since_prior_order = orders.days_since_prior_order.astype(np.float32)




