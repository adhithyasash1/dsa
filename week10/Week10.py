'''
Write a Python function BMCount(t, p) that accepts two arguments a text t and a pattern p and
implements a string-matching algorithm based on Boyer-Moore skipping heuristic discussed in
lectures, and returns intermediate steps data as listed below.
	
	--> Record the indexes of the characters in text t that will be matched with the last character of
		p in a list say skipL . skipL is the list of integers sorted in ascending order, where each
		integer is an index of a character in text t .
	
	--> Also count the number of character comparisons performed between t and p in a variable
		say count

and finally return skipL and count from the function in the same order.
'''

# Solution

def BMCount(t,p):
	# Preprocess
	last = {}
	for i in range(len(p)):
		last[p[i]] = i
	poslist,i, count = [], 0, 0 # Loop
	
	while i <= (len(t) - len(p)):
		(matched, j) = (True, len(p) - 1)
		poslist.append(i)
		while j > 0 and matched:
			count += 1
			if t[i + j] != p[j]:
				matched = False
			j -= 1
		if matched:
			i += 1
		else:
			j += 1
			if t[i+j] in last.keys():
				i += max(j-last[t[i+j]],1)
			else:
				i += (j + 1)
	return poslist, count

# Suffix 

t = input()
p = input()
list, c = BMCount(t, p)
print(*list)
print(c)

'''
Input
	lcetcxedt dfashoxdwkevfbiztvrwh xqhjtxntfplurlpkrbpvgehojnkagvqla
	ojnka
Output
	0 5 10 15 16 21 26 31 34 36 41 46 51 55 56
	18

Input
	wrbbphtchnrpnhwqfbppqwweijdgosxztpekucgmgfYDlkBfiqbjgkfzklltmfpgptiuywcpkdzwd
	bmylptppeaash
Output
	0 6 12 18 24 30 32 38 42 43 49 50 56 61 67 69 75 78 84
	25
'''




'''
You are given a string s = s1s2s3...sn , where n is the length of string s, and si is its 
ith character. The prefix of the string s of length l(1 <= l <= n) is string s1s2s3...sl.

Write a function PrefixMatch(s) that accepts a string s and returns a list of all unique
substrings of s[1:] that matches with any prefix of s.

Hint : Use concept of KMP algorithm to write an efficient solution.
'''

# Solution Code

def kmp_fail(p):
	m = len(p)
	fail = [0 for i in range(m)]
	j, k = 1, 0
	
	while j < m:
		if p[j] == p[k]:
			fail[j] = k + 1
			j, k = j + 1, k + 1
		elif k > 0:
			k = fail[k - 1]
		else:
			j += 1
	return(fail)

def PrefixMatch(s):
	res=[]
	if len(s) == 0:
		return res
	
	m = kmp_fail(s)
	
	for i in m:
		if i != 0:
			res.append(s[:i])
	ss = list(set(res))
	return ss

# Suffix 
	
s = input()
print(sorted(PrefixMatch(s)))


'''
Input
	ababa #s
Output
	['a', 'ab', 'aba'] #substrings that matched with prefix of s

	Explanation
		All possible unique substring of s[1:] or baba are b , a , ba , bab , baba , ab , and aba but only
		a , ab , aba matched with prefix of s
	
Input
	abababababababababababa
Output
	['a', 'ab', 'aba', 'abab', 'ababa', 'ababab', 'abababa', 'abababab',
	'ababababa', 'ababababab', 'abababababa', 'abababababab', 'ababababababa',
	'ababababababab', 'abababababababa', 'abababababababab', 'ababababababababa',
	'ababababababababab', 'abababababababababa', 'abababababababababab',
	'ababababababababababa']
'''




'''
A string is called a happy prefix if it is a non-empty prefix which is also a suffix (excluding itself).

Write a function happyPrefix(s) that accept a string s, and returns the longest happy prefix of
s. Return None if no such prefix exists.

Hint - KMP
'''

# Solution

def kmp_fail(p):
	# Initialize
	m = len(p)
	fail = [0 for i in range(m)]
	# Update
	j,k = 1,0
	while j < m:
		if p[j] == p[k]: #k+1 chars match
			fail[j] = k+1
			j,k = j+1,k+1
		elif k > 0: #find shorter prefix
			k = fail[k-1]
		else: #no match found at j
			j = j+1
	return(fail[-1])

def happyPrefix(s):
	if len(s)==0:
		return s
	m = kmp_fail(s)
	if m == 0:
		return None
	else:
		return s[0:m]

'''
Input
	abbcdeghjghjghjgggggggggggggggggggggjjhyyyyyyyyyyyyyyyyyyygfffjjjjjjjjjjjjjjj
	jjjjjjjhgghhhhhgghhhgghgkjkjkkkkkkkkkjhhhhhhhhhhhhhhhhhhhhjjjjjjjjjjjjjjjjjjj
	jjjjjjjjjjjjjjjjjkkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjhjjjjjjjjjjjjjjjjjjjjjjj
	jjjjjjjjjjjjjjjjjjjjjabbcdeghjghjghjgggggggggg
Output
	abbcdeghjghjghjgggggggggg

Input
	abcdefghijaaaaaaaababcdefghij
Output
	abcdefghij

Input
	abcde
Output
	None
'''




'''
Write a method is_accepted(s,start,final,t) that accept a string s , start state start , final
state final and dictionary of transition T and returns True if string s is accepted by finite
automaton, False otherwise.

Format of T :

				{
				(current_state,input_symbol) : next_state,
				..
				..
				}

For below Finite Automaton :

  
  )

q0  ->b
	->c

  ) a

q2  ->b
	->c

( ) a 

q2  ->b
	->c


'''

# Solution

def is_accepted(s,start,final,t):
	state = start
	for char in s:
		if (state,char) not in t:
			return False
		else:
			state = t[(state,char)]
	if state == final:
		return True
	else:
		return False

'''
Input
	aabbaa # s
	q0 # start
	q2 # final
	{('q0','b'):'q0',('q0','c'):'q0',('q0','a'):'q1',('q1','b'):'q1',
	('q1','c'):'q1',('q1','a'):'q2',('q2','b'):'q2',('q2','c'):'q2',
	('q2','a'):'q1'} #t
Output
	True

	# Start with initial state and read input symbol in string s one by one from
	left to right and move according to the given transition T.
	(q0,a)->q1
	(q1,a)->q2
	(q2,b)->q2
	(q2,b)->q2
	(q2,a)->q1
	(q1,a)->q2(last state)
	# After full scan of string, if last state is final state that means string s
	is accepted otherwise not accepted.

Input
	aabbab
	q0
	q2
	{('q0','b'):'q0',('q0','c'):'q0',('q0','a'):'q1',('q1','b'):'q1',
	('q1','c'):'q1',('q1','a'):'q2',('q2','b'):'q2',('q2','c'):'q2',
	('q2','a'):'q1'}
Output
	False

Input
	bbbbbbbbccccccccccccabbbbbbbbbbbcbcbcbcba
	q0
	q2
	{('q0','b'):'q0',('q0','c'):'q0',('q0','a'):'q1',('q1','b'):'q1',
	('q1','c'):'q1',('q1','a'):'q2',('q2','b'):'q2',('q2','c'):'q2',
	('q2','a'):'q1'}
Output
	True
'''




