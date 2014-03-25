def palindrome(str):
	length = len(str)

	# BASE CASE: length is 0 or 1 -- always a palindrome
	if (length < 2):		return True

	# BASE CASE: the 2 ends don't match -- can't be a palindrome
	if (str[0] != str[length - 1]):		return False

	# neither base case was hit -- remove first & last letter, repeat
	else:		return palindrome(str[1:length-1])


# ----------

if palindrome("racecar"):	print("That's a palindrome!")
else:											print("That's NOT a palindrome!")