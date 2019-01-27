import sys
#.1 define a function that will take argumentes from the command line 
def rearrange():
    #.2 starting from the second argument to avoid files name
    command_line_arguments_list = sys.argv[1:] 
    #.3 return the arguments arrange in alphabetical order
    return ' '.join(sorted(command_line_arguments_list))

if __name__ == "__main__":
    words = rearrange()
    print(words)