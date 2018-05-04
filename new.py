str1 = 'X-DSPAM-Confidence: 0.8475'


value=float(str1[str1.find(':')+2:len(str1)].strip())

print("Vlaue : "+str(value))