'''
Write a function findAllWords(d, p) that accept a list d of words where each word follows a
CamelCase notation, and the function return the list of all words in list d that matches a given
pattern p of all uppercase characters. Return empty list if pattern not matched.

CamelCase Notation is the practice of writing compound words or phrases joined without spaces,
where each word’s first letter is capitalized. For example, PowerPoint, LibreOffice, CinemaScope,
etc., are in CamelCase.

Hint:- You can use Tries
'''

# Solution

# A class to store a Trie node
class TrieNode:
	def __init__(self):
		self.d = {}
		self.word = []
	
	def insert(head, word):
		if head is None:
			head = TrieNode()
		curr = head
		for c in word:
			if c.isupper():
				if c not in curr.d.keys():
					curr.d[c]= TrieNode()
				curr = curr.d[c]
				curr.word.append(word)
		curr.isLeaf = True
		return head
	
	def findAllWords(dictionary, pattern):
		if not dictionary:
			return []
		head = None
		for s in dictionary:
			head = insert(head, s)
		curr = head
		for c in pattern:
			if c not in curr.d:
				return []
			else:
				curr = curr.d[c]
		return(curr.word)

'''
Input
	['Hi', 'HiTech', 'HiTechCity', 'Techie','TechieDelight', 'Hello',
	'HelloWorld', 'HiTechLab']
	HT
Output
	['HiTech', 'HiTechCity', 'HiTechLab']

Input
	['ActivePerl', 'ActiveSync', 'AdWords', 'AfterStep', 'AirDrop', 'AirPlay',
	'AirPod', 'AirTunes', 'AppKit', 'AppleScript', 'AppleTalk', 'AutoHotkey',
	'BandLab', 'BeagleBoard', 'BitKeeper', 'BitLocker', 'BitWarden',
	'BlackBerry', 'CardSpace', 'CardWorks', 'ChanServ', 'Cl', 'RisWorks',
	'ClearType', 'CloudBox', 'CompactFlash', 'CompuServe', 'ComputerHope',
	'CyberMax', 'DirectDraw', 'DirectX', 'DisplayPort', 'DualShock',
	'DuckDuckGo', 'EarPods', 'EmBootKit', 'EverQuest', 'ExpressCard',
	'ExpressCharge', 'FireWire', 'FiveThirtyEight', 'FoxServ', 'FreePascal',
	'FrontPage', 'GameCube', 'GarageBand', 'GeForce', 'GitHub', 'GlassWire',
	'GoToMyPC', 'GroupMe', 'GroupWare', 'HijackThis', 'HoloLens', 'HydraIRC',
	'HyperCard', 'IdeaPad', 'ImageShack', 'InfoSec', 'IntelliMouse',
	'IntelliTXT', 'JavaScript', 'JavaStation', 'LaserJet', 'LibreOffice',
	'LogMeIn', 'LucasArts', 'MacBook', 'MacPup', 'MacWorks', 'MagSafe', 'McAfee',
	'MicroProse', 'MobileMe', 'MorphOS', 'MultiSync', 'MxToolbox', 'MyCloud',
	'MySQL', 'NetWare', 'NeXT', 'NeXTSTEP', 'NoSQL', 'OneDrive', 'OnLive',
	'OpenGL', 'OpenLinux', 'OpenOffice', 'OpenStack', 'OpenSUSE', 'OpenVMS',
	'OpenWorld', 'OpenZFS', 'OwnCloud', 'PabloDraw', 'PageMaker', 'PageRank',
	'PixelSense', 'PlayStation', 'PostScript', 'PowerBook', 'PowerEdge',
	'PowerPC', 'PowerPoint', 'PowerQuest', 'PowerShell', 'ProtonMail',
	'PureBasic', 'QuickBooks', 'QuickTime', 'RadioShack', 'RamDisk', 'ReactOS',
	'RealNetworks', 'RealPlayer', 'RetailMeNot', 'SanDisk', 'ScanDisk',
	'SharePoint', 'SkyDrive', 'SmartMedia', 'SoundCloud', 'SourceForge',
	'SparkyLinux', 'SpeedStep', 'StarCraft', 'SuperDisk', 'SystemSoft',
	'ThinkPad', 'TinEye', 'TiVo', 'TrueCrypt', 'TrueType', 'TurboTax',
	'UltraWide', 'UnixWare', 'VirtualBox', 'VisiCalc', 'VxWorks', 'WarCraft',
	'WebEx', 'WebOS', 'WhatPulse', 'WinBook', 'WinDirStat', 'WinPopup',
	'WordPad', 'WordPerfect', 'WordStar', 'WorldWideWeb', 'YouTube']
	H
Output
	 ['HijackThis', 'HoloLens', 'HydraIRC', 'HyperCard']


Input
	['Hi', 'HiTech', 'HiTechCity', 'Techie','TechieDelight', 'Hello',
	'HelloWorld', 'HiTechLab']
	HW
Output
	['HelloWorld']
'''




