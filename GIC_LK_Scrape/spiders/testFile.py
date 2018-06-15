# import re
# pr = "\t\ttryjkjgkjk\n\n\n\n\n\n\n\nlprof\nname of the"
# # qe = pr.replace('\t', '')
# # print(re.sub(r'(.)\1+', r'\1\1', qe))
# # print(re.sub(r'\n', ':', qe))
#
# #to = 'aannnndddddddddnnfffff'
# print(re.sub(r'(\n)\1*', '\n', pr))

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