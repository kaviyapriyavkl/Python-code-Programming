def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    k_scr,s_scr=0,0
    for i in range(len(string)):
        if(string[i]in vowels):
            k_scr+=len(string)-i
        else:
            s_scr+=len(string)-i
    if(k_scr<s_scr):
        print("Stuart",s_scr)
    elif(k_scr>s_scr):
        print("Kevin",k_scr)
    else:
        print("Draw")
            
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)