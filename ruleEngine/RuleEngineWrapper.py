from antlr4 import InputStream, CommonTokenStream

from ruleEngine.RuleEngineVisitorImpl import RuleEngineVisitorImpl
from ruleEngine.base.RuleEngineLexer import RuleEngineLexer
from ruleEngine.base.RuleEngineParser import RuleEngineParser


def parse_hyper_rule_string(rule: str, init: dict = {}):
    char_stream = InputStream(rule)
    lexer = RuleEngineLexer(char_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RuleEngineParser(token_stream)
    # parser.setErrorHandler(HyperRuleBailErrorStrategy())
    tree = parser.statements()

    visitor = RuleEngineVisitorImpl(init)
    value = visitor.visit(tree)
    return value


class HyperParser(object):
    def __init__(self, init={}):
        self.visitor = RuleEngineVisitorImpl(init)
        self.lexer = RuleEngineLexer()

    def parse(self, rule: str):
        char_stream = InputStream(rule)
        self.lexer.inputStream = char_stream
        parser = RuleEngineParser(CommonTokenStream(self.lexer))
        # parser.setErrorHandler(HyperRuleBailErrorStrategy())
        return self.visitor.visit(parser.statements())
