
'''
One of my teammates threw this challenge.
The challenge is simple and is as follows:
------------------------------------------------------------------------
There are n kids with candies. You are given ana integer array candies, where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is True if, after giving the ith kid all the extraCandies, they will have the
greatest number of candies among all the kids, or False otherwise

Example 1:
Input:
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
Output:
    result = [True, True, True, False, True]

Example 2:
Input:
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
Output:
    result = [True, False, False, False, False]
'''


'''
I knew the answer and it was very simple and it is as below
result = [True if (x + extraCandies) >= max(candies) else False for x in candies]

However, I was exploring it and found all possible ways along with some variations.
'''

candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = []
# Traditional way of looping
for c in candies:
    if c + extraCandies >= max(candies):
        result.append(True)
    else:
        result.append(False)

# [True, True, True, False, True]
print('Traditional way of iterating through the list:')
print(f'{result}\n')


# Inline looping
result = [True if (x + extraCandies) >= max(candies) else False for x in candies]
# [True, True, True, False, True]
print('Inline looping over a list:')
print(f'{result}\n')

'''
In the problem, we were given two examples. So I thought I will run this inline loop for both the examples.
One way is to repeat the same code twice or put both the examples into a list... ah no... it cannot be a list,
because, we have different extraCandies for both the examples, so we need to use a dictionary.
'''
candyDict = [
    {'candies' : [2, 3, 5, 1, 3],
     'extraCandies': 3},
    {'candies' : [4, 2, 1, 1, 2],
     'extraCandies': 1},
]

print('Traditional looping over List of Dictionaries and Inline looping over each item: ')
for cd in candyDict:
    result = [True if (x + cd['extraCandies']) >= max(cd['candies']) else False for x in cd['candies']]
    # [True, True, True, False, True]
    # [True, False, False, False, False]
    print(f'{result}')
print()

result = [[True if c + cd['extraCandies'] >= max(cd['candies']) else False for c in cd['candies']] for cd in candyDict]
# [[True, True, True, False, True],
#  [True, False, False, False, False]
# ]
print('Inline looping over the list of dictionaries and its underling data - nested inline: ')
print(f'{result}\n')


'''
Until now, out output is a list. But we do not know which result refers to which set of data. To get that, we need to result a
dictionary as output. And we've added key to the input and the same key will be part of the result
'''
candyDict = [
    {'id' : 'one',
     'candies' : [2, 3, 5, 1, 3],
     'extraCandies': 3},

    {'id' : 'two',
     'candies' : [4, 2, 1, 1, 2],
     'extraCandies': 1},
]

result = [[{cd['id']: True if c + cd['extraCandies'] >= max(cd['candies']) else False} for c in cd['candies']] for cd in candyDict]
# [[{'one': True}, {'one': True}, {'one': True}, {'one': False}, {'one': True}], [{'two': True},
#   {'two': False}, {'two': False}, {'two': False}, {'two': False}
# ]]
print('Inline looping of dictionaries and its underling data, returning key value pair for each result: ')
print(f'{result}\n')

result = [{cd['id']: [True if c + cd['extraCandies'] >= max(cd['candies']) else False for c in cd['candies']]} for cd in candyDict]

print('Inline looping of dictionaries and its underlying data, returning key value per result set: ')
print(f'{result}\n')
# [{'one': [True, True, True, False, True]},
#  {'two': [True, False, False, False, False]}]
