'''
Write an efficient recursive function constructWord(word, wordList) which returns a list of lists in which all the ways word can be constructed from the elements of wordList. 

Return a empty list if there are no possible ways to constuct word with wordList. Reusing elements of wordList is allowed.
'''

# Solution

memo = {}
def constructWord(word, wordList):
    if word == '':
        return [[]]
    if word in memo.keys():
        return memo[word]
    totalwordlist = []
    for subword in wordList:
        if subword == word[:len(subword)]:
            subwordList = constructWord(word[len(subword):], wordList)
            totalwordlist.extend([[subword] + lst for lst in subwordList])
    memo[word] = totalwordlist
    return totalwordlist


'''
Input
	constructWord('apple', ['ap', 'pple', 'app', 'apl', 'appl', 'le', 'ple'])
Output
	[['ap', 'ple'], ['app', 'le']]

Input
	constructWord('abcabcabcbabcbabcabcabcabcabc',['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
Output
	[['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'b', 'a', 'b', 'c', 'b', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']]

Input
	constructWord('',['is', 'am', 'are'])
Output
	[[]]
'''




