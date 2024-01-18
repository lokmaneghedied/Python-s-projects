def arithmetic_arranger(problems,option=None):
    if len(problems) > 5:
        return "Error: Too many problems."

    else:
        top = ''
        bottom = ''
        line = ''
        res = ''
        for x in problems :
            problem = x.split()
            first_num = problem[0]
            operator = problem[1]
            second_num = problem[2]
            if ( len(first_num) > 4 or len(second_num) > 4 ) :
                return "Error: Numbers cannot be more than four digits."
            
            if not first_num.isnumeric() or not second_num.isnumeric():
                return "Error: Numbers must only contain digits."
            
            if operator == '+' or operator == '-':
                if operator == '+' :
                    sum = str(int(first_num) + int(second_num))
                else :
                    sum = str(int(first_num) - int(second_num))
                length = max(len(first_num),len(second_num)) + 2
                topX = str(first_num).rjust(length)
                bottomX = operator + str(second_num).rjust(length - 1)
                lineX = ''
                for i in range(length):
                    lineX +=  '-'
                resX = str(sum).rjust(length)
            else :
                return "Error: Operator must be '+' or '-'."
            if x != problems[-1]:
                top += topX + '    '
                bottom += bottomX + '    '
                line += lineX + '    '
                res += resX + '    '
            else :
                top += topX
                bottom += bottomX
                line += lineX
                res += resX
        top.rstrip()
        bottom.rstrip()
        line.rstrip()
        res.rstrip()
        if option == True:    
            arranged_problems = top + '\n' + bottom + '\n' + line + '\n' + res
        else:
            arranged_problems =  top + '\n' + bottom + '\n' + line
        return arranged_problems



print(arithmetic_arranger('test'))
