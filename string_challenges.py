# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
count = 0
for letter in word:
    if letter.lower() == 'а':
        count +=1
print(count)


# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
voewels ='ауоыэяюёие'
count = 0
for letter in word:
    if letter.lower() in voewels:
        count +=1
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
words = sentence.split()
for word in words:
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
words = sentence.split()
count = []
for word in words:
    count.append(len(word))
print(sum(count)/len(count))