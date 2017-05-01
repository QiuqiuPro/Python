
# coding: utf-8

# In[1]:

import numpy as np
import sklearn
import sklearn.datasets as ds
import sklearn.cross_validation as cv
import sklearn.neighbors as nb
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

digits = ds.load_digits()
X = digits.data
Y = digits.target
print((X.min(), X.max()))
print(X.shape)


# In[3]:

nrows, ncols = 2, 5
plt.gray()
for i in range(ncols * nrows):
    ax = plt.subplot(nrows, ncols, i + 1)
    ax.matshow(digits.images[i,...])
    plt.xticks([]); plt.yticks([]) #縦横の目盛りを非表示
    plt.title(digits.target[i])


# In[4]:

# このデータをK近傍分類器にかける
(X_train, X_test, Y_train, Y_test) = cv.train_test_split(X, Y, test_size=.25)


# In[5]:

knc = nb.KNeighborsClassifier()


# In[6]:

knc.fit(X_train, Y_train)


# In[7]:

knc.score(X_test, Y_test)


# In[14]:

# Let's draw a 1.
one = np.zeros((8,8))
one[1:-1, 4] = 16 #the image values are in [0,16]
one[2,3] = 16
two = np.array([[  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
             [  0.,   0.,  16.,  16.,  16.,   0.,   0.,   0.],
             [  0.,  16.,   0.,   0.,   0.,  16.,   0.,   0.],
             [  0.,   0.,   0.,   0.,   0.,  16.,   0.,   0.],
             [  0.,   0.,   0.,   0.,  16.,   0.,   0.,   0.],
             [  0.,   0.,   0.,  16.,   0.,   0.,   0.,   0.],
             [  0.,   0.,  16.,   0.,   0.,   0.,   0.,   0.],
             [  0.,  16.,  16.,  16.,  16.,  16.,   0.,   0.]])
plt.imshow(two, interpolation='none')


# In[9]:

plt.imshow(one, interpolation='none')
plt.grid(False)
plt.xticks(); plt.yticks()
plt.title("One")


# In[16]:

print(knc.predict(one.ravel()))
print(knc.predict(two.ravel()))


# In[ ]:



