"""
When I see patterns in my programs, I consider it a sign of trouble. The shape of a
program should reflect only the problem it needs to solve.
--Paul Graham, Lisp hacker and venture capitalist
"""


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence: %s' % self.text


sentence = Sentence('One morning I shot an elephant in my pajamas')

# print(sentence)


# print(sentence[3])

# for word in sentence:
#     print(word)


"""iterable
Any object from which the iter built-in function can obtain an iterator"""

# sentence_iterator = iter(sentence)
# print(sentence_iterator)
# print(next(sentence_iterator))

""" Python obtains iterators from iterables"""

# abc = 'ABC'
# for letter in abc:
#     print(letter)


# it = iter(abc)
# print(it)


# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

"""iterators are also iterable, but iterables are not iterators"""

def get_123():
    print('starting..')
    yield 1
    print('after 1')
    yield 2
    print('after 2')
    yield 3
    print('after 3')
#
# g123 = get_123()
# print(g123)
#
# print(next(g123))
# print(next(g123))
# print(next(g123))
# print(next(g123))

# for number in g123:
#     print(number)
#
# print(next(g123))

# g123 = get_123()
# print(next(g123))
# print(next(g123))

def odd():
    num = 1
    while True:
        yield num
        num += 2
        print('added 2')
#
# godd = odd()
# print(next(godd))
# print(next(godd))
# print(next(godd))

# for n in odds():
#     print(n)


from itertools import count, cycle
#
# cnt = count(1, .5)
# print(next(cnt))
# print(next(cnt))

ccl = cycle([1,2])


