# Problem:
# -------------
# Suppose you have a weight on one side of a scale. Given an array of other
# weights, see if the scale will balance. You can use weights on either side,
# and you don't have to use all the weights. 


# ----------------------
# HELPER FNS

# recursive fn called by the wrapper fn balanceable()
def balanceable_rec(L, R, weights):

	if (L == 0  or  L==R):   return True
	if (len(weights) == 0):  return False

	w = weights.pop(0)
	if balanceable_rec(L + w, R, weights[:]):  return True
	if balanceable_rec(L, R, weights[:]):	   return True
	if balanceable_rec(L, R + w, weights[:]):  return True

	return False

# wrapper fn
def balanceable(w, weights):
	return balanceable_rec(w, 0, weights)


# ----------------------
# MAIN

weights = [9, 3, 1]
w = 3

if (balanceable(w, weights)):  print("That can be balanced!")
else:			       print("That cannot be balanced!")
