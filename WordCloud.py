import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    frequency = {}
    file_contents = file_contents.read().lower()
    file_contents = file_contents.split()
    for i in range(len(file_contents)):

        for j in range(len(file_contents[i])):
            if (file_contents[i])[j] in punctuations:
                (file_contents[i])[j].replace((file_contents[i])[j], "")

        if file_contents[i] not in uninteresting_words:
            if file_contents[i] not in frequency.keys():
                frequency[file_contents[i]] = 1
            else:
                frequency[file_contents[i]] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency)
    return cloud.to_array()

# Display your wordcloud image

file = open("Chetan Bhagat.txt", "r")
myimage = calculate_frequencies(file)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

