# Mark Kelly - 02/03/2018 - opening and processing files


with open("data/iris.csv") as f:
  for line in f:
    str0 = (line.split (',')[0])
    str1 = (line.split (',')[1])
    str2 = (line.split (',')[2])
    str3 = (line.split (',')[3])
    print('{0:>3} {1:>3} {2:>3} {3:>3}'.format(str0, str1, str2, str3))
    # I'm creating a string variable for each column and then printing them out for each line in the file.
    # The formatting is aligning the string to the right with 3 characters which is enough for this dataset.
    
