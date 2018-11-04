# Searches for the given pattern string in the given text string using the Knuth-Morris-Pratt string matching algorithm.
# If the pattern is found, this returns the index of the start of the earliest match in 'text'. Otherwise None is returned.
def kmp_search(pattern, text):
	if pattern == "":
		return 0  # Immediate match
	# Compute longest suffix-prefix table
	lsp = [0]  # Base case
	for c in pattern[1 : ]:
		j = lsp[-1]  # Start by assuming we're extending the previous LSP
		while j > 0 and c != pattern[j]:
			j = lsp[j - 1]
		if c == pattern[j]:
			j += 1
		lsp.append(j)

	# Walk through text string
	j = 0  # Number of chars matched in pattern
	for i in range(len(text)):
		while j > 0 and text[i] != pattern[j]:
			j = lsp[j - 1]  # Fall back in the pattern
		if text[i] == pattern[j]:
			j += 1  # Next char matched, increment position
			if j == len(pattern):
				return i - (j - 1)
	retu 


rn None  # Not found
