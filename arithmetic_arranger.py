def arithmetic_arranger(problems, value=False):

    firstLine = ''
    secondLine = ''
    totalX = ''
    lines = ''
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    for problem in problems:
        a = problem.split()
        firstIndex = a[0]
        secondIndex = a[2]
        operators = a[1]
    
        if (len(firstIndex) > 4 or len(secondIndex) > 4):
            return "Error: Numbers cannot be more than four digits."

        if not firstIndex.isnumeric() or not secondIndex.isnumeric():
            return "Error: Numbers must only contain digits."

        if (operators == '+' or operators == '-'):
            if operators == "+":
                total = str(int(firstIndex) + int(secondIndex))
            else:
                total = str(int(firstIndex) - int(secondIndex))
            
            lenValues = max(len(firstIndex), len(secondIndex)) + 2
            topValues = str(firstIndex).rjust(lenValues)
            bottomValues = operators + str(secondIndex).rjust(lenValues - 1)
            tempLine = ''
            totalOf = str(total).rjust(lenValues)
            for i in range(lenValues):
                tempLine += '-'
           
            if problem != problems[-1]:
              firstLine += topValues + '    '
              secondLine += bottomValues + '    '
              lines += tempLine + '    '
              totalX += totalOf + '    '
            else:
              firstLine += topValues
              secondLine += bottomValues
              lines += tempLine
              totalX += totalOf
        else:
            return "Error: Operator must be '+' or '-'."
    
    firstLine.rstrip()
    secondLine.rstrip()
    lines.rstrip()
    if value:
        totalX.rstrip()
        arranged_problems = firstLine + '\n' + secondLine + '\n' + lines + '\n' + totalX
    else:
        arranged_problems = firstLine + '\n' + secondLine + '\n' + lines
    return arranged_problems