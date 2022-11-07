import numpy as np
import sentencepiece as spm
import random
from seq2seq.data.dictionary import Dictionary
import collections
import create_bpe_file
import pickle
import torch
# spm.SentencePieceTrainer.Train(input='data/en-fr/preprocessed/train.en', model_prefix='BPE_en',
#                                          vocab_size=4000)



#
# sp = spm.SentencePieceProcessor(model_file ='bpe_data/BPE_model/BPE_en.model')
# with open('data/en-fr/preprocessed/train.fr', 'r') as f:
#     file = f.read().strip().split('\n')
# #
# #
# aaa = file[6:8]
# bpe_traindata = sp.encode(aaa, out_type=str, alpha=0.1, enable_sampling=True)
# # bpe_traindata = sp.encode(file, out_type=str)
# print(aaa)
# print(bpe_traindata)
# print(sp.encode(aaa, out_type=str))
# print(sp.decode(bpe_traindata))




# all_data = []
# for i in bpe_traindata:
#     all_data = all_data + i
# collect = collections.Counter(all_data)
# print(collect)
#
# cc = []
# for i in enumerate(collect.items()):
#     j = i[1]
#     cc.append(j[0]+' '+str(j[1]))
#
# with open('bpe_data/prepared/dict.en', 'w') as f:
#     f.write('\n'.join(cc))




