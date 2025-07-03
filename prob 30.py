def freq(str):
    word = []
    word = str.split()
    Dict={}
    
    for key in word:
        Dict[key]= word.count(key)
        
    print("	Frequency of the word is:", Dict)
    
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")
    