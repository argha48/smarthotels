# Run in terminal or command prompt
# python3 -m spacy download en

import numpy as np
import pandas as pd
import re, nltk, spacy, gensim

# Sklearn
from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from pprint import pprint

# Plotting tools
import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt
# %matplotlib inline

from gensim.corpora import Dictionary, MmCorpus
trigram_dictionary = Dictionary.load('./models2/trigram_dict_all.dict')
trigram_bow_corpus = MmCorpus('./models2/trigram_bow_corpus.nm')
# Document to matrix
import numpy as np
from scipy.sparse import csr_matrix
rows=[]
cols=[]
data=[]
Nrow = 1000000#len(trigram_bow_corpus)
Ncol = len(trigram_dictionary)
for i in range(0,Nrow):#
    line = trigram_bow_corpus[i]
    for indx,freq in line:
        rows.append(i)
        cols.append(indx)
        data.append(freq)
dtm = csr_matrix((data,(rows,cols)), shape = (Nrow,Ncol), dtype=int)

# Materialize the sparse data
# data_dense = dtm.todense()

# Compute Sparsicity = Percentage of Non-Zero cells
# print("Sparsicity: ", ((data_dense > 0).sum()/data_dense.size)*100, "%")
n_topics = list(range(50, 150, 10))# + list(range(50, 200, 50)) + list(range(200, 500, 100))
for NTopic in n_topics:
    # Build LDA Model
    lda_model = LatentDirichletAllocation(n_components=NTopic,               # Number of topics
                                          max_iter=10,               # Max learning iterations
                                          learning_method='online',
                                          batch_size=500000,            # n docs in each learning iter
                                          evaluate_every = -1,       # compute perplexity every n iters, default: Don't
                                          n_jobs = -1,               # Use all available CPUs
                                          verbose = 1)
    lda_output = lda_model.fit_transform(dtm)
    from joblib import dump, load
    model_fname = './sklearnlda/lda_n_'+str(NTopic)+'.joblib'
    dump(lda_model, model_fname)
    X_fname = './sklearnlda/transformedX_n_'+str(NTopic)+'.joblib'
    dump(lda_output, X_fname)
    print(lda_model)  # Model attributes