'''
Write a function SuggestCorrectWords(w, d) that accepts an incorrectly spelt word w and a list
d of a predefined set of correct words. The function returns a list of all words from list d which
are at least 70% similar to w . 

For example, if the incorrect spelt word w has 10 characters, then all words in the list d which
are differed by maximum 3 characters to the word w , should be returned for the suggestion.

Sample Input : 
	absant #incorrect word
Output :
	['absent']

d = ['a', 'aachen', 'aardvark', 'aardvarks', 'aaron', 'ab', 'aba', 'ababa',
'abaci', 'aback', 'abactor', 'abactors', 'abacus', 'abacuses', 'abaft',
'abalone', 'abandon', 'abandoned', 'abandonee', 'abandonees', 'abandoning',
'abandonment', 'abandons', 'abase', 'abased', 'abasement', 'abases', 'abash',
'abashed', 'abashes', 'abashing', 'abasing', 'abatable', 'abate', 'abated',
'abatement', 'abatements', 'abater', 'abaters', 'abates', 'abating',
'abator', 'abators', 'abattoir', 'abattoirs', 'abbacies', 'abbacy', 'abbess',
'abbesses', 'abbey', 'abbeys', 'abbot', 'abbots', 'abbotsbury', 'abbott',
'abbreviate', 'abbreviated', 'abbreviates', 'abbreviating', 'abbreviation',
'abbreviations', 'abbreviator', 'abbreviators', 'abc', 'abdicant',
'abdicants', 'abdicate', 'abdicated', 'abdicates', 'abdicating',
'abdication', 'abdications', 'abdicator', 'abdicators', 'abdomen',
'abdomenal', 'abdomens', 'abdominal', 'abdominally', 'abduct', 'abducted',
'abducting', 'abduction', 'abductions', 'abductor', 'abductors', 'abducts',
'abe', 'abeam', 'abearances', 'abecedarian', 'abecedarians', 'abed', 'abel',
'aberaeron', 'aberavon', 'aberdare', 'aberdeen', 'aberdeenshire',
'aberdonian', 'aberdonians', 'aberdovey', 'aberfeldy', 'abergele',
'aberrance', 'aberrancy', 'aberrant', 'aberrate', 'aberration',
'aberrational', 'aberrations', 'abersoch', 'abertillery', 'aberystwyth',
'abet', 'abets', 'abetted', 'abetting', 'abettor', 'abettors', 'abeyance',
'abeyant', 'abhor', 'abhorred', 'abhorrence', 'abhorrent', 'abhorrently',
'abhorrer', 'abhorrers', 'abhorring', 'abhors', 'abidance', 'abide',
'abided', 'abiders', 'abides', 'abiding', 'abidingly', 'abidjan', 'abigail',
'abilities', 'ability', 'abingdon', 'abject', 'abjection', 'abjectly',
'abjuration', 'abjurations', 'abjure', 'abjured', 'abjurer', 'abjurers',
'abjures', 'abjuring', 'ablate', 'ablated', 'ablates', 'ablating',
'ablation', 'ablations', 'ablative', 'ablatives', 'ablaut', 'ablaze', 'able',
'abler', 'ablest', 'abloom', 'ablution', 'ablutions', 'ably', 'abnegate',
'abnegated', 'abnegates', 'abnegating', 'abnegation', 'abnegator',
'abnegators', 'abnormal', 'abnormalities', 'abnormality', 'abnormally',
'aboard', 'abode', 'abodes', 'abolish', 'abolished', 'abolishes',
'abolishing', 'abolishment', 'abolition', 'abolitionism', 'abolitionist',
'abolitionists', 'abominable', 'abominably', 'abominate', 'abominated',
'abominates', 'abominating', 'abomination', 'abominations', 'abominator',
'abominators', 'aboriginal', 'aborigine', 'aborigines', 'abort', 'aborted',
'abortifacient', 'abortifacients', 'aborting', 'abortion', 'abortionist',
'abortionists', 'abortions', 'abortive', 'abortively', 'aborts', 'abortus',
'abound', 'abounded', 'abounding', 'abounds', 'about', 'above',
'aboveground', 'abr', 'abracadabra', 'abrade', 'abraded', 'abrader',
'abraders', 'abrades', 'abrading', 'abraham', 'abrasion', 'abrasions',
'abrasive', 'abrasively', 'abrasives', 'abreaction', 'abreast', 'abridge',
'abridged', 'abridgement', 'abridgements', 'abridger', 'abridgers',
'abridges', 'abridging', 'abridgment', 'abridgments', 'abroad', 'abrogate',
'abrogated', 'abrogates', 'abrogating', 'abrogation', 'abrogator',
'abrogators', 'abrupt', 'abruptly', 'abruptness', 'abscess', 'abscessed',
'abscesses', 'abscise', 'abscised', 'abscises', 'abscising', 'abscissa',
'abscissas', 'abscission', 'abscond', 'absconded', 'absconder', 'absconders',
'absconding', 'absconds', 'abseil', 'abseiled', 'abseiler', 'abseilers',
'abseiling', 'abseils', 'absence', 'absences', 'absent', 'absente',
'absented', 'absentee', 'absenteeism', 'absentees', 'absentia', 'absenting',
'absently', 'absentminded', 'absentmindedly', 'absents', 'absinth',
'absinthe', 'absinthes', 'absinths', 'absolute', 'absolutely',
'absoluteness', 'absolutes', 'absolution', 'absolutions', 'absolutism',
'absolutist', 'absolutists', 'absolve', 'absolved', 'absolver', 'absolvers',
'absolves', 'absolving', 'absorb', 'absorbable', 'absorbed', 'absorbedly',
'absorbencies', 'absorbency', 'absorbent', 'absorbents', 'absorber',
'absorbers', 'absorbing', 'absorbingly', 'absorbs', 'absorption',
'absorptive', 'abstain', 'abstained', 'abstainer', 'abstainers',
3
'abstaining', 'abstains', 'abstemious', 'abstemiously', 'abstention',
'abstentions', 'abstinence', 'abstinent', 'abstinently', 'abstract',
'abstracted', 'abstractedly', 'abstractedness', 'abstracter', 'abstracters',
'abstracting', 'abstraction', 'abstractionism', 'abstractionist',
'abstractionists', 'abstractions', 'abstractive', 'abstractly',
'abstractness', 'abstractor', 'abstractors', 'abstracts', 'abstruse',
'abstrusely', 'abstruseness', 'absurd', 'absurdities', 'absurdity',
'absurdly', 'absurdum', 'abu', 'abuja', 'abundance', 'abundant',
'abundantly', 'abuse', 'abused', 'abuser', 'abusers', 'abuses', 'abusing',
'abusive', 'abusively', 'abusiveness', 'abut', 'abutment', 'abutments',
'abuts', 'abuttals', 'abutted', 'abutter', 'abutters', 'abutting', 'abysm',
'abysmal', 'abysmally', 'abysms', 'abyss', 'abyssal', 'abysses', 'abyssinia',
'abyssinian', 'abyssinians', 'acacia', 'acacias', 'academe', 'academia',
'academic', 'academically', 'academician', 'academicians', 'academics',
'academies', 'academy', 'acanthi', 'acanthus', 'acanthuses', 'acapulco',
'accede', 'acceded', 'accedence', 'acceder', 'acceders', 'accedes',
'acceding', 'accelerate', 'accelerated', 'accelerates', 'accelerating',
'acceleration', 'accelerations', 'accelerator', 'accelerators',
'accelerometer', 'accelerometers', 'accent', 'accented', 'accenting',
'accents', 'accentual', 'accentuate', 'accentuated', 'accentuates',
'accentuating', 'accentuation', 'accept', 'acceptability', 'acceptable',
'acceptably', 'acceptance', 'acceptances', 'acceptant', 'acceptation',
'accepted', 'accepting', 'acceptor', 'acceptors', 'accepts', 'access',
'accessed', 'accesses', 'accessibility', 'accessible', 'accessibly',
'accessing', 'accession', 'accessions', 'accessories', 'accessorise',
'accessorize', 'accessory', 'accidence', 'accidens', 'accident',
'accidental', 'accidentally', 'accidentals', 'accidents', 'acclaim',
'acclaimed', 'acclaiming', 'acclaims', 'acclamation', 'acclamations',
'acclamatory', 'acclimate', 'acclimated', 'acclimates', 'acclimating',
'acclimation', 'acclimatisation', 'acclimatise', 'acclimatised',
'acclimatises', 'acclimatising', 'acclimatization', 'acclimatize',
'acclimatized', 'acclimatizes', 'acclimatizing', 'acclivity', 'accolade',
'accolades', 'accommodate', 'accommodated', 'accommodates', 'accommodating',
'accommodatingly', 'accommodation', 'accommodations', 'accommodative',
'accompanied', 'accompanies', 'accompaniment', 'accompaniments',
'accompanist', 'accompanists', 'accompany', 'accompanying', 'accompli',
'accomplice', 'accomplices', 'accomplish', 'accomplishable', 'accomplished',
'accomplishes', 'accomplishing', 'accomplishment', 'accomplishments',
'accord', 'accordance', 'accordant', 'accorded', 'according', 'accordingly',
'accordion', 'accordionist', 'accordionists', 'accordions', 'accords',
'accost', 'accosted', 'accosting', 'accosts', 'accouchement',
'accouchements', 'account', 'accountabilities', 'accountability',
'accountable', 'accountably', 'accountancies', 'accountancy', 'accountant',
'accountants', 'accounted', 'accounting', 'accountings', 'accounts',
'accouter', 'accoutered', 'accoutering', 'accouterment', 'accouterments',
'accouters', 'accoutre', 'accoutred', 'accoutrement', 'accoutrements',
'accoutres', 'accoutring', 'accra', 'accredit', 'accreditation',
'accredited', 'accrediting', 'accredits', 'accrescendi', 'accrete',
'accreted', 'accretes', 'accreting', 'accretion', 'accretions', 'accrington',
'accruable', 'accrual', 'accruals', 'accrue', 'accrued', 'accrues',
'accruing', 'acculturate', 'acculturated', 'acculturates', 'acculturating',
'acculturation', 'accumulate', 'accumulated', 'accumulates', 'accumulating',
'accumulation', 'accumulations', 'accumulative', 'accumulator',
'accumulators', 'accuracy', 'accurate', 'accurately', 'accurateness',
'accursed', 'accusal', 'accusals', 'accusation', 'accusations', 'accusative',
'accusatives', 'accusatorial', 'accusatory', 'accuse', 'accused', 'accuser',
'accusers', 'accuses', 'accusing', 'accusingly', 'accustom', 'accustomary',
'accustomed', 'accustoming', 'accustoms', 'ace', 'aced', 'acerbate',
'acerbated', 'acerbates', 'acerbating', 'acerbic', 'acerbity', 'aces',
'acetaldehyde', 'acetate', 'acetates', 'acetic', 'acetone', 'acetones',
'acetyl', 'acetylene', 'acetylsalicylic', 'ache', 'ached', 'aches',
'achievable', 'achieve', 'achieved', 'achievement', 'achievements',
'achiever', 'achievers', 'achieves', 'achieving', 'achilles', 'aching',
'achnasheen', 'achromatic', 'achy', 'aciculate', 'acid', 'acidic',
'acidification', 'acidified', 'acidifier', 'acidifiers', 'acidifies',
'acidify', 'acidifying', 'acidity', 'acidly', 'acidosis', 'acids',
'acidulate', 'acidulated', 'acidulates', 'acidulating', 'acidulous', 'acing',
'acknowledge', 'acknowledgeable', 'acknowledged', 'acknowledgement',
'acknowledgements', 'acknowledges', 'acknowledging', 'acknowledgment',
'acknowledgments', 'acme', 'acne', 'acolyte', 'acolytes', 'aconite', 'acorn',
'acorns', 'acoustic', 'acoustical', 'acoustically', 'acoustics', 'acquaint',
'acquaintance', 'acquaintances', 'acquaintanceship', 'acquainted',
'acquainting', 'acquaints', 'acquest', 'acquests', 'acquiesce', 'acquiesced',
'acquiescence', 'acquiescent', 'acquiescently', 'acquiesces', 'acquiescing',
'acquirable', 'acquire', 'acquired', 'acquirement', 'acquirements',
'acquires', 'acquiring', 'acquisition', 'acquisitions', 'acquisitive',
'acquisitively', 'acquisitiveness', 'acquit', 'acquits', 'acquittal',
'acquittals', 'acquittance', 'acquittances', 'acquitted', 'acquitting',
'acre', 'acreage', 'acreages', 'acres', 'acrid', 'acridity', 'acridly',
'acrimonious', 'acrimoniously', 'acrimoniousness', 'acrimony', 'acrobat',
'acrobatic', 'acrobatically', 'acrobatics', 'acrobats', 'acronym',
'acronymic', 'acronyms', 'acrophobia', 'acropolis', 'acropolises', 'across',
'acrostic', 'acrostics', 'acrylic', 'acrylics', 'act', 'acta', 'acte',
'acted', 'actes', 'actin', 'acting', 'actinic', 'actinide', 'actinides',
'actinium', 'action', 'actionable', 'actionably', 'actions', 'activate',
'activated', 'activates', 'activating', 'activation', 'activator',
'activators', 'active', 'actively', 'actives', 'activism', 'activist',
'activists', 'activities', 'activity', 'acton', 'actor', 'actors', 'actress',
'actresses', 'acts', 'actual', 'actualisation', 'actualise', 'actualised',
'actualises', 'actualising', 'actualities', 'actuality', 'actualization',
'actualize', 'actualized', 'actualizes', 'actualizing', 'actually',
'actuals', 'actuarial', 'actuarially', 'actuaries', 'actuary', 'actuate',
'actuated', 'actuates', 'actuating', 'actuation', 'actuator', 'actuators',
'actum', 'actus', 'acuity', 'acumen', 'acupuncture', 'acupuncturist',
'acupuncturists', 'acute', 'acutely', 'acuteness', 'ad', 'ada', 'adage',
'adages', 'adagio', 'adagios', 'adam', 'adamant', 'adamantine', 'adamantly',
'adamants', 'adams', 'adamson', 'adamstown', 'adapt', 'adaptability',
'adaptable', 'adaptation', 'adaptations', 'adapted', 'adapter', 'adapters',
'adapting', 'adaptive', 'adaptively', 'adaptor', 'adaptors', 'adapts', 'add',
'addax', 'addaxes', 'added', 'addend', 'addenda', 'addends', 'addendum',
'adder', 'adders', 'addict', 'addicted', 'addicting', 'addiction',
'addictions', 'addictive', 'addicts', 'adding', 'addis', 'addison',
'addition', 'additional', 'additionally', 'additions', 'additive',
'additives', 'addle', 'addled', 'addles', 'addling', 'address',
'addressable', 'addressed', 'addressee', 'addressees', 'addresser',
'addressers', 'addresses', 'addressing', 'addressograph', 'adds', 'adduce',
'adduced', 'adducer', 'adducers', 'adduces', 'adducing', 'adduct',
'adducted', 'adducting', 'adduction', 'adductive', 'adductor', 'adductors',
'adducts', 'adeem', 'adeemed', 'adeeming', 'adeems', 'adelaide', 'adeline',
'ademption', 'ademptions', 'aden', 'adenine', 'adenines', 'adenoid',
'adenoidal', 'adenoids', 'adenoma', 'adenomas', 'adenosine', 'adept',
'adeptly', 'adeptness', 'adepts', 'adequacies', 'adequacy', 'adequate',
'adequately', 'adhere', 'adhered', 'adherence', 'adherent', 'adherents',
'adheres', 'adhering', 'adhesion', 'adhesions', 'adhesive', 'adhesiveness',
'adhesives', 'adiabatic', 'adidas', 'adieu', 'adieus', 'adieux', 'adios',
'adipocere', 'adipose', 'adiposity', 'adit', 'adits', 'aditus', 'adjacency',
'adjacent', 'adjacently', 'adjectival', 'adjectivally', 'adjective',
'adjectives', 'adjoin', 'adjoined', 'adjoining', 'adjoins', 'adjourn',
'adjourned', 'adjourning', 'adjournment', 'adjournments', 'adjourns',
'adjudge', 'adjudged', 'adjudgement', 'adjudgements', 'adjudges',
'adjudging', 'adjudgment', 'adjudgments', 'adjudicate', 'adjudicated',
'adjudicates', 'adjudicating', 'adjudication', 'adjudications',
'adjudicative', 'adjudicator', 'adjudicators', 'adjunct', 'adjunction',
'adjunctive', 'adjuncts', 'adjuration', 'adjurations', 'adjure', 'adjured',
'adjures', 'adjuring', 'adjust', 'adjustable', 'adjustably', 'adjusted',
'adjuster', 'adjusters', 'adjusting', 'adjustment', 'adjustments', 'adjusts',
'adjutant', 'adjutants', 'adler', 'adman', 'admeasurement', 'administer',
'administered', 'administering', 'administers', 'administrate',
'administrated', 'administrates', 'administrating', 'administration',
'administrations', 'administrative', 'administratively', 'administrator',
'administrators', 'administratrix', 'admirable', 'admirably', 'admiral',
'admirals', 'admiralties', 'admiralty', 'admiration', 'admire', 'admired',
'admirer', 'admirers', 'admires', 'admiring', 'admiringly', 'admissibility',
'admissible', 'admissibly', 'admission', 'admissions', 'admissive', 'admit',
'admits', 'admittance', 'admitted', 'admittedly', 'admitting', 'admix',
'admixed', 'admixes', 'admixing', 'admixture', 'admixtures', 'admonish',
'admonished', 'admonishes', 'admonishing', 'admonishment', 'admonishments',
'admonition', 'admonitions', 'admonitory', 'ado', 'adobe', 'adobes',
'adolescence', 'adolescent', 'adolescents', 'adolph', 'adonis', 'adopt',
'adopted', 'adopter', 'adopters', 'adopting', 'adoption', 'adoptions',
'adoptive', 'adopts', 'adorable', 'adorably', 'adoration', 'adore', 'adored',
'adorer', 'adorers', 'adores', 'adoring', 'adoringly', 'adorn', 'adorned',
'adorning', 'adornment', 'adornments', 'adorns', 'adrenal', 'adrenalin',
'adrenaline', 'adrenals', 'adrian', 'adriatic', 'adrienne', 'adrift',
'adroit', 'adroitly', 'adroitness', 'ads', 'adsorb', 'adsorbed', 'adsorbent',
'adsorbents', 'adsorbing', 'adsorbs', 'adsorption', 'adsorptive', 'adulate',
'adulated', 'adulates', 'adulating', 'adulation', 'adulator', 'adulators',
'adulatory', 'adult', 'adulterant', 'adulterants', 'adulterate',
'adulterated', 'adulterates', 'adulterating', 'adulteration',
'adulterations', 'adulterator', 'adulterators', 'adulterer', 'adulterers',
'adulteress', 'adulteresses', 'adulteries', 'adulterous', 'adulterously',
'adultery', 'adulthood', 'adults', 'adumbrate', 'adumbrated', 'adumbrates',
'adumbrating', 'adumbration', 'adv', 'advance', 'advanced', 'advancement',
'advancements', 'advances', 'advancing', 'advantage', 'advantaged',
'advantageous', 'advantageously', 'advantages', 'advantaging', 'advent',
'adventist', 'adventists', 'adventitious', 'adventitiously', 'advents',
'adventure', 'adventured', 'adventurer', 'adventurers', 'adventures',
'adventuresome', 'adventuring', 'adventurous', 'adventurously',
'adventurousness', 'adverb', 'adverbial', 'adverbially', 'adverbs',
'adversarial', 'adversaries', 'adversary', 'adversative', 'adverse',
'adversely', 'adversities', 'adversity', 'advert', 'adverted', 'adverting',
'advertise', 'advertised', 'advertisement', 'advertisements', 'advertiser',
'advertisers', 'advertises', 'advertising', 'adverts', 'advice', 'advices',
'advisability', 'advisable', 'advise', 'advised', 'advisedly', 'advisee',
'advisement', 'adviser', 'advisers', 'advises', 'advising', 'advisor',
'advisors', 'advisory', 'advocaat', 'advocacy', 'advocate', 'advocated',
'advocates', 'advocating', 'advocator', 'advocators', 'advowson', 'adze',
'adzes', 'ae', 'aegean', 'aegis', 'aeolian', 'aeolians', 'aeon', 'aeons',
'aequum', 'aerate', 'aerated', 'aerates', 'aerating', 'aeration', 'aerator',
'aerators', 'aerial', 'aerialist', 'aerialists', 'aerials', 'aerobatics',
'aerobe', 'aerobes', 'aerobic', 'aerobically', 'aerobics', 'aerodrome',
'aerodromes', 'aerodynamic', 'aerodynamically', 'aerodynamics', 'aerofoil',
'aerogramme', 'aerogrammes', 'aeronaut', 'aeronautic', 'aeronautical',
'aeronautically', 'aeronautics', 'aeronauts', 'aeroplane', 'aeroplanes',
'aerosol', 'aerosols', 'aerospace', 'aerostat', 'aerostatics', 'aerostats',
'aesop', 'aesthete', 'aesthetes', 'aesthetic', 'aesthetically',
'aesthetician', 'aestheticians', 'aestheticism', 'aesthetics', 'aestivate',
'aestivated', 'aestivates', 'aestivating', 'aestivation', 'aetiologies',
'aetiology', 'afar', 'affability', 'affable', 'affably', 'affair', 'affairs',
'affect', 'affectation', 'affectations', 'affected', 'affectedly',
'affectedness', 'affecting', 'affectingly', 'affection', 'affectionate',
'affectionately', 'affections', 'affective', 'affects', 'affeer', 'affeered',
'affeering', 'affeers', 'afferent', 'affiance', 'affianced', 'affiances',
'affiancing', 'affidavit', 'affidavits', 'affiliate', 'affiliated',
'affiliates', 'affiliating', 'affiliation', 'affiliations', 'affinities',
'affinity', 'affirm', 'affirmance', 'affirmances', 'affirmant', 'affirmants',
'affirmata', 'affirmation', 'affirmations', 'affirmative', 'affirmatively',
'affirmatives', 'affirmed', 'affirming', 'affirms', 'affix', 'affixed',
'affixes', 'affixing', 'afflatus', 'afflatuses', 'afflict', 'afflicted',
'afflicting', 'affliction', 'afflictions', 'afflicts', 'affluence',
'affluent', 'affluently', 'afford', 'affordability', 'affordable',
'afforded', 'affording', 'affords', 'afforest', 'afforestation',
'afforested', 'afforesting', 'afforests', 'affray', 'affrays',
'affreightment', 'affreightments', 'affright', 'affrighted', 'affrighting',
'affrights', 'affront', 'affronted', 'affronting', 'affronts', 'afghan',
'afghani', 'afghanis', 'afghanistan', 'afghans', 'aficionado', 'aficionados',
'afield', 'afire', 'aflame', 'afloat', 'aflutter', 'afoot', 'afore',
'aforementioned', 'aforesaid', 'aforethought', 'afoul', 'afraid', 'afresh',
'africa', 'african', 'africans', 'afrikaans', 'afrikaner', 'afrikaners',
'afro', 'afros', 'aft', 'after', 'afterbirth', 'afterbirths', 'afterburner',
'afterburners', 'aftercare', 'afterdeck', 'afterdecks', 'afterglow',
'afterimage', 'afterimages', 'afterlife', 'aftermath', 'afternoon',
'afternoons', 'afters', 'aftershave', 'aftershock', 'aftershocks',
'aftertaste', 'aftertastes', 'afterthought', 'afterthoughts', 'afterward',
'afterwards', 'again', 'against', 'agalma', 'agamemnon', 'agape', 'agar',
'agars', 'agate', 'agates', 'agatha', 'age', 'aged', 'ageing', 'ageism',
'ageless', 'agelessly', 'agelong', 'agencies', 'agency', 'agenda', 'agendas',
'agendum', 'agent', 'agents', 'ager', 'ageratum', 'agers', 'ages',
'agglomerate', 'agglomerated', 'agglomerates', 'agglomerating',
'agglomeration', 'agglomerations', 'agglutinate', 'agglutinated',
'agglutinates', 'agglutinating', 'agglutination', 'agglutinations',
'agglutinative', 'agglutinin', 'aggrandise', 'aggrandised', 'aggrandisement',
'aggrandises', 'aggrandising', 'aggrandize', 'aggrandized', 'aggrandizement',
'aggrandizes', 'aggrandizing', 'aggravate', 'aggravated', 'aggravates',
'aggravating', 'aggravation', 'aggravations', 'aggregate', 'aggregated',
'aggregately', 'aggregates', 'aggregating', 'aggregation', 'aggregations',
'aggress', 'aggressed', 'aggresses', 'aggressing', 'aggression',
'aggressions', 'aggressive', 'aggressively', 'aggressiveness', 'aggressor',
'aggressors', 'aggrieve', 'aggrieved', 'aggrieves', 'aggrieving', 'aggro',
'aghast', 'agile', 'agilely', 'agility', 'aging', 'agio', 'agios', 'agist',
'agisted', 'agister', 'agisters', 'agisting', 'agistment', 'agistments',
'agistor', 'agistors', 'agists', 'agitate', 'agitated', 'agitatedly',
'agitates', 'agitating', 'agitation', 'agitations', 'agitator', 'agitators',
'agleam', 'aglitter', 'aglow', 'agms', 'agnate', 'agnates', 'agnes',
'agnomen', 'agnomens', 'agnomina', 'agnostic', 'agnosticism', 'agnostics',
'ago', 'agog', 'agonies', 'agonise', 'agonised', 'agonises', 'agonising',
'agonisingly', 'agonistic', 'agonistical', 'agonize', 'agonized', 'agonizes',
'agonizing', 'agonizingly', 'agony', 'agoraphobia', 'agoraphobic', 'agotage',
'agouti', 'agouties', 'agoutis', 'agraphia', 'agrarian', 'agrarianism',
'agree', 'agreeable', 'agreeableness', 'agreeably', 'agreed', 'agreeing',
'agreement', 'agreements', 'agreer', 'agrees', 'agribusiness',
'agricultural', 'agriculturalist', 'agriculturalists', 'agriculturally',
'agriculture', 'agriculturist', 'agriculturists', 'agrimony', 'agrochemical',
'agronomic', 'agronomist', 'agronomists', 'agronomy', 'aground', 'ague',
'agues', 'ah', 'aha', 'ahead', 'ahem', 'ahmadabad', 'ahoy', 'ai', 'aia',
'aid', 'aida', 'aide', 'aided', 'aider', 'aiders', 'aides', 'aiding', 'aids',
'aigrette', 'aigrettes', 'aikido', 'ail', 'ailanthus', 'ailanthuses',
'ailed', 'aileron', 'ailerons', 'ailing', 'ailment', 'ailments', 'ails',
'aim', 'aimed', 'aiming', 'aimless', 'aimlessly', 'aimlessness', 'aims',
'aintree', 'air', 'airborne', 'airbrush', 'airbrushed', 'airbrushes',
'airbrushing', 'airbus', 'airbuses', 'aircraft', 'aircrew', 'aircrews',
'airdrie', 'airdrome', 'airdromes', 'airdrop', 'aired', 'airedale',
'airedales', 'aires', 'airfare', 'airfield', 'airfields', 'airflow',
'airfoil', 'airfoils', 'airframe', 'airframes', 'airier', 'airiest',
'airily', 'airiness', 'airing', 'airings', 'airless', 'airlift', 'airlifted',
'airlifting', 'airlifts', 'airline', 'airliner', 'airliners', 'airlines',
'airlock', 'airlocks', 'airmail', 'airman', 'airmen', 'airplane',
'airplanes', 'airplay', 'airport', 'airports', 'airs', 'airship', 'airships',
'airsick', 'airsickness', 'airspace', 'airspeed', 'airspeeds', 'airstrip',
'airstrips', 'airtight', 'airtime', 'airwaves', 'airway', 'airways',
'airworthiness', 'airworthy', 'airy', 'aisle', 'aisles', 'aitken', 'ajar',
'ajax', 'akimbo', 'akin', 'akron', 'al', 'ala', 'alabama', 'alabamian',
'alabaster', 'alacrity', 'aladdin', 'alai', 'alamo', 'alamos', 'alan',
'alarm', 'alarmed', 'alarming', 'alarmingly', 'alarmist', 'alarmists',
'alarms', 'alas', 'alaska', 'alaskan', 'alaskans', 'alb', 'albacore',
'albania', 'albanian', 'albanians', 'albans', 'albany', 'albatross',
'albatrosses', 'albeit', 'albert', 'alberta', 'albinism', 'albino',
'albinos', 'albion', 'albs', 'album', 'albumen', 'albumin', 'albums',
'albuquerque', 'alcalde', 'alcaldes', 'alcatraz', 'alcazar', 'alchemist',
'alchemists', 'alchemy', 'alcms', 'alcohol', 'alcoholic', 'alcoholics',
'alcoholism', 'alcohols', 'alcove', 'alcoves', 'aldborough', 'aldbourne',
'aldburgh', 'aldeburgh', 'alder', 'alderman', 'aldermaston', 'aldermen',
'aldernay', 'alderney', 'alders', 'aldershot', 'ale', 'aleatory', 'alec',
'aleck', 'alecks', 'alehouse', 'alembic', 'alembics', 'aleppo', 'alert',
'alerted', 'alerting', 'alertly', 'alertness', 'alerts', 'ales', 'aleutian',
'aleuts', 'alewife', 'alewives', 'alex', 'alexander', 'alexandra',
'alexandria', 'alexandrian', 'alexandrine', 'alexandrines', 'alexia',
'alexis', 'alfa', 'alfalfa', 'alfas', 'alfred', 'alfresco', 'alga', 'algae',
'algaecide', 'algaecides', 'algarve', 'algebra', 'algebraic',
'algebraically', 'algeria', 'algerian', 'algerians', 'algernon', 'algid',
'algiers', 'alginate', 'alginates', 'algol', 'algorithm', 'algorithmic',
'algorithmically', 'algorithms', 'alhambra', 'alia', 'alias', 'aliases',
'alibi', 'alibis', 'alice', 'alicia', 'alien', 'alienable', 'alienage',
'alienate', 'alienated', 'alienates', 'alienating', 'alienation',
'alienator', 'alienators', 'aliened', 'alienee', 'alienees', 'aliening',
'alienism', 'alienor', 'alienors', 'aliens', 'alight', 'alighted',
'alighting', 'alights', 'align', 'aligned', 'aligning', 'alignment',
'alignments', 'aligns', 'alike', 'aliment', 'alimenta', 'alimentary',
'alimentation', 'aliments', 'alimonies', 'alimony', 'aliphatic', 'aliquem',
'aliquot', 'alison', 'alistair', 'alit', 'aliter', 'aliunde', 'alive',
'alizarin', 'alkali', 'alkaline', 'alkalinise', 'alkalinised', 'alkalinises',
'alkalinising', 'alkalinity', 'alkalinize', 'alkalinized', 'alkalinizes',
'alkalinizing', 'alkalis', 'alkalise', 'alkalised', 'alkalises',
'alkalising', 'alkalize', 'alkalized', 'alkalizing', 'alkaloid', 'alkaloids',
'alkaloses', 'alkalosis', 'alkyd', 'alkyds', 'alkyl', 'alkyls', 'all',
'allah', 'allan', 'allay', 'allayed', 'allaying', 'allayment', 'allays',
'allegata', 'allegation', 'allegations', 'allege', 'alleged', 'allegedly',
'alleges', 'allegiance', 'allegiances', 'alleging', 'allegoric',
'allegorical', 'allegorically', 'allegories', 'allegorise', 'allegorised',
'allegorises', 'allegorising', 'allegorize', 'allegorized', 'allegorizes',
Public Test case
Input 1
'allegorizing', 'allegory', 'allegro', 'allegros', 'allele', 'alleles',
'allelic', 'alleluia', 'alleluias', 'allemande', 'allemandes', 'allen',
'allergen', 'allergenic', 'allergens', 'allergic', 'allergies', 'allergist',
'allergists', 'allergy', 'alleviate', 'alleviated', 'alleviates',
'alleviating', 'alleviation', 'alleviator', 'alleviators', 'alley', 'alleys',
'alleyway', 'alleyways', 'alliance', 'alliances', 'allied', 'allies',
'alligator', 'alligators', 'allison', 'alliterate', 'alliterated',
'alliterates', 'alliterating', 'alliteration', 'alliterations',
'alliterative', 'allocable', 'allocate', 'allocated', 'allocates',
'allocating', 'allocation', 'allocations', 'allocatur', 'allocution',
'allocutions', 'allodial', 'allograph', 'allographs', 'allomorph',
'allomorphic', 'allomorphs', 'allonge', 'allonges', 'allonym', 'allonyms',
'allopathic', 'allophone', 'allophones', 'allophonic', 'allot', 'allotment',
'allotments', 'allotrope', 'allotropes', 'allotropic', 'allotropy', 'allots',
'allotted', 'allottee', 'allottees', 'allotting', 'allow', 'allowable',
'allowably', 'allowance', 'allowances', 'allowed', 'allowing', 'allows',
'alloy', 'alloyed', 'alloying', 'alloys', 'allspice', 'allude', 'alluded',
'alludes', 'alluding', 'allure', 'allured', 'allurement', 'allurements',
'allures', 'alluring', 'alluringly', 'allusion', 'allusions', 'allusive',
'allusively', 'allusiveness', 'alluvia', 'alluvial', 'alluvion', 'alluvium',
'alluviums', 'ally', 'allying', 'alma', 'almanac', 'almanacs', 'almaria',
'almighty', 'almoigne', 'almond', 'almonds', 'almoner', 'almoners', 'almost',
'alms', 'alnmouth', 'alnwick', 'aloe', 'aloes', 'aloft', 'aloha', 'alone',
'aloneness', 'along', 'alongside', 'aloof', 'aloofly', 'aloofness', 'aloud',
'alp', 'alpaca', 'alpacas', 'alpenhorn', 'alpenhorns', 'alpenstock',
'alpenstocks', 'alpha', 'alphabet', 'alphabetic', 'alphabetical',
'alphabetically', 'alphabetisation', 'alphabetise', 'alphabetised',
'alphabetises', 'alphabetising', 'alphabetization', 'alphabetize',
'alphabetized', 'alphabetizes', 'alphabetizing', 'alphabets', 'alphanumeric',
'alphanumerically', 'alphas', 'alpine', 'alpinism', 'alpinist', 'alpinists',
'alps', 'already', 'alright', 'alsace', 'alsatian', 'alsatians', 'also',
'alt', 'altar', 'altarpiece', 'altarpieces', 'altars', 'alter', 'alterable',
'alteration', 'alterations', 'altercate', 'altercated', 'altercates',
'altercating', 'altercation', 'altercations', 'altered', 'altering',
'alterius', 'alternat', 'alternate', 'alternated', 'alternately',
'alternates', 'alternating', 'alternation', 'alternations', 'alternative',
'alternatively', 'alternatives', 'alternator', 'alternators', 'alternats',
'alters', 'althea', 'althorn', 'althorns', 'although', 'altimeter',
'altimeters', 'altitude', 'altitudes', 'alto', 'altocumuli', 'altocumulus',
'altogether', 'alton', 'altos', 'altostrati', 'altostratus', 'altrincham',
'altruism', 'altruist', 'altruistic', 'altruistically', 'altruists', 'alts',
'alum', 'aluminise', 'aluminised', 'aluminises', 'aluminising', 'aluminium',
'aluminize', 'aluminized', 'aluminizes', 'aluminizing', 'aluminum', 'alumna',
'alumnae', 'alumni', 'alumnus', 'alveolar', 'alveoli', 'alveolus', 'alvin',
'always', 'alwinton', 'alyssum', 'alyssums', 'alzheimer']

'''

