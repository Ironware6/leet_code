#Palindrome Number Solution
#By: Rafael Perez


class Solution(object):
    def isPalindrome(self,g):
      if (g < 0):
        return False
      elif(g >= 0):
        z = [int(x) for x in str(g)]
        if (z == z[::-1]):
          return True
      else:
        return False
