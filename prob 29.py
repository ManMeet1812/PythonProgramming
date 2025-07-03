strng = "Jasson and Japman are my nephews"

def matchstrng(str1):
    if str1 in strng:
        print("Strings matched")
    else:
        print("Strings not matched")
        
matchstrng("Jasson and Japman are my nephews")
matchstrng("J and J are my nephews")