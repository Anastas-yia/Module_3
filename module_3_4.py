# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    root_word = str(root_word).lower()
    other_words = list(other_words)
    lower_other_words = [word.lower() for word in other_words]
    same_words = []
    for i in lower_other_words:
        if root_word in i:
            same_words.append(i)
        elif i in root_word:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('мЕч', 'Мечта', 'зАмечательно', 'еч', 'вода', 'МЕЧи', 'ме', 'семечка')
print(result1)   #['richiest', 'orichalcum', 'richies']
print(result2)   #['Able', 'Disable']
print(result3)



