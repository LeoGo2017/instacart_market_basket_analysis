#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 16:08
# @Author  : LeoGo2017
# @File    : create_prior_add_data.py


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
orders['order_hour_of_day'] = orders['order_hour']
