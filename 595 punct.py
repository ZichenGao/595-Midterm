import nltk
import string
sentence_data = "The First sentence is about Python!.?\n\nThe Second: about (Django!.?\n\nYou can learn Pyt[hon,Django and Data Ananlysis here.. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print(nltk_tokens)
print(nltk_tokens[1])
print(len(nltk_tokens[1]))
print(len(nltk_tokens))
list1=list(nltk_tokens)
print(list1)

# bracket
def bracket(sentence_data):
    i=sentence_data.find("(")
    if sentence_data.rfind(")")==-1:
        print("Missing bracket",i)

bracket(sentence_data)
#double space

def double_space(sentence_data,nltk_tokens):
    j = sentence_data.find('\n\n')
    if j !=-1:
        print(j)
        for i in range(len(nltk_tokens)):
            a=sentence_data.find('\n\n',j+2,len(sentence_data))
            if a!=-1:
                print(a)
            else:
                break
    else:
        print("No double space")

double_space(sentence_data,nltk_tokens)

#!.?
def find_unexpected(nltk_tokens):
    n=len(nltk_tokens)
    i=0
    for i in range(n):
        if nltk_tokens[i].find("!.?") != -1:
            a=nltk_tokens[i].find("!.?")
            print("Error !.? in tokens",i,"sentence",a)


find_unexpected(nltk_tokens)

#square bracket
def squarebracket(sentence_data):
    i = sentence_data.find("[")
    if sentence_data.rfind("]") == -1:
        print("Missing square bracket", i)

squarebracket(sentence_data)

#double ..
def doubledot(nltk_tokens):
    n=len(nltk_tokens)
    i=0
    for i in range(n):
        if nltk_tokens[i].find("..") != -1:
            a=nltk_tokens[i].find("..")
            print("Error .. in tokens",i,"sentence",a)

doubledot(nltk_tokens)