## WAP to check if a string is a palindrome
text = input("enter text: ")

start = 0
end = len(text)-1
isPalindrome = True
while start <= end :
    if(text[start] != text[end]):
        isPalindrome = False
        break
    start+=1
    end-=1
    
if(isPalindrome):
    print("palindrome!")
else:
    print("not a palindrome!")