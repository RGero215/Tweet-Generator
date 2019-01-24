import sys

def rearrange():
    command_line_arguments_list = sys.argv[1:] 
    return ' '.join(sorted(command_line_arguments_list))

if __name__ == "__main__":
    words = rearrange()
    print(words)