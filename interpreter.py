class Interpreter:
    def __init__(self):
        self.variables = {}
        self.tokens = []
        self.validtokens = ['print',';', 'set','']

    def tokenize(code, self):
        for token in code.split(" "):
            pass

# how to run the tokens?

# example:
# code: print "Hello World";
# tokens:
# [
#    print
#    "Hello World"
# ]
# Output: Hello World!

# TODO: decide to use array or object for tokens.