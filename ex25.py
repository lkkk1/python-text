#coding = utf-8
def break_words(stuff):
    """ This function will break up words for us."""
 #split()用于对字符串进行分割操作
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
#sorted用于对所有可迭代的对象进行排序
    return sorted(words)

def first_word(words):
    """Print the first word after popping it off."""
#list.pop()用于移除列表中的一个元素，并返回该元素的值。默认最后一个
    word = words.pop(0)
    return word

def last_word(words):
    """Print the last word after popping is off."""
#移除列表最后一个值
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
#将句子拆分成单词后对单词排序
    words = break_words(sentence)
    return sort_words(words)

def first_and_last(sentence):
    """Prints the first and last words of the sentence."""
 #打印句子的第一个和最后一个词
    words = break_words(sentence)
    f1 = first_word(words)
    f2 = last_word(words)
    return f1,f2

def first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
#将拆分排序后的句子词组，打印出第一个和最后一个。
    words = sort_sentence(sentence)
    f3 = first_word(words)
    f4 = last_word(words)
    return f3,f4
"""
sentence = "All good things come to those who wait."
print("The first and the last word is %s and %s"%first_and_last(sentence))

print("Sorted:%s"%sort_sentence(sentence))

print("Sorted,first and last one is that %s and %s"%first_and_last_sorted(sentence))
"""