#! /usr/bin/python
import re

def is_txt(operand):
    operand = "".join(operand)
    if operand.endswith('.txt'):
        return True
    else:
        return False

def rewrite(default_s, first, second, flag, data):
    #check whether 's' appears at the beginning of the command.  The syntax of the s command is ‘s/regexp/replacement/flags’/
    if default_s == "'s":
        if flag == '':
            output = re.sub(first, second, data, 1)

        #check whether 'digit/g' appears at the end of the string, Replacing all the occurrence of the pattern from the beginning to the nth occurrence
        elif re.search('\dg', flag):
            match_num = int(flag[0])
            output = re.sub(first, second, data, match_num)

        #check whether /g appears at the end of the string, Replacing the all the occurrences of a pattern
        elif re.search('g', flag):
           output = re.sub(first, second, data)

        #checking whethear '/p' appears, Duplicating the replaced lines
        elif re.search('p', flag):
            output = re.sub(first, second, data)
            output = re.split('\n', output)
            double = []
            for line in output:
                double.extend([line, line])
            output = "\n".join(double)

        return output


"""
sed main function. The sed utility is a stream editor that shall read one or more text files, 
make editing changes according to a script of editing commands, and write the results to standard output
"""
def sed():
    while(True):
        usr_input = input("@~: ")
        good_input = True
        usr_input = usr_input.split(" ")
        if usr_input[0] != 'sed':
            good_input = False
            print("bad input.")
        # input_classification, split user input by spacing to a list. for example -> (sed 's/on/forward/' sample.txt).
        command = usr_input[0]
        replacement = usr_input[1]
        if len(usr_input) == 3:
            operand = usr_input[2]
        elif len(usr_input) > 3:
            operand = usr_input[2:]

        else:
            good_input = False
            print("bad input.")


        if good_input:
            '''
            if the operand is text file we will read it as a string, if it not a file -> it just a string
            so we will use it as is;
            '''
            if is_txt(operand) is True:
                with open(operand, "r") as text_file:
                    data = text_file.read()
            else:
                data = " ".join(operand)

            #isolate elements from user inuput
            args = replacement.split('/')
            default_s = args[0]
            first = args[1]
            second = args[2]
            if args[3] == "'":
                flag = ''
            else:
                flag = args[3]

            output = rewrite(default_s, first, second, flag, data)

            if is_txt(operand) is True:
                lines_list = output.split("\n")
                with open(operand, "w") as text_file:
                    for line in lines_list:
                        text_file.write(line)
                        text_file.write('\n')

        print(output)

sed()

