"""
如何保存并恢复sklearn建立的模型
"""
from sklearn.externals import joblib

# 保存
joblib.dump(lr, 'lr.model')
# 恢复
lr = joblib.load('lr.model')
