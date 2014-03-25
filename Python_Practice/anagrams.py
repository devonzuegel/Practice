def is_anagram(s1, s2):
	if len(s1) != len(s2):	return False
	if (len(s1) == 0):			return True

	ch = s1[0]
	if ch in s2:
		s1 = s1.replace(ch, "", 1)
		s2 = s2.replace(ch, "", 1)
		return is_anagram(s1, s2)
	else: return False



# --------------------------

if is_anagram("dogs", "gods"):	print("That's an anagram!")
else:														print("That's not an anagram :(")