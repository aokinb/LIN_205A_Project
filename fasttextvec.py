# from https://fasttext.cc/docs/en/unsupervised-tutorial.html

# import modules
import fasttext
import numpy as np

# build model with corpus
model = fasttext.train_unsupervised('/Users/nynaeve/Desktop/UC Davis/22 SPRING/computational linguistics/LIN_205A_Project/debate_transcripts/1960_1.txt')

# returns all words in vocabulary sorted by decreasing frequency
print(model.words)

# to get word vector for specific item
print(model.get_word_vector("the"))

# save model as binary file (with some model name)
model.save_model("/Users/nynaeve/Desktop/UC Davis/22 SPRING/computational linguistics/LIN_205A_Project/vectors/trial.bin")

# can reload this model later
model = fasttext.load_model("model_filename.bin/Users/nynaeve/Desktop/UC Davis/22 SPRING/computational linguistics/LIN_205A_Project/vectors/trial.bin")


# in order to use wordvecutil, need to get word vectors in .txt format
vectorList = []

for word in model.words:
    vec = []
    vec.append(word)
    list = model.get_word_vector(word)
    for i in list:
        vec.append(i)
    # vec = np.insert(vec, 0, word)
    vectorList.append(vec)

# save as .txt
with open("file.txt", 'w') as file:
        for row in vectorList:
            s = " ".join(map(str, row))
            file.write(s+'\n')


import wordvecutil
v = wordvecutil.word_vectors("/Users/nynaeve/Desktop/UC Davis/22 SPRING/computational linguistics/LIN_205A_Project/file.txt", 100000)

# most similar words: 
print(v.near('democrat', 10))

# find similarity: 
print(v.sim('democrat', 'republican'))