# Solution

def ED(u,v):
	import numpy as np
	(m,n) = (len(u),len(v))
	ed = np.zeros((m+1,n+1))
	for i in range(m-1,-1,-1):
		ed[i,n] = m-i
	for j in range(n-1,-1,-1):
		ed[m,j] = n-j
	for j in range(n-1,-1,-1):
		for i in range(m-1,-1,-1):
			if u[i] == v[j]:
				ed[i,j] = ed[i+1,j+1]
			else:
				ed[i,j] = 1 + min(ed[i+1,j+1], ed[i,j+1], ed[i+1,j])
	return(ed[0,0])

def SuggestCorrectWords(w,d):
	sw = []
	for word in d:
		if ED(w,word) <= int(len(w)*.3):
			sw.append(word)
	return sw

'''
Input
	blternate
Output
	['altercate', 'alternat', 'alternate', 'alternated', 'alternates',
	'alternats']

Input
	allocte
Output
	['allocate', 'allocated', 'allocates', 'allonge', 'allot', 'allots',
	'allotted', 'allottee']

Input
	aggreeb
Output
	['aggress', 'agree', 'agreed', 'agreer', 'agrees']
'''




'''
Suppose L is a non-empty list of distinct positive integers. 

Write a function Subsequence(L) that
returns a list that contains all such non empty subsequences of the list L in which the elements
are arranged in increasing order.
'''

