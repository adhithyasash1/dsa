'''
Write a function Huffman(s) that accepts a string of characters a,b,c,d,e and f without any space.
The function should generate prefix code for each character based on its frequency in string s and return a 
dictionary where the key represents the character and the corresponding value represents Huffman code for
that character.

Select two smallest frequency nodes each time, if more than 2 nodes have the same 
smallest frequency, then select nodes in the lexicographical order of their symbol.
Assume x and y are the two smallest nodes, then : 

-> if x.frequency < y.frequency then x will always come on the right of the parent node.
-> if x.frequency = y.frequency then the symbol of the node (in lexicographical order) will become the left child, and others will become the right child of the parent node.
-> if x is a left node and y is a right node, then parent node will be identified by x.symbol + y.symbol for further creation of tree.

Example : 

Input : 

s = 'aaaacccbbdddddddeeefffff'
# frequency of each character : 
a - 4
b - 2
c - 3
d - 7
e - 3
f - 5

Output : 

a 111
b 000 
c 001
d 01
e 110
f 01

'''

'''
Huffman Coding

Algorithm : 

1) Calculate the frequency of each character in the string.
2) Sort the characters in increasing order of the frequency.
3) Make each unique character as a leaf node.
4) Create an empty node z. Assign the minimum frequency to the left child of z and assign the second minimum frequency to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.
5) Remove these two minimum frequencies from Q and add the sum into the list of frequencies.
6) Insert node z into the tree.
7) Repeat steps 3 to 5 for all the characters.
8) For each non-leaf node, assign 0 to the left edge and 1 to the right edge.
'''

class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

# Solution        
        
def Huffman(s):
    huffcode = {}
    char = list(s)
    freqlist = []
    unique_char = set(char)
    for c in unique_char:
        freqlist.append((char.count(c),c))
    nodes = []
    for nd in sorted(freqlist):
        nodes.append((nd,Node(nd[0],nd[1])))
    while len(nodes) > 1:
        nodes.sort()
        L = nodes[0][1]
        R = nodes[1][1]
        newnode = Node(L.frequency + R.frequency, L.symbol + R.symbol,L,R)
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(((L.frequency + R.frequency, L.symbol + R.symbol),newnode))

    for ch in unique_char:
        temp = newnode
        code = ''
        while ch != temp.symbol:           
            if ch in temp.left.symbol:
                code += '0'
                temp = temp.left
            else:
                code += '1'
                temp = temp.right
        huffcode[ch] = code   
    return huffcode


s = 'abbcaaaabbcdddeee'
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])

'''
Output : 

a 10
b 01
c 110
d 111
e 00


At each recursive step, extract letters with minimum frequency and replace by composite letter with combined frequency 
Store frequencies in an array  
Linear scan to find minimum values 
|A| = k, number of recursive calls is (k-1)
Complexity is O(k^2)
Instead, maintain frequencies in an heap 
Extracting two minimum frequency letters and adding back compound  letter are both O(logk)
Complexity drops to O(klogk)
'''