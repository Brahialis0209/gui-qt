class InputSimplexException(Exception):

    def __init__(self, object_name):
        Exception.__init__(self)
        self.object_name = object_name
        self.message = "Error in input parameters, check: "

    def Message(self):
        return self.message + self.object_name


class SimplexAlgorithmException(Exception):

    def __init__(self):
        Exception.__init__(self)
        self.message = "The objective function is not " \
                       "bounded below on many constraints."

    def Message(self):
        return self.message


class NotSolveSimplex(Exception):

    def __init__(self):
        Exception.__init__(self)
        self.message = "No solutions."

    def Message(self):
        return self.message
