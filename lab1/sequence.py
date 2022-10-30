colorNote = ('rouge', 'bleu')

colorNote= colorNote+('yellow',)
print(colorNote)

phrase=input ("donner une phrase: ")
dictMot= dict()
for i in range (0, len(phrase)-1):
    mot=phrase[i :i + 2]
    if (mot not in dictMot):
        dictMot[mot] = 1
print (dictMot)