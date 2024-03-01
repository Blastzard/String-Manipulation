def input_gather():
    string = input("Please enter a string: ")
    
    while len(string) < 5:
        string = input("Please enter a string (at least 5 characters): ")
        
    return string

def str_reverse(string):
    print(string[::-1])
    
def char_counter(string):
    index = 0
    vowel = []
    consonant = []
    for character in string:
        
        if string[index].lower() in ('a', 'e', 'i', 'o', 'u'):
            vowel.append(string[index])
            
        elif string[index].upper() in ("A", "E", "I", "O", "U"):
            vowel.append(string[index])
        
        else:
            consonant.append(string[index])
            
        index += 1
    
    return len(vowel), len(consonant)
        
            
        
        