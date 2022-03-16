import pandas as pd

grades_dict = grades_dict = {'Wally': [87,96,70], 'Eva': [100,87,90], 'Sam': [94,77,90],
'Katie':[100,81,82],'Bob':[83,65,85]}

#Series are one-dimensional arrays.
#Dataframes are two-dimensional arrays.
#Each column in a dataframe is a series.

grades = pd.DataFrame(grades_dict)
grades.index = ['Test1','Test2','Test3']

print(grades)

eva = grades['Eva']

sam = grades.Sam

# Using the loc and iloc methods

test2 = grades.loc['Test2']

test1 = grades.iloc[0]

#for consecutive rows

test1_thru_test3 = grades.loc['Test1':'Test3']

#for non-consecutive rows

test1_and_test3 = grades.loc[['Test1','Test3']]

test1_and_test2 = grades.iloc[0:2]

#View only Eva's and Katie's grades for Test1 and Test2

test_EK = grades.loc[:'Test2',['Eva','Katie']]

#View only Sam's THRU Bob's grades for Test1 and Test3

test_SB = grades.iloc[[0,2],2:5]

### Boolean Indexing
# Select everyone with an A grade

gades_A = grades[grades>=90]

#Select everyone with a B grade

grades_B = grades[(grades>=80) & (grades <90)]

#Select everyone with an A or B grade.

grades_A_or_B = grades[(grades>=90)|(grades>=80)]

# by student
pd.set_option('precision',2)

print(grades.describe())

# by test
print(grades.T.describe())

print(grades.T.mean())

# sort rows by their indices (Test name)

r_sorted_grades_i = grades.sort_index(ascending=False)
c_sorted_grades_i = grades.sort_index(axis=1)

print()