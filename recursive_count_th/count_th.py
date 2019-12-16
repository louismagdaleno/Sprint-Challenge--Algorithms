'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    return count_helper(word, 0)
    
def count_helper(word, count):
    i = word.find('th')

    if i == -1:
        return count

    word = word[0: i:] + word[i+3::]
    count += 1
    return count_helper(word, count)
