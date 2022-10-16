import re
count = 0
Match_String = "ab1aa@34baaa8ba9"
Matcher = re.finditer('\D', Match_String)      # It will return matched CHARACTER and SPACIAL Symbole only accept Digits.
print("\D [0-9] Accept digit,Remaning all")
for Match in Matcher:
    count +=1
    #print("\S Accept Space Characters")
    print("Start : {} , End : {} , Group : {}".format(Match.start(),Match.end(),Match.group()))
print('Number of occurencess: ',count)