"""  "hi hi hi" -> ["hi hi hi"] and not ["hi" "hi" "hi"]; """
"""   "hey hey hey" -> ["hey hey", "hey"] or ["hey", "hey hey"] but not ["hey", "hey", "hey"]; """
"""    "what a disgusting food" -> ["what a", "disgusting", "food"];  """
"""    "Avadakedavra alohomora" -> ["Avadakedav", "ra", "alohomora"] or alike, but never ["Avadakedav", "ra alohomo", "ra"]. """
"""     No optimizations needed, no ideal solution needed. As simple as it is put here. """
"""  """
"""  """
#Input
str="hi hi hi"
#str="Avadakedavra alohomora"
str="what a disgusting food"
#str="h hi hihi Avadakedavra alohomora ddddddddffffffffffffffffffsdfsdf hi hih dd ss sadfasdfdd"
#str= '''what a disgusting must be hi hi hi 0 01 012 0123 01234 012345 0123456 012345670 01 012 0123 01234 012345 0123456 01234567 012345678 0123456789 01234567890 
012345678901 0123456789012 01234567890123 Avadakedavra alohomora 012345678901234 0123456789012345 01234567890123456789 0123456789012345678901 0 0123456789 012345678 0 012345 
0 01234 012 012 02 01 0 20 0'''


def concatstr(a):
    out=[]
    tmp="" #temp string to concatenate items 
    for item in a:
        if len(item) == 10:
            if tmp:
                out.append(tmp.strip())
                tmp=''
            out.append(item)
        elif len(item) > 10:
            #out.append(item[:10])
            #slice by 10
            if tmp:
                out.append(tmp.strip())
                tmp=''

            out.append(re.findall('(.{1,10})',item)) #add to result
 
        else: #if <10
            if len(tmp)+len(item)>10:
                out.append(tmp.strip())
                tmp=item
            else:
                tmp+=item
             
    out.append(tmp.strip()) #strip out leading and trailing spaces
    #flattened list of arrays for proper output.
    flat_list=[]
    for sublist in out:
        if isinstance(sublist, list)==True:
            for item in sublist:
                flat_list.append(item)
        elif sublist : #removes empty objects
            flat_list.append(sublist)
    
    print ("Result is:\t", flat_list) # output in one line
    print ("Result is:\t")
    for i in flat_list:  
        print ("%10s"%i ) # output in records by 10 




print ("In:\t\t",str)
fields=(re.split('(\s)', str))
concatstr(fields)
