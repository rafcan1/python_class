# REGEX CONTINUED

"""
RE PATTERNS
METACHARACTERS used inside the patterns are:
". ^ $ * + ? { } [ ] \\ | ( )"
"*" zero or more
"+" one or more
"{2}" exactly two
"^" marks the start. When you use a text, you must turn it into a list of words.
"$" marks the end. When you use a text, you must turn it into a list of words.
"[abc]" a or b or c is enough
"[a-z]" any lowercase letter from the alphabet
"ad?b" d is optional

"""
import re

raw_string = r'/nabc'  # 5 characters, literally
regular_string = '/nabc'  # 4 characters, /n is treated as a single character
# it is recommended to use a raw string when using regex
"""
test_list = ["ab", "adb", "addb", "acb"]
pattern = r'ad*b' #between a and b there can be d, 0 or  more times.
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')

test_list = ["ab", "adb", "addb", "acb"]
pattern = r'ad+b'  # between a and b there can be d, one or more times.
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')

test_list = ["ab", "adb", "addb", "acb"]
pattern = r'ad{2}b'  # between a and b there can be exactly two d
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')

test_list = ["ab", "adb", "addb", "acb"]
pattern = r'^ad'  # if the expression starts with ad, it will match
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')

test_list = ["ab", "adb", "addb", "acb"]
pattern = r'cb$'  # all items that have cb at the end
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')


test_list = ["ab", "adb", "addb", "acb", "ghj"]
pattern = r'[cbk]'  # any of c b or k works
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')
"""
test_list = ["ab", "adb", "addb", "acb"]
pattern = r'ad?b'  # d is optional, 0 or 1 d
for phrase in test_list:
    if re.search(pattern, phrase):
        print(f'"{phrase}" phrase is a match')
    else:
        print(f'"{phrase}" phrase is not a match')

text2 = '''
Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as 
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a 
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, 
including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. 
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable 
of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. 
This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge 
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach 
its development and deployment with caution and responsibility.
Our emails: robdyz@ext.amu.edu.pl, 123avbs@abc.com kasia.dyzman@amu.edu.pl, https://www.google.com, httpds://anglistyka.amu.edu.pl/, http://wp.pl.
Our codes: 61-465, 61465
Our phones: +48 61 123 456, +49-01-321-654, +4861123456
'''


def finditer_pattern(pattern, text):
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match)


def findall_pattern(pattern, text):
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)


# pattern_email = r"[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+"
# pattern_email = r'[\w.-]+@[\w.-]+'
pattern_web = r'https?://(www.)?[\w.]+'
print('\n')
finditer_pattern(pattern_web, text2)
findall_pattern(pattern_web, text2)
