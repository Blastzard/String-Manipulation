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
                list1=string_analysis(string)
                palindrome=list1[0]
                letters=list1[1]
                vowel=list1[2]
                consonants=list1[3]
                print(f"Palindrome: {palindrome}\nAmount of letters: {letters}\nAmount of vowels: {vowel}\nAmount of consonants: {consonants}")
            elif answer=="6":
                go=False
def menu():
    answer=input("What would you like to do?\n1)Input a string \n2)reverse the string\n3)Count vowels\n4)replace characters\n5)Analyze the string\n6)Exit")
    while answer.isdigit()!=True or int(answer)>6 or int(answer)<1:
        answer=input("What would you like to do?\n1)Input a string \n2)reverse the string\n3)Count vowels\n4)replace characters\n5)Analyze the string\n6)Exit")
    return answer
def char_replace(string):
    go=True
    while go==True:
        ch=input("What character would you like to replace: ")
        ch1=input("What would you like to replace it with: ")
        newstring=string.replace(ch.lower(),ch1)
        if newstring==string:
            print("Sorry that didn't work please try again")
        else:
            go=False
    return newstring
def input_gather():
    string = input("Please enter a string: ")
    
    while len(string) < 5:
        string = input("Please enter a string (at least 5 characters): ")
        
    return string

def str_reverse(string):
    reversestring=string[::-1]
    return reversestring
def char_counter(string):
    index = 0
    consonant = ("B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z")
    vowel = ["a","e","i","o","u"]
    vtotal = 0
    ctotal = 0
    for character in string:
        
        for x in vowel:
            
            if character.lower() == x:
                
                vtotal+=1
                
        for y in consonant:
            
            if character.upper() == y:
                
                ctotal+=1
                
    return vtotal, ctotal
              
def string_analysis(string):
    palin="No"
    list2=char_counter(string)
    revstr=str_reverse(string)
    if revstr.lower()==string.lower():
        palin="Yes"
    letters=int(list2[0])+int(list2[1])
    return palin, letters, list2[0], list2[1]
        
        