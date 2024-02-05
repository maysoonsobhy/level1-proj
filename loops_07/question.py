def rev_statement(statement):
    words = statement.split(" ")
    reverse_statement = ' '.join(reversed(words))
    return reverse_statement

input = "i like this program very much"
print(rev_statement(input))