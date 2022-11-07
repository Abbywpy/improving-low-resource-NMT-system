import sentencepiece as spm
import pickle
import numpy as np

# load bpe model
bpe_model_fr = spm.SentencePieceProcessor(model_file='bpe_data/BPE_model/BPE_test.model')
bpe_model_en = spm.SentencePieceProcessor(model_file='bpe_data/BPE_model/BPE_en.model')

# fr
def make_scrfile_by_srcdict(bpe_dict, old_file, new_pickle, dropoutrate=1):
    with open(old_file, 'r') as f:
        old_file = f.read().strip().split('\n')
    old_bpe = bpe_model_fr.encode(old_file, out_type=str, alpha=dropoutrate, enable_sampling=True, nbest_size=-1)
    new_array = []
    for i in old_bpe:
        new_array.append([bpe_dict.index(j) for j in i])
    new_array = pickle.dumps(np.array(new_array))
    with open(new_pickle, 'wb') as f:
        f.write(new_array)

# en
def make_scrfile_by_tardict(bpe_dict, old_file, new_pickle, dropoutrate=1):
    with open(old_file, 'r') as f:
        old_file = f.read().strip().split('\n')
    old_bpe = bpe_model_en.encode(old_file, out_type=str, alpha=dropoutrate, enable_sampling=True, nbest_size=-1)
    new_array = []
    for i in old_bpe:
        b = [bpe_dict.index(j) for j in i]
        b.append(bpe_dict.eos_idx)
        new_array.append(b)

    new_array = pickle.dumps(np.array(new_array))
    with open(new_pickle, 'wb') as f:
        f.write(new_array)


