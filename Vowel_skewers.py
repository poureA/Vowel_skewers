def Vowel_skewers(seq)->bool :
    '''function docstring'''
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    ALPHABET = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    if seq[0] in alphabet or seq[0] in ALPHABET :
        if seq[-1] in alphabet or seq[-1] in ALPHABET :
            temp_list = seq.split('--')
            if len(temp_list)>=3 :  
                key = True
                for character in temp_list :
                    if character not in alphabet and character not in ALPHABET :
                        return False
                    else :
                        if key is True :
                            if character in 'aeoiu' and character in 'AEOIU' :
                                return False
                            key = False 
                        else :
                            if character not in 'aeoiu' and character not in 'AEOIU'  :
                                return False
                            key = True
                return True
            else :
                return False
        else :
            return False
    else :
        return False
while ask:=input('Enter your text :') :
        print(Vowel_skewers(ask))
