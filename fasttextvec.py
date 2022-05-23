# from https://fasttext.cc/docs/en/unsupervised-tutorial.html

# import modules
import fasttext

# build model with corpus
model = fasttext.train_unsupervised('/Users/nynaeve/Desktop/UC Davis/22 SPRING/computational linguistics/LIN_205A_Project/debate_transcripts/1960_1.txt')

# returns all words in vocabulary sorted by decreasing frequency
print(model.words)

# to get word vector for specific item
print(model.get_word_vector("the"))

# save model as binary file (with some model name)
model.save_model("model_filename.bin")

# can reload this model later
model = fasttext.load_model("model_filename.bin")