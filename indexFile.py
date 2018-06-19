from pprint import pprint as pp
from glob import glob

from functools import reduce
raw_input = input


def parsetexts(fileglob='data/T*.txt'):
    texts, words = {}, set()
    for txtfile in glob(fileglob):
        with open(txtfile, 'r') as f:
            txt = f.read().split()
            words |= set(txt)
            texts[txtfile.split('\\')[-1]] = txt
    return texts, words

texts, words = parsetexts()
print('\nTexts')
# pp(texts)
print('\nWords')
# pp(sorted(words))

# invindex = {word: set(txt
#                       for txt, wrds in texts.items() if word in wrds)
#             for word in words}
print('\nInverted Index')
# pp({k: sorted(v) for k, v in invindex.items()})

terms = ["Visiting"]
# print('\nTerm Search for: ' + repr(terms))
# pp(sorted(termsearch(terms)))

from collections import Counter


def termsearch(terms):  # Searches full inverted index
    if not set(terms).issubset(words):
        return set()
    return reduce(set.intersection,
                  (set(x[0] for x in txtindx)
                   for term, txtindx in finvindex.items()
                   if term in terms),
                  set(texts.keys()))


def phrasesearch(phrase):
    wordsinphrase = phrase.strip().strip('"').split()
    if not set(wordsinphrase).issubset(words):
        return set()
    # firstword, *otherwords = wordsinphrase # Only Python 3
    firstword, otherwords = wordsinphrase[0], wordsinphrase[1:]
    found = []
    for txt in termsearch(wordsinphrase):
        # Possible text files
        for firstindx in (indx for t, indx in finvindex[firstword]
                          if t == txt):
            # Over all positions of the first word of the phrase in this txt
            if all((txt, firstindx + 1 + otherindx) in finvindex[otherword]
                   for otherindx, otherword in enumerate(otherwords)):
                found.append(txt)
    return found


finvindex = {word: set((txt, wrdindx)
                       for txt, wrds in texts.items()
                       for wrdindx in (i for i, w in enumerate(wrds) if word == w)
                       if word in wrds)
             for word in words}
print('\nFull Inverted Index')
# pp({k: sorted(v) for k, v in finvindex.items()})

# print('\nTerm Search on full inverted index for: ' + repr(terms))
# pp(sorted(termsearch(terms)))

# phrase = '"Reservation of Seats"'
# print('\nPhrase Search for: ' + phrase)
# print(phrasesearch(phrase))

# Show multiple match capability
phrase = '"කෘෂි හා කාර්මික නිෂ්පාදන සඳහා"'
print('\nPhrase Search for: ' + phrase)
ans = phrasesearch(phrase)
print(ans)
ans = Counter(ans)
print('  The phrase is found most commonly in text: ' + repr(ans.most_common(1)[0][0]))