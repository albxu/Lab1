import sys

words = ["load", "store", "loadI", "add", "sub", "mult", "lshift", "rshift", "output", "nop", ',', "=>"]
syntactic_categories = ["MEMOP", "LOADI", "ARITHOP", "OUTPUT", "NOP", "CONSTANT", "REGISTER", "COMMA", "INTO", "EOF", "EOL"]
EOF = False
line_count = 0
line_index = 0 


def scan_line(file):
    global EOF
    global line_count

    # Read the first line
    line = file.readline()

    # End of File
    if line == "":
        EOF = True
        return (9, "")
    
    line = line + '\n'
    
    return line

def scan_word(input_string):
    global line_index
    global line_count

    def next_char():
        global line_index
        line_index += 1
        return input_string[line_index - 1]

    # Read the first character
    c = next_char()

    # get rid of whitespace
    while c == ' ' or c == '\t':
        c = next_char()

    # nop opcode
    if c == 'n':
        c = next_char()
        if c == 'o':
            c = next_char()
            if c == 'p':
                c = next_char()
                if c == ' ':
                    return (4, 9)
                else:
                    return opcode_whitespace_error("nop")
            else:
                return not_a_word_error("no" + c)
        else:
            return not_a_word_error("n" + c)
    
    # lshift, load, and loadI opcodes
    if c == 'l':
        c = next_char()
        if c == 's':
            c = next_char()
            if c == 'h':
                c = next_char()
                if c == 'i':
                    c = next_char()
                    if c == 'f':
                        c = next_char()
                        if c == 't':
                            c = next_char()
                            if c == ' ':
                                return (2, 6)
                            else:
                                return opcode_whitespace_error("lshift")
                        else:
                            return not_a_word_error("lshif" + c)
                    else:
                        return not_a_word_error("lshi" + c)
                else:
                    return not_a_word_error("lsh" + c)
            else:
                return  not_a_word_error("ls" + c)
        elif c == 'o':
            c = next_char()
            if c == 'a':
                c = next_char()
                if c == 'd':
                    c = next_char()
                    if c == ' ':
                        return (0, 0)
                    if c == 'I':
                        c = next_char()
                        if c == ' ':
                            return (1, 2)
                        else:
                            return opcode_whitespace_error("loadI")
                    else:
                        return not_a_word_error("load" + c)
                else:
                    return not_a_word_error("loa" + c)
            else:
                return not_a_word_error("lo" + c)
        else:
            return not_a_word_error("l" + c)
    
    elif c == 's':
        c = next_char()
        if c == 'u':
            c = next_char()
            if c == 'b':
                c = next_char()
                if c == ' ':
                    return (2, 4)
                else:
                    return opcode_whitespace_error("sub")
            else:
                return not_a_word_error("su" + c)
        elif c == 't':
            c = next_char()
            if c == 'o':
                c = next_char()
                if c == 'r':
                    c = next_char()
                    if c == 'e':
                        c = next_char()
                        if c == ' ':
                            return (0, 1)
                        else:
                            return opcode_whitespace_error("store")
                    else:
                        return not_a_word_error("stor" + c)
                else:
                    return not_a_word_error("sto" + c)
            else:
                return not_a_word_error("st" + c)
        else:
            return not_a_word_error("s" + c)
    
    # mult opcode
    elif c == 'm':
        c = next_char()
        if c == 'u':
            c = next_char()
            if c == 'l':
                c = next_char()
                if c == 't':
                    c = next_char()
                    if c == ' ':
                        return (2, 5)
                    else:
                        return opcode_whitespace_error("mult")
                else:
                    return not_a_word_error("mul" + c)
            else:
                return not_a_word_error("mu" + c)
        else:
            return not_a_word_error("m" + c)    
        
    # add opcode
    elif c == 'a':
        c = next_char()
        if c == 'd':
            c = next_char()
            if c == 'd':
                c = next_char()
                if c == ' ':
                    return (2, 3)
                else:
                    return opcode_whitespace_error("add")
            else:
                return not_a_word_error("ad" + c)
        else:
            return not_a_word_error("a" + c)
        
    # rshift opcode
    elif c == 'r':
        c = next_char()
        if c == 's':
            c = next_char()
            if c == 'h':
                c = next_char()
                if c == 'i':
                    c = next_char()
                    if c == 'f':
                        c = next_char()
                        if c == 't':
                            c == next_char()
                            if c == ' ':
                                return (2, 7)
                            else:
                                return opcode_whitespace_error("rshift")
                        else:
                            return not_a_word_error("rshif" + c)
                    else:
                        return not_a_word_error("rshi" + c)
                else:
                    return not_a_word_error("rsh" + c)
            else:
                return not_a_word_error("rs" + c)
        elif c >= '0' and c <= '9':
            n = 0
            while c >= '0' and c <= '9':
                t = int(c)
                c = next_char()
                n = n * 10 + t
            line_index -= 1
            return (6, n)
    
        else:
            return not_a_word_error("r" + c)

    # output opcode
    elif c == 'o':
        c = next_char()
        if c == 'u':
            c = next_char()
            if c == 't':
                c = next_char()
                if c == 'p':
                    c = next_char()
                    if c == 'u':
                        c = next_char()
                        if c == 't':
                            c = next_char()
                            if c == ' ':
                                return (3, 8)
                            else:
                                return opcode_whitespace_error("output")
                        else:
                            return not_a_word_error("outp" + c)
                    else:
                        return not_a_word_error("out" + c)
                else:
                    return not_a_word_error("ou" + c)
            else:
                return not_a_word_error("o" + c)
        else:
            return not_a_word_error("o" + c)
    
    # handle commas
    elif c == ',':
        return (7, ',')
    
    # handle into
    elif c == '=':
        c = next_char()
        if c == '>':
            return (8, "=>")
        else:
            return not_a_word_error("= " + c)

    # handle new lines
    elif c == '\n' or c == '\r\n':
        return (10, 0)
    
    # handle comments
    elif c == '/':
        c = next_char()
        if c == '/':
            return (-1, 0)
        else:
            return not_a_word_error("/" + c)
        
    # handle numbers
    if (c < '0' or c > '9'):
        return not_a_word_error(c)
    else:
        n = 0
        while c >= '0' and c <= '9':
            t = int(c)
            c = next_char()
            n = n * 10 + t
        line_index -= 1
        return (5, n)
        
# handle error messages
# prints an error message based on given word
def opcode_whitespace_error(opcode: str):
    global line_index
    print(f'ERROR {line_count}: expected whitespace after opcode: "{opcode}"', file=sys.stderr)
    line_index -= 1
    return (-1, 0)

def not_a_word_error(word):
    global line_index
    print(f'ERROR {line_count}: "{word}" is not a valid word', file=sys.stderr)
    line_index -= 1
    return (-1, 0)



