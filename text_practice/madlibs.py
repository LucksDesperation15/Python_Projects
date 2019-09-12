import os, re
#Perhaps write some code to allow the user to input there own madlib
# Or better yet create a webscraper and scrape madlibs from a website and then
# randomize which ones you get each time.
print('''Welcome to madlibs!
Please enter your own your word where the words \"ADJECTIVE\", \"NOUN\", \"ADVERB\", or \"VERB\" appear:
 ''')
print('''The ADJECTIVE panda walked to the NOUN and then VERB.
A nearby NOUN was unaffected by these events.
''')
madlib = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

newmadlib = madlib.replace(".", "")
#Need a way to get rid of periods in madlib string.
#newmad = 'The %s panda walked to the %s and then %s. A nearby %s was unaffected by these events.' % ()
words = newmadlib.split()

def isitaword(avn, parts):
    while True:
        if avn.isalpha():
            words[words.index(parts.upper())] = avn
            break
        else:
            print('Please enter a valid word')
            if parts == 'adjective' or parts == 'adverb':
                avn = input('Please enter an %s: ' % parts)
            else:
                avn = input('Please enter a %s: ' % parts)


adj = input('Please enter an adjective: ')
isitaword(adj.lower(), 'adjective')

firstnoun = input('Please enter a noun: ')
isitaword(firstnoun.lower(), 'noun')

verb = input('Please enter a verb: ')
isitaword(verb.lower(), 'verb')

secondnoun = input('Please enter a noun: ')
isitaword(secondnoun.lower(), 'noun')

final = " ".join(words)
capitalRegex = re.findall('([A-Z][a-z]*)', final)
for i in capitalRegex:
    pos = words.index(i)
    if pos == 0:
        continue
    else:
        words[pos - 1] = words[pos - 1] + '.'
usermadlib = " ".join(words)
finalusermadlib = usermadlib + '.'
fname = open('madlibs.txt', 'w')
fname.write('''Original:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.\n
''')
fname.write('Your madlib: \n')
fname.write(finalusermadlib)
fname.close()

#end
