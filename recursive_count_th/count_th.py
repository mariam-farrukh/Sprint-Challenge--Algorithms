'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    print(word)
    # Base case?
    # if length of the word is less 2 then return the count
    # if the beginning of the word contains 'th', then add to the count and then repeat the recursion
    # have to use : in list style(similar to last week's sprint challenge).
    if len(word) < 2:
        return count
    if word[0:2] == 'th':
        count = count + 1

    # recursively call the function with word[1:]
    # Move up one letter and check if new [0:2] are 'th'.
    return count_th(word[1:], count)
