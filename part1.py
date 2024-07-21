#This is the read_calls function:
#it opens and reads the file
#it splits each line by ':' to separate caller and calles
#then updates the dictionary with caller info
def read_calls(filename):
    call_dict = {}
    
    with open(filename, 'r') as file:
        for line in file:
            names = line.strip().split(':')
            caller = names[0]
            for callee in names[1:]:
                key = (caller, callee)
                call_dict[key] = call_dict.get(key, 0) + 1
    
    return call_dict


#This is the callt1to2 function
#this creates a new dict
#it iterates through the items in the first dict
#orgs the data into new strct
def call1to2(dict1):
    dict2 = {}

    for(caller, callee), count in dict1.items():
        if caller not in dict2:
            dict2[caller] = {}
        dict2[caller][callee] = count

    return dict2
