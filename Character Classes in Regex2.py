import re
count = 0
Match_String = 'aDbaa@7baaa923456Eba0'
# Matcher = re.finditer('[a-z]', Match_String)  # Any lower case alphabet symbol
# Matcher = re.finditer('[A-D]', Match_String)    # Any UPPER CASE alphabet symbol
# Matcher = re.finditer('[a-z A-D]', Match_String)   # Any alphabet symbol it may upper/lower case or both
# Matcher = re.finditer('[0-9]', Match_String)        # Any digit
# Matcher = re.finditer('[a-z A-Z 0-9]', Match_String)  # Any Alphanumeric Symbol
Matcher = re.finditer('[^a-z A-Z 0-9]', Match_String)   #Accept any alphanumeric symbol
for Match in Matcher:
    count += 1
    print('Start : {}  ----  End : {} ---- Matched Patters : {}'.format(Match.start(), Match.end(),Match.group()))
print("Number of occurences : ", count)