import argparse
import sentencepiece as spm

bpe_model_en = spm.SentencePieceProcessor(model_file='bpe_data/BPE_model/BPE_en.model')

def get_args():
    parser = argparse.ArgumentParser('Sequence to Sequence Model')
    parser.add_argument('--filePath', type=str, help='bpe test en')
    parser.add_argument('--newFilePath', type=str, help='new test en')
    return parser.parse_args()
def main(args):
    with open(args.filePath, 'r') as f:
        file = f.read().strip().split('\n')
    file_0 = [i.split(' ') for i in file]
    new = bpe_model_en.decode(file_0)
    with open(args.newFilePath, 'w') as f:
        f.write('\n'.join(new))






if __name__ == '__main__':
    args = get_args()
    main(args)