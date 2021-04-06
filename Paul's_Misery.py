'''
Paul is an excellent coder and sits high on the CW leaderboard. He solves kata like a banshee but would also like to lead a normal life, with other activities. 
But he just can't stop solving all the kata!!

Given an array (x) you need to calculate the Paul Misery Score. The values are worth the following points:

kata = 5
Petes kata = 10
life = 0
eating = 1
The Misery Score is the total points gained from the array. Once you have the total, return as follows:

<40 = 'Super happy!'
<70 >=40 = 'Happy!'
<100 >=70 = 'Sad!'
=100 = 'Miserable!'
'''

def paul(x):
    dict = {'kata':5,
            'Petes kata':10,
            'life': 0,
            'eating' : 1
            }
    list_of_scores = []
    for key, value in dict.items():
        for i in x:
            if i == key:
                list_of_scores.append(value)
    if sum(list_of_scores) < 40:
        return 'Super happy!'
    elif 40 <= sum(list_of_scores) <70:
        return 'Happy!'
    elif 70 <= sum(list_of_scores) <100:
        return 'Sad!'
    elif sum(list_of_scores) >= 100:
        return 'Miserable!'
      
      
# See this slightly cleaner solution which uses map() function and cleans elif statements a little bit:

points = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}

def paul(x):
    score = sum(map(points.get, x))
    return (
        'Super happy!' if score < 40 else
        'Happy!' if score < 70 else
        'Sad!' if score < 100 else
        'Miserable!'
    )



