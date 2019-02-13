import matplotlib.pyplot as plt   # for plotting the results
plt.style.use('ggplot')

# for loading the data:
from tmtoolkit.utils import unpickle_file
# for model evaluation with the lda package:
from tmtoolkit.topicmod import tm_lda
# for constructing the evaluation plot:
from tmtoolkit.topicmod.evaluate import results_by_parameter
from tmtoolkit.topicmod.visualize import plot_eval_results
from gensim.corpora import Dictionary, MmCorpus
trigram_dictionary = Dictionary.load('./models2/trigram_dict_all.dict')
trigram_bow_corpus = MmCorpus('./models2/trigram_bow_corpus.nm')
# Document to matrix
import numpy as np
from scipy.sparse import csr_matrix
rows=[]
cols=[]
data=[]
for i in range(0,len(trigram_bow_corpus)):
    line = trigram_bow_corpus[i]
    for indx,freq in line:
        rows.append(i)
        cols.append(indx)
        data.append(freq)
dtm = csr_matrix((data,(rows,cols)), shape = (len(trigram_bow_corpus),len(trigram_dictionary)), dtype=int)

const_params = dict(n_iter=20)
ks = list(range(5, 100, 5)) #+ list(range(50, 200, 50)) + list(range(200, 500, 100))
varying_params = [dict(n_topics=k, alpha=1.0/k) for k in ks]

eval_results = tm_lda.evaluate_topic_models(dtm,varying_params,const_params, return_models=True)#,n_max_processes=8

results_by_n_topics = results_by_parameter(eval_results, 'n_topics')

# fig, ax = plt.subplots(figsize=(8, 6))
plot_eval_results(results_by_n_topics)
plt.tight_layout()
# plt.savefig('valid_lda.eps', format='eps', dpi=300)
plt.show()
