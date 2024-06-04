import re


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
