"""
def spin_words(sentence):
    reverse_txt = ''
    for word in split_sentence_on_words(sentence):
        if len(word) >= 5:
            reverse_txt += word[::-1] + " "
        elif len(word) < 5:
            reverse_txt += word + " "
    return (reverse_txt.rstrip())

def split_sentence_on_words(sentence):
    splited_text = sentence.split()
    return splited_text
sentence = "Stop spinning my words"
print(spin_words(sentence))

join_splite_text = " ".join(split_sentence_on_words(sentence))
print(join_splite_text)
"""
"""
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

sentence = "Stop spinning my words"
print(spin_words(sentence))
"""
def iq_test(numbers):
    indexEven = 0
    indexOdd = 0
    numEven = 0
    numOdd = 0
    nums = numbers.split(" ")

    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            numEven += 1
            indexEven = i + 1
            print(indexEven)
        else:
            numOdd += 1
            indexOdd = i + 1
numbers = "2 4 6 8 1"
print(iq_test(numbers))
