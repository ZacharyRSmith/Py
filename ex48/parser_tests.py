from parser import *

def assert_equal(actual, expected):
    if actual == expected:
        print "True"
    else:
        print "False"

# class ParserError(Exception):
#     pass

def test_sentence():
    sentence = Sentence(('noun', 'I'), ('verb', 'hate'), ('noun', 'pepperoni'))
    assert_equal(sentence.subject, 'I')
    assert_equal(sentence.verb, 'hate')
    assert_equal(sentence.object, 'pepperoni')

print "#test_sentence():"
test_sentence()

# class Sentence(object):

#     def __init__(self, subject, verb, obj):
#         # remember we take ('word_type','word') tuples and convert them
#         self.subject = subject[1]
#         self.verb = verb[1]
#         self.object = obj[1]

def test_match():
    assert_equal(match([('noun', 'Chicken!')], 'noun'), ('noun', 'Chicken!'))
    assert_equal(match([('noun', 'Chicken!')], 'GOLD'), None)
    assert_equal(match(None, 'GOLD'), None)

print "#test_match():"
test_match()

# def match(word_list, expecting):
#     if word_list:
#         word = word_list.pop(0)

#         if word[0] == expecting:
#             return word
#         else:
#             return None
#     else:
#         return None

def test_parse_object():
    assert_equal(parse_object([('stop', 'The'), ('noun', 'Chicken!')]),
                              ('noun', 'Chicken!'))
    assert_equal(parse_object([('stop', 'The'), ('direction', 'North!')]),
                              ('direction', 'North!'))

print "#test_parse_object():"
test_parse_object()

# def parse_object(word_list):
#     skip(word_list, 'stop')
#     next_word = peek(word_list)

#     if next_word == 'noun':
#         return match(word_list, 'noun')
#     elif next_word == 'direction':
#         return match(word_list, 'direction')
#     else:
#         raise ParserError("Expected a noun or direction next.")

def test_parse_sentence():
    sentence = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb,    'run')
    assert_equal(sentence.object,  'north')

    sentence = parse_sentence([('noun', 'bear'), ('verb', 'eat'),
                               ('stop', 'the'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb,    'eat')
    assert_equal(sentence.object,  'honey')

print "#test_parse_sentence():"
test_parse_sentence()

# def parse_sentence(word_list):
#     subj = parse_subject(word_list)
#     verb = parse_verb(word_list)
#     obj = parse_object(word_list)

#     return Sentence(subj, verb, obj)

def test_parse_subject():
    assert_equal(parse_subject([('stop', 'The'), ('noun', 'chicken')]),
                               ('noun', 'chicken'))
    assert_equal(parse_subject([('verb', 'move')]),
                               ('noun', 'player'))

print "#test_parse_subject():"
test_parse_subject()

# def parse_subject(word_list):
#     skip(word_list, 'stop')
#     next_word = peek(word_list)

#     if next_word == 'noun':
#         return match(word_list, 'noun')
#     elif next_word == 'verb':
#         return ('noun', 'player')
#     else:
#         raise ParserError("Expected a verb next.")

def test_parse_verb():
    assert_equal(parse_verb([('stop', 'My'), ('verb', 'move')]),
                 ('verb', 'move'))

print "#test_parse_verb():"
test_parse_verb()

# def parse_verb(word_list):
#     skip(word_list, 'stop')

#     if peek(word_list) == 'verb':
#         return match(word_list, 'verb')
#     else:
#         raise ParserError("Expected a verb next.")

# def peek(word_list):
#     if word_list:
#         word = word_list[0]
#         return word[0]
#     else:
#         return None

# def skip(word_list, word_type):
#     while peek(word_list) == word_type:
#         match(word_list, word_type)