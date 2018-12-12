def clean_str(sentence):
    
   
    sentence=sentence.expandtabs(1)
    #print(input)
    #wordlist=input.split()
    #print(wordlist)
    #sentence=''
    #for w in wordlist:   
    #    print(w)
    #    sentence=sentence+' '+w
    #sentence=' '.join(word[0] for word in wordlist)
    sentence=sentence.strip(' ')
    sentence=sentence.strip('.')
    sentence=sentence.strip(';')
    sentence=sentence.strip(',')
    sentence=sentence.replace('%','')
    sentence=sentence.replace('=',' ')
    sentence=sentence.replace(',',', ')
    sentence=sentence.replace(';',' ')
    sentence=sentence.replace(', ',' ')
    sentence=sentence.replace('.',' ')
    sentence=sentence.replace('/',' ')
    sentence=sentence.replace('/ ',' ')
    sentence=sentence.replace('-',' ')
    sentence=sentence.replace('(',' ')
    sentence=sentence.replace(')',' ')
    sentence=sentence.replace(':',' ')
    sentence=sentence.replace('   ',' ')
    sentence=sentence.replace('  ',' ')
    sentence=sentence.lower()
    
    #print(sentence)
    wordlist=sentence.split()
    #print(wordlist)
    #a=wordlist.tolist()
    #print(a)
    #print("clean done")
    return sentence
if __name__ == '__main__':
    #sentence=open('input.txt',encoding='utf-8').read()
    clean_str(sentence)