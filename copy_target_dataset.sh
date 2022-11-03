src=fr
tgt=en
data=./data/$tgt-$src

# create preprocessed directory
mkdir -p $data/preprocessed_copy/
origin_data=$data/preprocessed
copied_data=$data/preprocessed_copy



# concat files
echo $origin_data
echo $copied_data

# concat 2 lang into src
cat $origin_data/test.* > $copied_data/test.src
cat $origin_data/tiny_train.* > $copied_data/tiny_train.src
cat $origin_data/tm.* > $copied_data/tm.src
cat $origin_data/train.* > $copied_data/train.src
cat $origin_data/valid.* > $copied_data/valid.src

# duplicat tgt lang into same file
cat $origin_data/test.$tgt $origin_data/test.$tgt > $copied_data/test.tgt
cat $origin_data/tiny_train.$tgt $origin_data/tiny_train.$tgt > $copied_data/tiny_train.tgt
cat $origin_data/tm.$tgt $origin_data/tm.$tgt > $copied_data/tm.tgt
cat $origin_data/train.$tgt $origin_data/train.$tgt > $copied_data/train.tgt
cat $origin_data/valid.$tgt $origin_data/valid.$tgt > $copied_data/valid.tgt
