import math

def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a list
        containing the words without punctuation
        from VDH CS111 Final Project.py
    """
    txt = str.lower(txt)        # initialise and clean up text
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('?', '')
    txt = txt.replace('!', '')
    txt = txt.replace(':', '')
    txt = txt.replace(';', '')
    txt = txt.split()           # split txt into words
    
    return txt
    
def stem(s):
    """ accepts a string as a parameter. The function should then return the stem of s
        order of trimmings goes by frequency of usage in english in accordance with
        suffixes: http://www.darke.k12.oh.us/curriculum/la/suffixes.pdf
        prefixes: http://www.darke.k12.oh.us/curriculum/la/suffixes.pdf
        the ones i picked were somewhat arbitrary and based on taste rather than statistical certainty
        from VDH CS111 Final Project.py
    """
    if len(s) > 1:
        if len(s) > 3:
            if s[-1] == 's':        # plural
                s = s[:-1]
        if len(s) > 4:
            if s[-2] == 'ed':       # past tense participle
                if s[-3] == s[-4]:  # eg zapped becomes zap
                    s = s[:-3]
                else:
                    s = s[:-1]      # eg raged becomes rage
            elif s[-3:] == 'ing':   # gerund
                if len(s) < 6:      # some english words end in 'ing' without tense change, eg. 'thing', 'sing'
                    return s
                elif s[:3] == 'kiss' or s[:3] == 'kill' or s[:3] == 'puff' or s[:4] == 'dress' \
                or s[:3] == 'fizz' or s[:3] == 'buzz':
                    s = s[:-3]
                elif s[-4] == s[-5]:    # if the two letters before 'ing' are the same, as in 'planning'
                    s = s[:-4]          # cut off one of the dupicates and 'ing'
                else:                   # if word is a true simple present participle, slice 'ing'
                    s = s[:-3]
            elif s[-2] == 'ly':     # characteristic of: 'excitedly'
                s = s[:-2]
            elif s[-4:] == 'ness':  # condition of: 'happiness'
                s = s[:-4]
            elif s[-3:] == 'ful':   # full of: 'hopeful'
                s = s[:-3]
            elif s[-4:] == 'less':  # without: 'hopeless'
                s = s[:-4]

    # prefixes
    if s[:1] == 'un':
        s = s[2:]
    elif s[:1] == 're':
        s = s[2:]
    elif s[:2] == 'dis' or s[:1] == 'dys':
        s = s[2:]
    elif s[:2] == 'non':
        s = s[3:]
    elif s[:2] == 'pre':
        s = s[3:]
    elif s[:3] == 'anti':
        s = s[5:]

    return s
