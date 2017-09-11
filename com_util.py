#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/11 16:06
# @Author  : LeoGo2017
# @File    : com_util.py


import pandas as pd

def merge_count(df, columns, value, cname):
    add = pd.DataFrame(df.groupby(columns)[value].count()).reset_index()
    add.columns = columns + [cname]
    df = df.merge(add, on=columns, how='left')
    return df


def merge_nunique(df, columns, value, cname):
    add = pd.DataFrame(df.groupby(columns)[value].count()).reset_index()
    add.columns = columns + [cname]
    df = df.merge(add, on=columns, how='left')
    return df

def merge_median(df, columns, value, cname):
    add = pd.DataFrame(df.groupby(columns)[value].median()).reset_index()
    add.columns = columns + [cname]
    df = df.merge(add, on=columns, how='left')
    return df

def merge_mean(df,columns,value,cname):
    add = pd.DataFrame(df.groupby(columns)[value].mean()).reset_index()
    add.columns=columns+[cname]
    df=df.merge(add,on=columns,how="left")
    return df

def merge_sum(df,columns,value,cname):
    add = pd.DataFrame(df.groupby(columns)[value].sum()).reset_index()
    add.columns=columns+[cname]
    df=df.merge(add,on=columns,how="left")
    return df

def merge_max(df,columns,value,cname):
    add = pd.DataFrame(df.groupby(columns)[value].max()).reset_index()
    add.columns=columns+[cname]
    df=df.merge(add,on=columns,how="left")
    return df

def merge_min(df,columns,value,cname):
    add = pd.DataFrame(df.groupby(columns)[value].min()).reset_index()
    add.columns=columns+[cname]
    df=df.merge(add,on=columns,how="left")
    return df

def merge_std(df,columns,value,cname):
    add = pd.DataFrame(df.groupby(columns)[value].std()).reset_index()
    add.columns=columns+[cname]
    df=df.merge(add,on=columns,how="left")
    return df

