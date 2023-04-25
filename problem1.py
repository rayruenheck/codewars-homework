import timeit
# # Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# # Rules for a smiling face:

# # Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# # A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# # Every smiling face must have a smiling mouth that should be marked with either ) or D
# # No additional characters are allowed except for those mentioned.

# # Valid smiley face examples: :) :D ;-D :~)
# # Invalid smiley faces: ;( :> :} :]

def count_smileys(arr):
        a=arr.count(':-)')#O(n)
        b=arr.count(':~)')#O(n)
        c=arr.count(':-D')#O(n)
        d=arr.count(':~D')#O(n)
        e=arr.count(':D')#O(n)
        f=arr.count(':)')#O(n)
        g=arr.count(';-)')#O(n)
        h=arr.count(';~)')#O(n)
        i=arr.count(';-D')#O(n)
        j=arr.count(';~D')#O(n)
        k=arr.count(';D')#O(n)
        l=arr.count(';)')#O(n)
        return a + b + c + d + e + f + g + h + i + j + k + l#O(1)
arr = [':)',':(',':D',':O',':;']
#time complexity = O(n) or linear

print(count_smileys([':)',':(',':D',':O',':;']))
print(timeit.timeit('count_smileys(arr)', globals=globals(), number=1000))