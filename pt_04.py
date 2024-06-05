'''
Programming Task 04 (file: pt_04a.py, texta.py)
15 points, 30 min.

1. Create a file "texta.py", it is your new module now
3. Create a file "pt_04a.py"
4. Copy / paste the class definition "TextIO" from  your homework exercise "pp_230.py" to the file "texta.py"
5. Inside "texta.py", create also a class "TextAnalyser"
TextAnalyser specyfication:
5.1 Data attributes:
_text # your text to analyze
_number_of_sentences
_list_of_sentences

5.2 Instance methods to implement
 def __init__(self, text: str):
 def set_list_of_sentences(self) -> None:
 def set_number_of_sentences(self) -> None:
 def get_list_of_sentences(self) -> list:
 def get_number_of_sentences(self) -> int:  
 def __str__(self):
 
Implement complete classes (data attributes and methods) inside texta.py --> now it becomes your module you can import to pt_04 file
TextIO # you can copy from your homework
TextAnalyser # to implement from the beginning

Treat a sentence as a collection of characters ending with ".?!"
Use re.split() method

Using shakespeare.txt, print the results to the terminal

Exemplary result:
        -----------------------------------------
        TextAnalyser Module v.1.0
        -----------------------------------------



Enter the line number from which you want to start analysis: 252
Text File Analysis - PYTHON PROGRAMMING\shakespeare.txt
List of sentences:
1. 1
  From fairest creatures we desire increase,


'''
from texta import TextIO, TextAnalyser


def print_sentences(los, nos):
    '''
    Prints :
    los : list of sentences
    nos : number of sentences
    '''
    print(f"List of sentences: ")
    for i, s in enumerate(los, 1):
        print(f"## {i}. ##\n{s}")
    print(f"Number of sentences: ")
    print(nos)


# Adapt the file path to your situation
file = r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\shakespeare.txt'
try:
    s_line = int(
        input('Enter the line number from which you want to start analysis: '))

    tio = TextIO(file, s_line)
    tio.read_from_file()
    all_text = tio.get_text()
    ta = TextAnalyser(all_text)
    print(ta)  # inside TextAnalyzer class implement the short information banner
    print(f"Text File Analysis - {file}")
    # start of your code
    ta.set_list_of_sentences()
    los = ta.get_list_of_sentences()
    ta.set_number_of_sentences()
    nos = ta.get_number_of_sentences()
    # end of your code
    print_sentences(los, nos)
except ValueError as err:
    print(f"You entered wrong line number, {err}")
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
