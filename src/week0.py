import re, sys

def line_strip(line: str) -> str:
    pattern = re.compile('\/\/[^\/\n]*')
    line = re.sub(pattern, "", line.lower())
    line = re.sub("\s|\n", "", line)
    if len(re.findall("[^a-z]", line)) > 0:
        print("invalid character found!")
        exit(1)
    return line

def file_strip(filepath: str) -> str:
    resulting_program = ""
    file = open(filepath, "r")
    for line in file:
        resulting_program = resulting_program + line_strip(line)
    file.close()
    return resulting_program

if len(sys.argv) != 3:
    print("Invalid amount of parameters!")
    exit(1)
elif sys.argv[1] == "run":
    res = line_strip(sys.argv[2])
    print(res)
elif sys.argv[1] == "file":
    res = file_strip(sys.argv[2])
    print(res)
else:
    print("Unknown parameter")
    exit(1)