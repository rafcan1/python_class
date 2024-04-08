'''
Exercise 80, file "pp_80.py"
The text is given:
shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'
Write a program that will find and print to the terminal the longest word in the text.
In order to achieve it, implement the function that will delete all '.', ',', get the list of all words,  
use dictionary comprehension to get word:length pairs and use sorted() functio.

Expected result:
The longest word is 'trenches' with the length 8 characters.

'''


def get_longest_word(text: str) -> tuple[str, int]:
    '''
    Function returns the longest word together with its length

    Parameters:
        text: any text
    Returns:

    Exemplary result:
    ('trenches',8)
    '''
    for char in ",.":
        text = text.replace(char, " ")

    words = text.split()
    word_lengths = {word: len(word) for word in words}
    sorted_word_lengths = sorted(
        word_lengths.items(), key=lambda x: x[1], reverse=True)

    longest_word, length = sorted_word_lengths[0]
    return longest_word, length


# Test the function with the provided Shakespeare text
shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beauty\'s field, ....'
longest_word, length = get_longest_word(shakespeare)
print(f"The longest word is '{
      longest_word}' with the length {length} characters.")
