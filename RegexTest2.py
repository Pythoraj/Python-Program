# We ahve import RE regex module
import re
count = 0       
# We need to convert given pattern in to regex object. 
Pattern = re.compile('Python')

# Need to create Matcher Object
Matcher = Pattern.finditer("Learning Python is very easy")
for match in Matcher:
    count = count+1
    print('Match is available at start index', match.start())

print('The number of occurences is : ', count)