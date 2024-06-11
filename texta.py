import re
from collections import Counter
import operator
import sqlite3


class TextIO:
    def __init__(self, filepath, startline=0):
        self.filepath = filepath
        self.text = ""
        self.startline = startline

    def get_text(self) -> str:
        return self.text

    def read_from_file(self) -> None:
        with open(self.filepath, "r") as file:
            lines = file.readlines()
            self.text = ''.join(lines[self.startline:])

    def write_to_file(self, text: str, f_path: str, mode: str = "w") -> None:
        with open(f_path, mode) as file:
            file.write(text)


class TextAnalyser:
    def __init__(self, text: str):
        self._text = text
        self._number_of_sentences = None
        self._list_of_sentences = None
        self._list_of_lines = None
        self._number_of_lines = None
        self._searched_phrase = None
        self._is_phrase_a_word = None
        self._lines_with_searched_phrase = None
        self._number_of_searched_phrases = None

    def set_list_of_sentences(self) -> None:
        self._list_of_sentences = re.split(r'[.?!]', self._text)

    def set_number_of_sentences(self) -> None:
        self._number_of_sentences = len(self._list_of_sentences)

    def get_list_of_sentences(self) -> list:
        return self._list_of_sentences

    def get_number_of_sentences(self) -> int:
        return self._number_of_sentences

    def __str__(self):
        return f"TextAnalyser Module v.1.0"

    def set_list_of_lines(self) -> None:
        # Function assigns the instance variable _list_of_lines
        self._list_of_lines = self._text.split('\n')

    def get_list_of_lines(self) -> list:
        # Function returns the list of lines in the "text"
        return self._list_of_lines

    def set_number_of_lines(self) -> None:
        # Function assigns the instance variable _number_of_lines
        self._number_of_lines = len(self._text.split('\n'))

    def get_number_of_lines(self) -> int:
        # Function returns number of lines  in the "text"
        return self._number_of_lines

    def get_searched_phrase(self):
        """
        Function returns the instance variable _searched_phrase
        """
        return self._searched_phrase

    def get_is_phrase_a_word(self, is_word):
        """
        Function returns the instance variable _is_phrase_a_word (bool)
        """
        return self._is_phrase_a_word

    def set_search_phrase_lines(self, phrase: str, isPhraseAWord=True) -> list[str]:
        """
        Function assigns the instance variable _searched_phrase
        Function assigns the instance variable _is_phrase_a_word (bool)
        Function assigns the instance variable _lines_with_searched_phrase
        Phrase is treated as separate word or as an element of another phrase
        Parameters:
            phrase: searched text
            isPhraseAWord: is searched phrase a word or a part of a word
        """
        self._searched_phrase = phrase
        self._is_phrase_a_word = isPhraseAWord
        self._lines_with_searched_phrase = []

        for line in self._list_of_lines:
            if isPhraseAWord:
                if phrase in line.split():
                    self._lines_with_searched_phrase.append(line)
            else:
                if phrase in line:
                    self._lines_with_searched_phrase.append(line)

        return self._lines_with_searched_phrase

    def get_search_phrase_lines(self) -> list[str]:
        """
        Function returns the list of lines containing the given phrase.
        """
        return self._lines_with_searched_phrase

    def set_number_of_searched_phrases(self) -> int:
        """
        Function assigns the instance variable: _number_of_searched_phrases
        (it is not number of lines, we can have several phrases inside a line)
        """
        self._number_of_searched_phrases = self._text.count(
            self._searched_phrase)

    def get_number_of_searched_phrases(self) -> int:
        """
        Function returns the number of occurrences of the given phrase
        """
        return self._number_of_searched_phrases

    def get_most_frequent_words(self) -> list[tuple[str, int]]:
        words = re.findall(r'\b\w+\b', self._text.lower())
        counter = Counter(words)
        return sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

    def get_longest_words(self) -> list[str]:
        # use set to remove duplicates
        words = set(re.findall(r'\b\w+\b', self._text.lower()))
        return sorted(words, key=len, reverse=True)

    def write_search_phrase_lines_to_file(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            for line in self._lines_with_searched_phrase:
                f.write(line + '\n')

    def write_search_phrase_info_to_db(self, db_path: str) -> None:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS search_info
                     (phrase text, occurrences integer)''')
        c.execute("INSERT INTO search_info VALUES (?, ?)",
                  (self._searched_phrase, self._number_of_searched_phrases))
        conn.commit()
        conn.close()
