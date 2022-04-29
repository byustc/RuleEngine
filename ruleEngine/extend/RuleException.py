# -*- coding:utf-8 -*-


class RuleError(Exception):
    """ Unspecified hyper rule error. """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class RuleParameterError(RuleError):
    """ Unspecified hyper rule parameter list error. """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class RuleSyntaxError(RuleError):
    """ Unspecified hyper rule syntax error. """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
