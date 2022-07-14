'''
Domino Solitaire
(Indian National Olympiad in Informatics, 2008)

In Domino Solitaire, you have a grid with two rows and many columns. Each square in the grid
contains an integer. You are given a supply of rectangular 2 × 1 tiles, each of which exactly covers
two adjacent squares of the grid. You have to place tiles to cover all the squares in the grid such
that each tile covers two squares and no pair of tiles overlap. The score for a tile is the difference
between the bigger and the smaller number that are covered by the tile. The aim of the game is to
maximize the sum of the scores of all the tiles. Here is an example of a grid, along with two
different tilings and their scores.

The score for Tiling 1 is 12 = (9−8)+(6−2)+(7−1)+(3−2) while the score for Tiling 2 is 6 = (8−6)+(9−7)+
(3−2)+(2−1). There are other tilings possible for this grid, but you can check that Tiling 1 has the
maximum score among all tilings. Your task is to read the grid of numbers and compute the
maximum score that can be achieved by any tiling of the grid.

Solution hint :
Recursively find the best tiling, from left to right. You can start the tiling with one vertical tile or
two horizontal tiles. Use dynamic programming to evaluate the recursive expression efficiently.

Input format
The first line contains one integer N, the number of columns in the grid. This is followed by 2 lines
describing the grid. Each of these lines consists of N integers, separated by blanks.

Output format
A single integer indicating the maximum score that can be achieved by any tiling of the given grid.

Test Data : 
For all inputs, 1 <= N <= 10^5. Each integer in the grid is in the range {0, 1, ..., 10}.
'''

def solve(l1, l2):
	n = len(l1)
	if n == 0:
		return(0)
	ans = [0 for i in range(n+1)]
	ans[n - 1] = max(l1[n - 1],l2[n - 1]) - min(l1[n - 1],l2[n - 1])
	for i in range(n - 2, -1, -1):
		vert = max(l1[i],l2[i]) - min(l1[i],l2[i]) + ans[i + 1]
		horz = (max(l1[i],l1[i + 1]) - min(l1[i],l1[i + 1]) + max(l2[i],l2[i + 1]) - min(l2[i],l2[i + 1])) + ans[i + 2]
		ans[i] = max(vert, horz)
	return(ans[0])

n = int(input())
l1 = [int(i) for i in input().strip().split()]
l2 = [int(i) for i in input().strip().split()]
print(solve(l1, l2))


'''
Input
	4
	8 6 2 3
	9 7 1 2
Output
	12

Input
	10
	68 41 93 60 24 70 23 21 58 65
	54 77 23 96 19 27 21 31 29 75
Output
	349
'''