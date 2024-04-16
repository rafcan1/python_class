'''
Programming Task 02, file "pt_02.py", score: 10 points

LEARNING DICTIONARY COMPREHESION

Write a program that will print to display a list of tuples that will consist of the most frequent character in the sentence / sentences and it's frequency, 
sorted in a descending order.
In order to complete the task

1. define a function
def get_character_freq(sentence):
    characters_freq = {}
    # your code
    return sorted_characters_freq
and  

def remove_punctuation(text: str, remove_space: bool = False) -> str:


2. As a data structure use a dictionary
3. In your analize, don't use spaces, coma, dots and other punctuations, work on lowers only
4. use count() method of string class to count characters 


Expected result:
[('e', 66), ('t', 56), ('h', 49), ('o', 48), ('s', 39), ('a', 38), ('r', 30), ('n', 27), ('d', 24), 
('u', 22), ('l', 22), ('i', 21), ('w', 16), ('\n', 15), ('m', 13), ('c', 13), ('y', 13), ('f', 12), 
('b', 8), ('g', 5), ('p', 4), ('v', 4), ('k', 2)]
'''


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-.//:;<=>?@[\\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    for char in ",.'!?:;":
        text = text.replace(char, " ")
    return text.lower()


def get_character_freq(sentence: str) -> list[tuple[str, int]]:
    '''
    Function returns list of characters together with its length

    Parameters:
        sentence: any text
    Returns:
        List of tuples
    '''
    characters_freq = {}
    for i in remove_punctuation(sentence, remove_space=True):
        characters_freq[i] = remove_punctuation(
            sentence, remove_space=True).count(i)

    sorted_characters_freq = sorted(
        characters_freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters_freq


sentence = '''
 As fast as thou shalt wane so fast thou grow'st,
  In one of thine, from that which thou departest,
  And that fresh blood which youngly thou bestow'st,
  Thou mayst call thine, when thou from youth convertest,
  Herein lives wisdom, beauty, and increase,
  Without this folly, age, and cold decay,
  If all were minded so, the times should cease,
  And threescore year would make the world away:
  Let those whom nature hath not made for store,
  Harsh, featureless, and rude, barrenly perish:
  Look whom she best endowed, she gave thee more;
  Which bounteous gift thou shouldst in bounty cherish:
    She carved thee for her seal, and meant thereby,
    Thou shouldst print more, not let that copy die.
'''

print(get_character_freq(sentence))
