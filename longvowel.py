#long-long vowels
#extend vowels to the length of 5
word = 'cookies'
num = 0
# Checking for vowels except for the last letter
while num < len(word)-1:
    # checking for vowels and if the next letter is the same
    if (word[num] == 'a' or word[num] == 'e' or word[num] == 'o' or word[num] == 'i' or word[num] == 'u') and word[num+1] == word[num]:
        counter = 0
        #Add three more vowels
        while counter < 4:
            print(word[num], end='')
            counter += 1
    #print the rest of the letters
    else:
        print(word[num], end= '')    
            
    num += 1 
#print the last letter       
print(word[len(word)-1], end='')        