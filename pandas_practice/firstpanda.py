import pandas as pd

events = [8, 13, 18, 22, 31]
my_column = pd.Series(events)
print(my_column)

careers = {'Careers' : ['Data Analyst', 'Backend Developer', 'Computer Programmer', 'App Developer'],
           'Language': ['SQL', 'Python', 'Assembly', 'Java'],
           'Resources': ['YouTube', 'Coursera', 'Books', 'HyperSkill']}

frame_careers = pd.DataFrame(careers)
print(frame_careers)

guess = frame_careers.iloc[1]
print(guess)