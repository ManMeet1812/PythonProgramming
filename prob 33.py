def freq(strng):
    word = []
    word = strng.split()
    cnt=0
    for key in word:
        if (key=='little'):
           cnt= word.count(key)
    print(cnt)
            

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")
            
###########################################
def freq(strng, passedkey):
    words=[]
    words=string.split()
    Dict= {}
    
    for key in words:
        if(key == passedkey):
            Dict[key]=words.count(key)
            
    print(Dict)
    
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go", 'little')
    
    