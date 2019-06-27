def reverse(text):
    return text[::-1]

def is_palindrom(text):
    needlessSymbols = ['"', '“', '”', "'", ',', '.', '!', '?', '(', ')', '[', ']', ':', ';', '-', '—', '/', ' ', '\t', '\n']

    updatedText = ''
    for s in text:
        if s not in needlessSymbols:
            updatedText += s.upper()

    #print(updatedText)
    return updatedText == reverse(updatedText)

something = input('Введите текст: ')



if(is_palindrom(something)):
    print('Да, это палиндром.')
else:
    print('Нет, это не палиндром.')
