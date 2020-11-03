#! python3
# stripFunction.py - An alternative function for strip()
import re

text = '  ******With great power comes great responsibilities.****** '
print(text)

def stripIt(text,cut):

    # If second argument is blank, removes all the spaces
    # from start and end.
    
    if cut=='':
        isStartBlank = re.compile(r'^(\s)*')
        mo1 = isStartBlank.sub('', text)

        isEndBlank = re.compile(r'(\s)*$')
        mo2 = isEndBlank.sub('', mo1)

        print('Case 1')
        print(mo2)

    # removes second argument from start and end
    # spaces are automatically removed
    
    else:

        isStartBlank = re.compile(r'^(\s)*')
        mo3 = isStartBlank.sub('', text)

        isEndBlank = re.compile(r'(\s)*$')
        mo4 = isEndBlank.sub('', mo3)
        
        isStartCut = re.compile(cut)
        mo5 = isStartCut.sub('', mo4)

        isEndCut = re.compile(cut)
        mo6 = isEndCut.sub('', mo5)

        print('Case 2:')
        print(mo6)


stripIt(text, '\*')

