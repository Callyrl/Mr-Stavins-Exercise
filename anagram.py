#%%
def anag(word1, word2): 
    if(sorted(word1) == sorted(word2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings are not anagrams.")          
          
 
word1 = input("Enter a string:")
word2 =input("Enter a string:") 

anag(word1, word2) 
#%%


