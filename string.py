def main():
    string=False
    go=True
    while go==True:
        if string==False:
           string=input_gather() 
        else:
            answer=menu()
            if answer=="1":
                string=input_gather()
            elif answer=="2":
                reverse=str_reverse(string)
                print(reverse)
            elif answer=="3":
                vowel=char_counter(string)
                vowel=vowel[0]
                print(vowel)
            elif answer=="4":
                newstring=char_replace(string)
                print(newstring)
            elif answer=="5":
                list1=string_analysis()
                palindrome=list1[0]
                letters=list1[1]
                vowel=list1[2]
                consonants=list1[3]
                print(f"Palindrome: {palindrome}\nAmount of letters: {letters}\nAmount of vowels: {vowel}\nAmount of consonants: {consonants}")
            elif answer=="6":
                go=False
def menu():
    answer=input("What would you like to do?\n1)Input a string \n2)reverse the string\n3)Count vowels\n4)replace characters\n5)Analyze the string\n")
    while answer.isdigit()!=True or int(answer)>5 or int(answer)<1:
        answer=input("What would you like to do?\n1)Input a string \n2)reverse the string\n3)Count vowels\n4)replace characters\n5)Analyze the string\n6)Exit")
    return answer
def char_replace(string):
    go=True
    while go==True
        ch=input("What character would you like to replace")
        ch1=input("What would you like to replace it with")
        newstring=string.replace(ch,ch1)
        if newstring==string:
            print("Sorry that didn't work please try again")
        else:
            go=False
    return newstring