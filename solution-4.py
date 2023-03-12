from word2number import w2n
import re

keyWords=['division','multiple','plus','substract','+','-','*','/','=','equals']

regex = '^[0-9]+$'
temp=''

# check string in number or not
def check(string):
    if(re.search(regex, string)):
        return False
         
    else:
        return True

# covert string to number
def convertStringToNumber(string):    
    num = w2n.word_to_num(string)
    return str(num)

# read file
file=open("TMW_small.txt")
lines=file.readlines()

# open write file
output = open("small_output.txt","w")
for i in range(1,len(lines)):
    li=lines[i].split(' ')
    finalString=''
    for i in li:
        
        # break loop at equals
        if(i=='=' or i=='equals'):
            finalString+=(convertStringToNumber(temp) if temp!='' else '')
            temp=''
            break
            
        # check keyword or number      
        if(i not in keyWords and check(i)):
            temp+=i+' '
        else:
            if(i=='division'):
                i='/'
            elif(i=='multiple'):
                i='*'
            elif(i=='substract'):
                i='-'
            elif(i=='plus'):
                i='+'
            elif(i=='equals'):
                i='='
            finalString+=(convertStringToNumber(temp) if temp!='' else '')+' '+i+' '
            temp=''
            
    # check answer is true or false and write answer  
    if(li[len(li)-1].strip()==str(eval(finalString))):
        output.write("true\n")
    else:
        output.write("false\n")   

output.close()
file.close()
