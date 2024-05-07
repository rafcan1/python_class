# REGULAR EXPRESSIONS

"""
Allows us to search for and match specific patterns of text
re methods

search method

search(pattern,string, flags=0) --returns a match object if there is a match anywhere in the string
findall(pattern,string, flags=0) --creates a list containing all matches.
split(pattern,string,maxsplit=0, flags=0) --split string by the occurences of pattern and returns a list of them
sub(pattern,repl,string,count=0,flags=0)--replaces one or many matches with a string



import re
if re.search("ab", sys.argv[1]):#if we use it inside if block, returns "match object" or "none"
    print("a match")
else:
    print("no match")
"""
import re
import sys
"""
if re.search("ab", sys.argv[1]):
    print("a match")
else:
    print("not a match")

if re.search("a.b", sys.argv[1]):
    print("a match")
else:
    print("not a match")

if re.search("a..b", sys.argv[1]):
    print("a match")
else:
    print("not a match")

if re.search("a.*b", sys.argv[1]):
    print("a match")
else:
    print("not a match")

if re.search("a.*db", sys.argv[1]):
    print("a match")
else:
    print("not a match")
"""
# USEFUL FUNCTION
text0 = '''Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach its development and deployment with caution and responsibility.'''

text = '''
Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as 
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a 
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, 
including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. 
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable 
of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. 
This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge 
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach 
its development and deployment with caution and responsibility.
'''


def search_pattern(pattern, text):
    result = re.search(pattern, text)
    if result:
        print(result)
        # returns matching string
        print(f"Matching string is '{result.group()}'")
        print(f'located at {result.start()}.End is before {result.end()}')
    else:
        print(f'Pattern "{pattern}" not found')


# search_pattern("that", text)
search_pattern("r.*y", text)
