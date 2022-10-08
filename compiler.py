class Compiler:
    def __init__(self):
        self.variables = {}
        self.tokens = []
        self.validtokens = []

    def tokenize(code, self):
        for line in code.split("\n"):
            for token in split(" "):
                if token == ";":
                    continue
                