def arithmetic_arranger(*problems):
#get the length
  listLen = len(problems[0])
  if listLen >= 6:
    arranged_problems = "Error: Too many problems."
    return arranged_problems

#seed awnser
  row0 = ''
  row1 = ''
  row2 = ''
#row 4 is the --- line which is 1 + max size of number
  row3 = ''
  row4 = ''
  counter = 0 #counts the postion in the list
  stringlength = 0 #counts the length of the number maxx == 4
  arranged_problems = 'Unknowen Error'
  numberCheck = 0
#this is for awnser and sorting
  num1 = ''
  num2 = ''
  num3 = ''
  sign = ''

  for prob in problems[0]:
    prob = prob.rstrip()
    row0 = row0 + prob + ' '
  rowTemp = row0.split()
#now sort into rows 0,3,6,9,12 (1,4,7,10,13) [2,5,8,11,14]

  for STRnum in rowTemp:
    #check for string length EnvironmentError
    if len(STRnum) >= 5:
      arranged_problems = 'Error: Numbers cannot be more than four digits.'
      return arranged_problems
        
    #checks the first number in the problem
    if counter == 0 or counter % 3 == 0:
      try:
        numberCheck = int(STRnum)
      except:
        arranged_problems = 'Error: Numbers must only contain digits.'
        return arranged_problems
      num1 = STRnum
      stringlength = len(STRnum)
    #this checks for the sign
    elif counter == 1 or counter % 3 == 1:
      if STRnum == '+' or STRnum == '-':
        sign = STRnum
      else:
        arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
        return arranged_problems
    #this is the last number and the spaceing is needed
    else:
      try:
        numberCheck = int(STRnum)
      except:
        arranged_problems = 'Error: Numbers must only contain digits.'
        return arranged_problems
      num2 = STRnum
      #now if true add up the awnserProblems

      #now we find how many spaces and put into a string
      if len(num1) > len(num2):
        numberCheck = len(num1) - len(num2)
        row1 = row1 + '  ' + num1 + '    '
        row2 = row2 + sign + ' ' + (' ' * numberCheck) + num2+'    '
        num3 = '--' + ('-' * len(num1))
        row3 = row3 + num3 +'    '
        try:
          if problems[1] == True and sign == '+':
            row0 = str((int(num1) + int(num2)))
            row4 = row4 +(' ' * (len(num3)-len(row0))) + row0 + '    '
          elif problems[1] == True and sign == '-':
            row0 = str((int(num1) - int(num2)))
            row4 = row4 +(' ' * (len(num3)-len(row0))) + row0 + '    '
          else:
            arranged_problems = 'error in try block of num1 > num2'
        except:
          #do nothing
          pass
      elif len(num1) < len(num2):
        numberCheck = len(num2) - len(num1)
        row1 = row1 + '  ' + (' ' * numberCheck) + num1 + '    '
        row2 = row2 + sign + ' ' + num2+'    '
        num3 = '--' + ('-' * len(num2))
        row3 = row3 + num3 +'    '
        try:
          if problems[1] == True and sign == '+':
            row0 = str((int(num1) + int(num2)))
            row4 = row4 + (' ' * (len(num3)-len(row0))) + row0 + '    '
          elif problems[1] == True and sign == '-':
            row0 = str((int(num1) - int(num2)))
            row4 = row4 + (' ' * (len(num3)-len(row0))) + row0 + '    '
          else:
            arranged_problems = 'error in try block of num1 > num2'
        except:
          #do nothing
          pass
      else:
        numberCheck = len(num2)
        row1 = row1 + '  ' + num1 + '    '
        row2 = row2 + sign + ' ' + num2+'    '
        num3 = '--' + ('-' * len(num2))
        row3 = row3 + num3 +'    '
        try:
          if problems[1] == True and sign == '+':
            row0 = str((int(num1) + int(num2)))
            row4 = row4 + (' ' * (len(num3)-len(row0))) + row0 + '    '
          elif problems[1] == True and sign == '-':
            row0 = str((int(num1) - int(num2)))
            row4 = row4 + (' ' * (len(num3)-len(row0))) + row0 + '    '
          else:
            arranged_problems = 'error in try block of num1 > num2'
        except:
          #do nothing
          pass

    counter = counter + 1

  #now we formate the awnser
  #print(row1)
  #print(row2)
  #print(row3)
  #print(row4)
  row1 = row1.rstrip()
  row2 = row2.rstrip()
  row3 = row3.rstrip()
  arranged_problems = row1 + '\n' + row2 + '\n' + row3
  try:
    if problems[1] is True:
      row4 = row4.rstrip()
      arranged_problems = arranged_problems + '\n' + row4 
  except:
    pass

  return arranged_problems