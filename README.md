# ATMT assignment_03 BPE and BPE drop out
Fr-En translation with srouce and target sentences in BEP or BEP-dropout tokens.

# New scripts

### atmt_2022/test.py

```
Create bpe token dict(dict.fr, dict.en ) from 
train.fr and train.en in  /atmt_2022/data/en-fr/preprocessed/
```

### atmt_2022/ create_bpe_file.py

```
Create training, validation and testing data with bpe token 
dict and original preprocessed datasets for model
```
### atmt_2022/BPE_decode.py

```
After translate.py, the generated txt is shown in BEP tokens. 
We need to transform it into normal English tokens before running postprocess.sh
```

# Training a model

```
!python train.py \
    --data bpe_data/prepared \
    --source-lang fr \
    --target-lang en \
    --save-dir assignments/13/baseline/checkpoints \
    --batch-size 348 \
    --patience 15 \
    --log-file log/13.log \
    --lr 0.0005 \
    --cuda\
    --BpeDropOutSrc 1\
    --BpeDropOutTar 1 \
    --encoder-embed-dim 128 \
    --encoder-hidden-size 128 \
    --decoder-embed-dim 128 \
    --decoder-hidden-size 256 \
    --encoder-num-layers 1 \
    --decoder-num-layers 1 
```

Notes:
- --BpeDropOutSrc,--BpeDropOutTar 1 means no dropout; set 0.1 as paper suggests

# Evaluating a trained model

Run inference on test set
```
!python translate.py \
    --data bpe_data/prepared \
    --dicts bpe_data/prepared \
    --checkpoint-path assignments/13/baseline/checkpoints/checkpoint_last.pt \
    --output assignments/13/baseline/enfr_translations.txt \
    --batch-size 128 \
    --cuda
```
After translate.py, the generated txt is shown in BEP tokens. We need to transform it into normal English tokens before
running postprocess.sh
```
!python BPE_decode.py \
  --filePath assignments/13/baseline/enfr_translations.txt \
  --newFilePath assignments/13/baseline/enfr_translations_new.txt
```

Postprocess model translations
```
!bash scripts/postprocess.sh \
    assignments/13/baseline/enfr_translations_new.txt \
    assignments/13/baseline/enfr_translations.p.txt en
```

Score with SacreBLEU
```
!cat \
    assignments/13/baseline/enfr_translations.p.txt \
    | sacrebleu data/en-fr/raw/test.en
```