# Solution

def subseq(L, i = 0, sublist = []):
	if i == len(L):
		if len(sublist) != 0:
			subs.append(sorted(sublist))
	else:
		subseq(L,i+1,sublist)
		subseq(L,i+1,sublist+[L[i]])
	return subs
	
subs = []

def Subsequence(L):
	L.sort()
	return subseq(L)

'''
Input
	[2,4,1,3]
Output
	[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4],
	[2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]

Input
	 [1,2]
Output
	[[1], [1, 2], [2]]

Input
	[1,2,3,4,5]
Output
	[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 5], [1, 2,
	4], [1, 2, 4, 5], [1, 2, 5], [1, 3], [1, 3, 4], [1, 3, 4, 5], [1, 3, 5], [1,
	4], [1, 4, 5], [1, 5], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 5], [2,
	4], [2, 4, 5], [2, 5], [3], [3, 4], [3, 4, 5], [3, 5], [4], [4, 5], [5]]
'''



'''
Write a function findAllwords (d, p) that accept a list d of words where each word follows a CamelCase notation, and the
function return the list of all words in list d that matches a given pattern p of all uppercase characters. Return empty list if
pattern not matched.
CamelCase Notation is the practice of writing compound words or phrases joined without spaces, where each word's first letter
s capitalized. For example, PowerPoint, LibreOffice, CinemaScope, etc., are in CamelCase.

Hint:- You can use Tries
Sample Input 1
['Hi' , 'HiTech' , 'HiTechcity', 'Techie', 'TechieDelight', 'Hello', 'Helloworld', 'HiTechLab' ]

Output
[' Helloworld' ]

Sample Input 2
['Hi' , 'HiTech', 'HiTechcity', 'Techie' , 'TechieDelight' , 'Hello' , 'Helloworld', 'HiTechLab' ]

Output
['HiTech', 'HiTechcity', 'HiTechLab' ]
'''

# A class to store a Trie node
class TrieNode:
    def __init__(self):
        self.d = {}
        self.word = []

def insert(head, word):
    if head is None:
        head = TrieNode()

    curr = head
    for c in word:
        if c.isupper():
            if c not in curr.d.keys():
                curr.d[c]= TrieNode()
            curr = curr.d[c]
            curr.word.append(word)
    curr.isLeaf = True
    return head

def findAllWords(dictionary, pattern):
    if not dictionary:
        return []
    head = None
    for s in dictionary:
        head = insert(head, s)
    curr = head
    for c in pattern:
        if c not in curr.d:
            return []
        else:
            curr = curr.d[c]
    return(curr.word)

d = eval(input())
p = input()
print(findAllWords(d, p))












