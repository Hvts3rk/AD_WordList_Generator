import os

'''
        @Author: Giorgio Rando
        @Version: 1.0
        @Descriptio: tool per la creazione di usernames AD's compliant partendo da una
        wordlist, secondo la convenzione: prima_lettera_del_nome+_cognome. 
        Es. John Smith -> jsmith
'''

dic = []
endDict = []
new_String = ""

with open("wordlist_index.txt", "r") as f:
        for x in f.readlines():
                if x[0].isupper():
                        dic.append(x.strip("\n"))
                else:
                        pass

try:
        for y in range(len(dic)):
                new_string = dic[y][0]+dic[y+1]
                endDict.append(new_string.lower())
except:
        print "[!] Un elemento non processato!"
        pass

with open("final_wordlist.txt", "w+") as f:
        for x in endDict:
                f.writelines(x + "\n")

print "[+] Estrazione conclusa con successo! \n Salvo file in: ./final_wordlist.txt"
