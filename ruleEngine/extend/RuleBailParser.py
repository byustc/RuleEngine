from ruleEngine.base.RuleEngineParser import RuleEngineParser


class RuleBailParser(RuleEngineParser):

    def setErrorHandler(self, handler):
        self._errHandler = handler



