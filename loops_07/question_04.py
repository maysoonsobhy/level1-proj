
def remove_special(statement):
    new_statement = ""
    for letter in statement:
        if letter.isalnum():
            new_statement=new_statement+letter
    return new_statement
# Main program
ini_str="123abcjw:, .@! eiw"
print(remove_special(ini_str))
