# import re
# from nltk.corpus import stopwords
#
# arr = ['names', 'i am a roble', 'kanha', 'you are my sunshine', 'lets happened to be the word']
# mergedText = 'names i am a roble kanha you are my sunshine let\'s happened to be the word @d%^'
# a_removed = re.sub(r' a ','', mergedText)
# the_removed = re.sub(r' a ','', a_removed)
# SPLIT_RE = re.compile(r'[^a-zA-Z0-9]')
#
# s=set(stopwords.words('english'))
# print(list(filter(lambda w: not w in s,mergedText.split())))
# # print(SPLIT_RE.split(a_removed))