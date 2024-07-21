#Given a dictionary where the values are unique, create a new dictionary where the keys become values and the values become keys:

# Question 1: Reverse dictionary
def question1(d):
    return {v: k for k, v in d.items()}

#Exampe on how to use this:
org_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = question1(org_dict)
print(question1)  #The Output should be {1: 'a', 2:'b', 3: 'c'}



#Given a dictionary, create a new dictionary where each value from the original dictionary becomes a key in the new dictionary and its value is a list of keys from the original dictionary that had the same value:

# Question 2: Group by value
def question2(d):
    return {v: [k for k, val in d.items() if val == v] for v in set(d.values())}

#Example usage:
org_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
grouped_dict = question2(org_dict)
print(grouped_dict)



#Given two dictionaries, merge them into a new dictionary. Where keys match, sum their values, assuming all value are numeric
# Question 3: Merge dictionaries
def question3(d1, d2):
    return {k: d1.get(k,0) + d2.get(k, 0) for k in set(d1) | set(d2)}

#Example on how to use
dict1 = {'a': 1, 'b': 2, 'c':3}
dict2 = {'b': 3, 'c':4, 'd': 5}
merged_dict = question3(dict1, dict2)
print(merged_dict)


#Create a list of integers from a nested list structure that appear more than once anywhere in the entire structure
# Question 4: Find duplicates in nested list
def question4(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return list({num for num in flat_list if flat_list.count(num)>1})

#Example in use
nested_list = [[1,2],[3,2],[1,5,3],[6,5]]
duplicates = question4(nested_list)
print(duplicates)
