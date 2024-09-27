def reverseString(s):
    s = str(s)
    res = ''
    for c in s:
        res = c + res
    return res

def twoSum(nums, target):
    length = len(nums)
    for i in range(length-1):
        num1 = num[i]
        for j in range(i + 1, length):
            if num1 + num[j] == target:
                return [i, j]
            
def isPalindrome(x):
    x = str(x)
    if reverseString(x) == x:
        return True
    return False      