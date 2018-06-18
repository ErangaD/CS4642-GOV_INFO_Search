import re
pr = "Eranga\n \n\n\n\n\n\n\nlprof\n\n\n\n\n\n\n\n\n\n \n \nname of the"
qe = pr.replace('\t', '')

first = re.sub(r'(\s*\n\s*)\1*', '\n', qe)
print(first)

# from collections import defaultdict
#
# def create_index(data):
#     index = defaultdict(list)
#     for i, tokens in enumerate(data):
#         for token in tokens:
#             index[token].append(i)
#     return index
#
# create_index([['a', 'a', 'b'], ['a', 'c']])