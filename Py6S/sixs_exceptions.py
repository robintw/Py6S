class Error(Exception):
    """Base class for exceptions raised in the process of running 6S."""
    pass

class ParameterError(Error):
    """Exception raised for errors in parameter specifications.
    
    Call as:
    
    ParameterError(parameter_name, message)
    
    """
    
    def __init__(self, param_name, msg):
        self.param_name = param_name
        self.msg = msg
    
    def __str__(self):
        return "%s: %s" % (self.param_name, self.msg)

class OutputParsingError(Error):
    """Exception raised for errors when parsing the 6S output.
    
    Call as:
    
    OutputParsingError(message)
    
    """
    
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
class ExecutionError(Error):
    """Exception raised for errors when running the 6S model.
    
    Call as:
    
    ExecutionError(message)
    
    """
    
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg