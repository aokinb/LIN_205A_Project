# eve booker 5/17/2022
# code to check amount of words in text files (debate transcripts)

# import required modules
import os
import glob

# open directory/initialize variables
# (used my specific path)
os.chdir("/Users/nynaeve/Desktop/UC Davis/22 SPRING/computational linguistics/LIN_205A_Project/debate_transcripts")
totalWordCount = 0

# iterate over files in directory
for filename in glob.glob('*.txt'):

    # open text file in read only mode
    with open(filename, 'r') as file:

        #read content of file and store in new variable
        data = file.read()
        # print(data)

        # split data
        words = data.split()

        # check number of words in file
        # print(len(words))

        # store word count
        wordCount = len(words)

        # update total word count
        totalWordCount = totalWordCount + wordCount

print('Total number of words: ', totalWordCount)
# total number of words: 718433 