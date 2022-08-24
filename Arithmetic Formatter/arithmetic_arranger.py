
def arithmetic_arranger(problems, solve = False):
  limit = 5
  arranged_problems = ''
  line1 = ''
  line2 = ''
  line3 = ''
  answer = ''
  
  #check format
  if len(problems) > limit:
    return 'Error: Too many problems.'

  for i in range(len(problems)):
    #print(problems[i])
    #operation.append(problems[i].split(' '))
    operation = problems[i].split(' ')

    if operation[1] != '-' and operation[1] != '+':
      return "Error: Operator must be '+' or '-'."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    
    if operation[0].isdigit() == False or operation[2].isdigit() == False:
      return 'Error: Numbers must only contain digits.'
    #aux_str.append(operation)
    
    #check conversion rules
    gap = max(len(operation[0]),len(operation[2]))+2
    #problems
    if i == 0:
      line1 = f"{operation[0].rjust(gap)}"
      line2 = f"{operation[1]}{operation[2].rjust(gap-1)}"
      line3 = f"{'-'*gap}"
    else: 
      line1 += f"{' '*4}{operation[0].rjust(gap)}"
      line2 += f"{' '*4}{operation[1]}{operation[2].rjust(gap-1)}"
      line3 += f"{' '*4}{'-'*gap}"
    
    #solution
    if solve == True:
      if operation[1] == '+': 
        op = str(int(operation[0])+int(operation[2]))
      elif operation[1] == '-':
        op = str(int(operation[0])-int(operation[2]))
        
      if i == 0:
        answer = f"{op.rjust(gap)}"
      else:
        answer += f"{' '*4}{op.rjust(gap)}"
      
  arranged_problems+=line1 + '\n'
  arranged_problems+=line2 + '\n'
  arranged_problems+=line3
  if solve == True:
    arranged_problems+= '\n'+ answer
  
  return arranged_problems