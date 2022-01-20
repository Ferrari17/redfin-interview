# Problem statement
# Given two strings A and B, return true if any substring of A is an anagram of B

# Examples:
# A         B
# -----------------
# Redfin, friend —> true
# Redfin, fred —> true
# Redfin, nerd —> false
# redfin, find —> true
# redfin, finned —> false

def compare (A,B):
  lenB = len(B)
  for i in range(lenB):
    curr = A[i:i+lenB]
    if check(curr,B) == True:
      print("They are anagrams")
      return
  print("They are not anagrams")
  
def check(s1, s2):
  if (sorted(s1)==sorted(s2)):
    return True
  else:
    return False
    
s1 = "Redfin"
s2 = "find"
compare(s1, s2)
