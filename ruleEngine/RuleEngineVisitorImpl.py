from ruleEngine.base.RuleEngineParser import RuleEngineParser
from ruleEngine.base.RuleEngineVisitor import RuleEngineVisitor
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import math

# define Data Link Escape Character dict
from ruleEngine.extend.RuleException import RuleParameterError, RuleSyntaxError

blank_str_dict = {
    '\\n': '\n',
    '\\f': '\f',
    '\\t': '\t',
    '\\b': '\b',
    '\\r': '\r',
}
real_str_dict = {
    '\\"': '"',
    '\\\\': '\\',
}

date_fmt_dict = {
    'yyyy': '%Y',
    'MM': '%m',
    'dd': '%d',
    'HH': '%H',
    'mm': '%M',
    'ss': '%S',
}


class RuleEngineVisitorImpl(RuleEngineVisitor):

    def __init__(self, init: dict = {}):
        self.vars: dict = init

    def visitStatements(self, ctx: RuleEngineParser.StatementsContext):
        res = None
        for stmtCtx in ctx.statement():
            res = self.visit(stmtCtx)
        return res

    def visitStatements_block(self,
                              ctx: RuleEngineParser.Statements_blockContext):
        return self.visit(ctx.statements())

    def visitExprStmt(self, ctx: RuleEngineParser.ExprStmtContext):
        return self.visit(ctx.expression())

    def visitAssignStmt(self, ctx: RuleEngineParser.AssignStmtContext):
        return self.visit(ctx.assign_statement())

    def visitIfStmt(self, ctx: RuleEngineParser.IfStmtContext):
        return self.visit(ctx.if_statement())

    def visitAssignRef(self, ctx: RuleEngineParser.AssignRefContext):
        name = ctx.REF_VAR().getText()
        value = self.visit(ctx.expression())
        self.vars.update({name: value})
        return value

    def visitAssignLocal(self, ctx: RuleEngineParser.AssignLocalContext):
        name = ctx.LOCAL_VAR().getText()
        value = self.visit(ctx.expression())
        self.vars.update({name: value})
        return value

    def visitIf_statement(self, ctx: RuleEngineParser.If_statementContext):
        res = None
        len_condition = len(ctx.condition())
        for i in range(len_condition):
            condition = self.visit(ctx.condition(i))
            if condition:
                res = self.visit(ctx.condition_branch(i))
                break
        if not res:
            res = self.visit(ctx.condition_branch(len_condition))
        return res

    def visitCondition(self, ctx: RuleEngineParser.ConditionContext):
        return self.visit(ctx.expression())

    def visitBranchStmt(self, ctx: RuleEngineParser.BranchStmtContext):
        return self.visit(ctx.statement())

    def visitBranchBlock(self, ctx: RuleEngineParser.BranchBlockContext):
        return self.visit(ctx.statements_block())

    def visitParalist(self, ctx: RuleEngineParser.ParalistContext):
        res = []
        for item in ctx.para():
            res.append(self.visit(item))
        return res

    def visitPara(self, ctx: RuleEngineParser.ParaContext):
        return self.visit(ctx.expression())

    def visitPow(self, ctx: RuleEngineParser.PowContext):
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(left) not in [int, float]:
            raise RuleSyntaxError(
                '[pow] Left operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int, float]:
            raise RuleSyntaxError(
                '[pow] Right operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(right), right_token.line,
                                 right_token.column + 1))

        return math.pow(left, right)

    def visitUminus(self, ctx: RuleEngineParser.UminusContext):
        exp_token = ctx.expression().start
        exp_value = self.visit(ctx.expression())
        if type(exp_value) not in [int, float]:
            raise RuleSyntaxError(
                '[uminus] The operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(exp_value), exp_token.line,
                                 exp_token.column + 1))
        return -exp_value

    def visitMul(self, ctx: RuleEngineParser.MulContext):
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(left) not in [int, float]:
            raise RuleSyntaxError(
                '[mul] Left operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int, float]:
            raise RuleSyntaxError(
                '[mul] Right operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(right), right_token.line,
                                 right_token.column + 1))

        return left * right

    def visitDiv(self, ctx: RuleEngineParser.DivContext):
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(left) not in [int, float]:
            raise RuleSyntaxError(
                '[div] Left operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int, float]:
            raise RuleSyntaxError(
                '[div] Right operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(right), right_token.line,
                                 right_token.column + 1))
        if right == 0:
            raise RuleSyntaxError(
                '[div] The divider should not be 0! but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(right), right_token.line,
                                 right_token.column + 1))
        return left / right

    def visitFloor_Div(self, ctx: RuleEngineParser.Floor_DivContext):
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(left) not in [int, float]:
            raise RuleSyntaxError(
                '[floor_div] Left operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int, float]:
            raise RuleSyntaxError(
                '[floor_div] Right operand should be a number, but it is type: {0}. at line {1},'
                ' pos {2}'.format(type(right), right_token.line,
                                  right_token.column + 1))
        if right == 0:
            raise RuleSyntaxError(
                '[floor_div] The divider should not be 0! but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(right), right_token.line,
                                 right_token.column + 1))
        return left // right

    def visitMod(self, ctx: RuleEngineParser.ModContext):
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(left) not in [int]:
            raise RuleSyntaxError(
                '[mod] Left operand should be a int, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int]:
            raise RuleSyntaxError(
                '[mod] Right operand should be a int, but it is type: {0}. at line {1},'
                ' pos {2}'.format(type(right), right_token.line,
                                  right_token.column + 1))
        if right == 0:
            raise RuleSyntaxError(
                '[mod] The divider should not be 0! but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(right), right_token.line,
                                 right_token.column + 1))

        return left % right

    def visitSub(self, ctx: RuleEngineParser.SubContext):
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(left) not in [int, float]:
            raise RuleSyntaxError(
                '[sub] Left operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int, float]:
            raise RuleSyntaxError(
                '[sub] Right operand should be a number, but it is type: {0}. at line {1},'
                ' pos {2}'.format(type(right), right_token.line,
                                  right_token.column + 1))
        return left - right

    def visitAdd(self, ctx: RuleEngineParser.AddContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        left_token = ctx.expression(0).start
        right_token = ctx.expression(1).start

        if isinstance(left, str) or isinstance(right, str):
            if type(left) not in [int, float, bool, str]:
                raise RuleSyntaxError(
                    '[add] Left operand should be a number, a string or a boolean, '
                    'but it is type: {0}. at line {1}, '
                    'pos {2}'.format(type(left), left_token.line,
                                     left_token.column + 1))
            if type(right) not in [int, float, bool, str]:
                raise RuleSyntaxError(
                    '[add] Right operand should be a number, a string or a boolean, '
                    'but it is type: {0}. at line {1},'
                    ' pos {2}'.format(type(right), right_token.line,
                                      right_token.column + 1))
            return str(left) + str(right)

        if type(left) not in [int, float]:
            raise RuleSyntaxError(
                '[add] Left operand should be a number, but it is type: {0}. at line {1}, '
                'pos {2}'.format(type(left), left_token.line,
                                 left_token.column + 1))
        if type(right) not in [int, float]:
            raise RuleSyntaxError(
                '[add] Right operand should be a number, but it is type: {0}. at line {1},'
                ' pos {2}'.format(type(right), right_token.line,
                                  right_token.column + 1))

        return left + right

    def visitNot(self, ctx: RuleEngineParser.NotContext):
        res = self.visit(ctx.expression())
        if type(res) not in [None, int, float, str, bool]:
            exp_token = ctx.expression().start
            raise RuleSyntaxError(
                '[not] Expression type error, it is type: {0}. at line {1},'
                ' pos {2}'.format(type(res), exp_token.line,
                                  exp_token.column + 1))
        return False if bool(res) else True

    def visitAnd(self, ctx: RuleEngineParser.AndContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left and right else False

    def visitOr(self, ctx: RuleEngineParser.OrContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left or right else False

    def visitParen(self, ctx: RuleEngineParser.ParenContext):
        return self.visit(ctx.expression())

    def visitRefVar(self, ctx: RuleEngineParser.RefVarContext):
        name = ctx.REF_VAR().getText().replace('$', '')
        if name in self.vars:
            return self.vars[name]
        token = ctx.REF_VAR().symbol
        raise RuleSyntaxError(
            "Reference Variable " + name +
            " is referenced but not initialized. "
            "at line {0}, pos {1}".format(token.line, token.column + 1))

    def visitLocalVar(self, ctx: RuleEngineParser.LocalVarContext):
        name = ctx.LOCAL_VAR().getText()
        if name in self.vars:
            return self.vars[name]

        token = ctx.LOCAL_VAR().symbol
        raise RuleSyntaxError(
            "Local Variable " + name + " is referenced but not initialized. "
            "at line {0}, pos {1}".format(token.line, token.column + 1))

    def visitIntLiteral(self, ctx: RuleEngineParser.IntLiteralContext):
        res = ctx.INT_LITERAL().getText()
        return int(res)

    def visitFloatLiteral(self, ctx: RuleEngineParser.FloatLiteralContext):
        res = ctx.FLOAT_LITERAL().getText()
        return float(res)

    def visitStringLiteral(self, ctx: RuleEngineParser.StringLiteralContext):
        '''
        双引号不应该是占用字符串中的字节
        # "asdfas\rdsfasd"
        # "a\"sdfa\ns\"dsf\fa\r\ns \tdfasd\bf\\a"
        :param ctx:
        :return:
        '''
        # _str = ctx.STRING_LITERAL().getText()[1:-1]
        _str = ctx.STRING_LITERAL().getText().strip('"')

        str = RuleEngineVisitorImpl.handler_str(_str)
        return str

    def visitStringLiteralRefVar(
            self, ctx: RuleEngineParser.StringLiteralRefVarContext):
        left_str = ctx.STRING_LITERAL(0).getText().strip('"')
        left_str = RuleEngineVisitorImpl.handler_str(left_str)

        ref_var_name = ctx.REF_VAR().getText().replace('$', '')
        if ref_var_name in self.vars:
            ref_var_value = self.vars[ref_var_name]
        else:
            token = ctx.REF_VAR().symbol
            raise RuleSyntaxError(
                "Reference Variable " + ref_var_name +
                " is referenced but not initialized. "
                "at line {0}, pos {1}".format(token.line, token.column + 1))

        if len(ctx.STRING_LITERAL()) > 1:
            right_str = ctx.STRING_LITERAL(1).getText().strip('"')
            right_str = RuleEngineVisitorImpl.handler_str(right_str)
            _str = left_str + str(ref_var_value) + right_str
        else:
            _str = left_str + str(ref_var_value)
        return _str

    def visitBooleanLiteral(self, ctx: RuleEngineParser.BooleanLiteralContext):
        return True if ctx.BOOLEAN_LITERAL().getText() in ['True', 'true'
                                                           ] else False

    def visitNullLiteral(self, ctx: RuleEngineParser.NullLiteralContext):
        return None

    def visitEq(self, ctx: RuleEngineParser.EqContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left == right else False

    def visitNe(self, ctx: RuleEngineParser.NeContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return False if left == right else True

    def visitGt(self, ctx: RuleEngineParser.GtContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left > right else False

    def visitLt(self, ctx: RuleEngineParser.LtContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left < right else False

    def visitGe(self, ctx: RuleEngineParser.GeContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left >= right else False

    def visitLe(self, ctx: RuleEngineParser.LeContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return True if left <= right else False

    def visitSum(self, ctx: RuleEngineParser.SumContext):
        '''
        sum(1,2,3)
        sum(1,2,3, "a")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        token = ctx.paralist().start
        for i, num in enumerate(para_list):
            if type(num) not in [int, float]:
                raise RuleParameterError(
                    "[sum] {0}th parameter types error, it is type: {1}. at line {2}, pos {3}"
                    "".format(i + 1, type(num), token.line, token.column + 1))
        return math.fsum(para_list)

    def visitAvg(self, ctx: RuleEngineParser.AvgContext):
        para_list = self.visit(ctx.paralist())
        token = ctx.paralist().start
        for i, num in enumerate(para_list):
            if type(num) not in [int, float]:
                raise RuleParameterError(
                    "[avg] {0}th parameter types error, it is type: {1}. at line {2}, pos {3}"
                    "".format(i + 1, type(num), token.line, token.column + 1))
        return math.fsum(para_list) / len(para_list)

    def visitSqrt(self, ctx: RuleEngineParser.SqrtContext):
        '''
        sqrt(1)
        sqrt(1,2)
        sqrt(0)
        sqrt(-1)
        sqrt("sdf")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len > 1:
            raise RuleParameterError(
                'sqrt function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))

        num = para_list[0]
        if type(num) not in [float, int]:
            raise RuleParameterError(
                "[sqrt] The parameter types error, it is type: {0}. at line {1}, pos {2}"
                "".format(type(num), token.line, token.column + 1))

        if num < 0:
            token = ctx.paralist().start
            raise RuleParameterError(
                "[sqrt] The parameter must be a number greater than or equal to 0. "
                "at line {0}, pos {1}".format(token.line, token.column + 1))

        return math.sqrt(para_list[0])

    def visitLog(self, ctx: RuleEngineParser.LogContext):
        '''
        log(9, 3)
        log(9, -3)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len > 2:
            raise RuleParameterError(
                'log function takes exactly one or two argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))

        num = para_list[0]
        if type(num) not in [int, float]:
            token = ctx.paralist().start
            raise RuleParameterError(
                "[log] The first parameter types error, it is type: {0}. at line {1}, pos {2}"
                "".format(type(num), token.line, token.column + 1))

        if num <= 0:
            token = ctx.paralist().start
            raise RuleParameterError(
                "[log] The first parameter must be a number greater than 0. "
                "at line {0}, pos {1}".format(token.line, token.column + 1))

        if para_len == 1:
            return math.log(num)
        elif para_len == 2:
            if type(para_list[1]) not in [int, float]:
                raise RuleParameterError(
                    "[log] The second parameter types error, it is type: {0}. at line {1}, pos {2}"
                    "".format(type(para_list[1]), token.line,
                              token.column + 1))
            if para_list[1] <= 0:
                raise RuleParameterError(
                    "[log] The second parameter must be a number greater than 0. "
                    "at line {0}, pos {1}".format(token.line,
                                                  token.column + 1))

            return math.log(num, para_list[1])

    def visitLen(self, ctx: RuleEngineParser.LenContext):
        '''
        len("sdfa")
        求字符串长度
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len > 1:
            raise RuleParameterError(
                'len function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            num = para_list[0]
            if not isinstance(num, str):
                raise RuleParameterError(
                    "[len] The parameter types error, it is type: {0}. at line {1}, pos {2}"
                    "".format(type(num), token.line, token.column + 1))
            return len(num)

    def visitCount(self, ctx: RuleEngineParser.CountContext):
        '''
        求参数个数
        count(1,4,7,234,4,1,9)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        return len(para_list)

    def visitMax(self, ctx: RuleEngineParser.MaxContext):
        '''
        max(1,7.6,3.3,90801,0)
        max(111,76.2,3.3,90801,10)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        token = ctx.paralist().start
        for i, num in enumerate(para_list):
            if type(num) not in [int, float]:
                raise RuleParameterError(
                    "[max] {0}th parameter types error, it is type: {1}. at line {2}, pos {3}"
                    "".format(i + 1, type(num), token.line, token.column + 1))
        return max(para_list)

    def visitMin(self, ctx: RuleEngineParser.MinContext):
        '''
        min(1,4,7.3,234,4,1,9)
        min(111,76.2,3.3,90801,10)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        token = ctx.paralist().start
        for i, num in enumerate(para_list):
            if type(num) not in [int, float]:
                raise RuleParameterError(
                    "[min] {0}th parameter types error, it is type: {1}. at line {2}, pos {3}"
                    "".format(i + 1, type(num), token.line, token.column + 1))
        return min(para_list)

    def visitSubstr(self, ctx: RuleEngineParser.SubstrContext):
        '''
        example : substr("abcdefgh")
        example : substr("abcdefgh", 1)
        example : substr("abcdefgh", 1, 3)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)

        token = ctx.paralist().stop
        if para_len > 3:
            raise RuleParameterError(
                'substr function takes exactly one, two or three argument, '
                'but it was given {0}. at line {1}, pos {2}'.format(
                    para_len, token.line, token.column + 1))
        _str = para_list[0]
        if not isinstance(_str, str):
            token = ctx.paralist().start
            raise RuleParameterError(
                "[substr] The first parameter types error, it is type: {0}. at line {1}, "
                "pos {2}".format(type(_str), token.line, token.column + 1))

        if para_len == 1:
            return _str

        start = para_list[1]
        if not isinstance(start, int):
            raise RuleParameterError(
                "[substr] The second parameter types error, it is type: {0}. at line {1}, "
                "pos {2}".format(type(start), token.line, token.column + 1))

        if para_len == 2:
            return _str[start:]
        elif para_len == 3:
            end = para_list[2]
            if not isinstance(end, int):
                raise RuleParameterError(
                    "[substr] The third parameter types error, it is type: {0}. at line {1}, "
                    "pos {2}".format(type(end), token.line, token.column + 1))
            return _str[start:end]

    def visitTrim(self, ctx: RuleEngineParser.TrimContext):
        '''
        trim(" sdfs sdfa ")
        trim(" sdfasd 8712 ",12)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop

        if para_len > 1:
            raise RuleParameterError(
                'trim function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        num = para_list[0]
        if not isinstance(num, str):
            raise RuleParameterError(
                "[trim] The parameter types error, it is type: {0}. at line {1}, pos {2}"
                "".format(type(num), token.line, token.column + 1))
        return para_list[0].strip()

    def visitIs_number(self, ctx: RuleEngineParser.Is_numberContext):
        '''
        is_number("889.1231a")
        is_number(889.1231)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len > 1:
            raise RuleParameterError(
                'is_number function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            try:
                param = para_list[0]
                if not isinstance(param, str):
                    raise RuleParameterError(
                        "[is_number] The parameter types error, it is type: {0}. at line {1}"
                        ", pos {2}".format(type(param), token.line,
                                           token.column + 1))
                float(param)
                return True
            except ValueError:
                return False

    def visitIs_int(self, ctx: RuleEngineParser.Is_intContext):
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop

        if para_len > 1:
            raise RuleParameterError(
                'is_int function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            try:
                param = para_list[0]
                if not isinstance(param, str):
                    raise RuleParameterError(
                        "[is_int] The parameter types error, it is type: {0}. at line {1}"
                        ", pos {2}".format(type(param), token.line,
                                           token.column + 1))
                int(param)
                return True
            except ValueError:
                return False

    def visitIs_null(self, ctx: RuleEngineParser.Is_nullContext):
        '''
        is_null(null)
        is_null("null")
        is_null("")
        is_null(" ")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        if para_len > 1:
            token = ctx.paralist().stop
            raise RuleParameterError(
                'is_null function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            null_list = [None, ""]
            return True if para_list[0] in null_list else False

    def visitTo_str(self, ctx: RuleEngineParser.To_strContext):
        '''
        to_str(sysdate())
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        if para_len > 1:
            token = ctx.paralist().stop
            raise RuleParameterError(
                'to_str function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            if isinstance(para_list[0], datetime):
                return str(para_list[0]).split('.')[0]
            return str(para_list[0])

    def visitTo_int(self, ctx: RuleEngineParser.To_intContext):
        '''
        to_int("89239123")
        to_int("892a39123")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len > 1:
            raise RuleParameterError(
                'to_int function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            try:
                return int(para_list[0])
            except ValueError:
                raise RuleSyntaxError(
                    '[to_int] NumberFormatException: For input string: {0}. '
                    'at line {1}, pos {2}'.format(para_list[0], token.line,
                                                  token.column + 1))

    def visitTo_float(self, ctx: RuleEngineParser.To_floatContext):
        '''
        example: to_float("8989.8989e3")
        example: to_float("8989.8989e3a")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len > 1:
            raise RuleParameterError(
                'to_float function takes exactly one argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        if para_len == 1:
            try:
                return float(para_list[0])
            except ValueError:
                raise RuleSyntaxError(
                    '[to_float] NumberFormatException: For input string: {0}. '
                    'at line {1}, pos {2}'.format(para_list[0], token.line,
                                                  token.column + 1))

    def visitTo_date(self, ctx: RuleEngineParser.To_dateContext):
        '''
        example : to_date("2014-12-31 18:20:10")
        example : to_date("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
        example : to_date("2017-09-12", "%Y-%m-%d %H:%M:%S")
        example : to_date("2017/09/12", "%Y/%m/%d")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        if para_len > 2:
            token = ctx.paralist().stop
            raise RuleParameterError(
                'to_date function takes exactly one or two argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        try:
            date_str = para_list[0]
            if para_len == 1:
                if date_str.find(":") != -1:
                    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                else:
                    return datetime.strptime(date_str, "%Y-%m-%d")
            if para_len == 2:
                date_format = para_list[1]
                for key, value in date_fmt_dict.items():
                    date_format = date_format.replace(key, value)
                return datetime.strptime(date_str, date_format)
        except ValueError:
            token = ctx.paralist().start
            raise RuleParameterError(
                '[to_date] format error. at line {0}, pos {1}'.format(
                    token.line, token.column + 1))

    def visitAdd_to_date(self, ctx: RuleEngineParser.Add_to_dateContext):
        '''
        example 2: add_to_date(to_date("2017-09-01"), "year", 1)
        example 2: add_to_date(to_date("2017-09-01"), "month", 15)
        example 2: add_to_date(to_date("2017-09-01"), "week", 1)
        example 2: add_to_date(to_date("2017-09-01  "), "day", 1)
        example 2: add_to_date(to_date("2017-09-01"), "day", 1)
        example 2: add_to_date(to_date("2017-09-01"), "second", 1)
        example 2: add_to_date(to_date("2017-09-01"), "minute", 2)
        example 2: add_to_date(to_date("2017-09-01"), "hour", 3)
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len != 3:
            raise RuleParameterError(
                'add_to_date function takes exactly three argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        _date = para_list[0]
        _type = para_list[1]
        _value = para_list[2]

        if not isinstance(_date, datetime):
            token = ctx.paralist().start
            raise RuleParameterError(
                "[add_to_date] The first parameter types error, it is type: {0}. at line {1},"
                " pos {2}".format(type(_date), token.line, token.column + 1))
        if not isinstance(_type, str):
            raise RuleParameterError(
                "[add_to_date] The second parameter types error, it is type: {0}. at line {1}"
                ", pos {2}".format(type(_type), token.line, token.column + 1))
        if not isinstance(_value, int):
            raise RuleParameterError(
                "[add_to_date] The third parameter types error, it is type: {0}. at line {1}"
                ", pos {2}".format(type(_value), token.line, token.column + 1))

        if _type not in [
                "year", "month", "week", "day", "hour", "minute", "second"
        ]:
            raise RuleParameterError(
                "[add_to_date] The value of the second parameter is illegal. at line {0}, "
                "pos {1}".format(token.line, token.column + 1))

        if _type == 'year':
            return _date + relativedelta(years=_value)
        elif _type == 'month':
            return _date + relativedelta(months=_value)
        if _type == 'week':
            return _date + timedelta(weeks=_value)
        elif _type == 'day':
            return _date + timedelta(days=_value)
        elif _type == 'hour':
            return _date + timedelta(hours=_value)
        elif _type == 'minute':
            return _date + timedelta(minutes=_value)
        elif _type == 'second':
            return _date + timedelta(seconds=_value)

    def visitDate_diff(self, ctx: RuleEngineParser.Date_diffContext):
        '''
        example: date_diff(to_date("2017-10-1"), sysdate(), "hour")
        example: date_diff(to_date("2017-10-1"), to_date("2007-10-1"), "year")
        example: date_diff(to_date("2017-10-1"), to_date("2007-10-1"), "month")

                 date_diff(to_date("2017-10-10"), to_date("2007-12-09"), "year")
                 date_diff(to_date("2018-01-10"), to_date("2017-10-09"), "month")
                 date_diff(to_date("2018-10-10"), to_date("2017-10-09"), "month")
                 date_diff(to_date("2018-01-10"), to_date("2017-10-09"), "day")
                 date_diff(to_date("2017-10-17"), sysdate(), "hour")
                 date_diff(to_date("2017-10-17"), sysdate(), "minute")
                 date_diff(to_date("2017-10-17"), sysdate(), "second")
        :param ctx:
        :return:
        '''
        para_list = self.visit(ctx.paralist())
        para_len = len(para_list)
        token = ctx.paralist().stop
        if para_len != 3:
            raise RuleParameterError(
                'date_diff function takes exactly three argument, but it was given {0}. '
                'at line {1}, pos {2}'.format(para_len, token.line,
                                              token.column + 1))
        first_datetime = para_list[0]
        second_datetime = para_list[1]
        res_type = para_list[2]

        if not isinstance(first_datetime, datetime):
            token = ctx.paralist().start
            raise RuleParameterError(
                "[date_diff] The first parameter types error, it is type: {0}. at line {1}, "
                "pos {2}".format(type(first_datetime), token.line,
                                 token.column + 1))
        if not isinstance(second_datetime, datetime):
            token = ctx.paralist().start
            raise RuleParameterError(
                "[date_diff] The second parameter types error, it is type: {0}. at line {1}, "
                "pos {2}".format(type(second_datetime), token.line,
                                 token.column + 1))
        if not isinstance(res_type, str):
            raise RuleParameterError(
                "[date_diff] The third parameter types error, it is type: {0}. at line {1}, "
                "pos {2}".format(type(res_type), token.line, token.column + 1))

        if res_type not in [
                "year", "month", "day", "hour", "minute", "second"
        ]:
            raise RuleParameterError(
                "[date_diff] The value of the third parameter is illegal. at line {0}, "
                "pos {1}".format(token.line, token.column + 1))

        diff_datetime = first_datetime - second_datetime

        if res_type == 'year':
            return first_datetime.year - second_datetime.year
        elif res_type == 'month':
            return (first_datetime.year - second_datetime.year
                    ) * 12 + first_datetime.month - second_datetime.month
        elif res_type == 'day':
            return int(diff_datetime.total_seconds() / (60 * 60 * 24))
        elif res_type == 'hour':
            return int(diff_datetime.total_seconds() / (60 * 60))
        elif res_type == 'minute':
            return int(diff_datetime.total_seconds() / 60)
        elif res_type == 'second':
            return int(diff_datetime.total_seconds())

    def visitSysdate(self, ctx: RuleEngineParser.SysdateContext):
        '''
        sysdate()
        :param ctx:
        :return:
        '''
        return datetime.now()

    def visitErrorNode(self, node):
        token = node.symbol
        raise RuleSyntaxError(
            "[ErrorNode] token recognition error at: {0}. at line {1}, pos {2}"
            .format(token.text, token.line, token.column + 1))

    @staticmethod
    def handler_str(str):
        '''
        字符串处理
        :param str:
        :return:
        '''
        for key, value in blank_str_dict.items():
            str = str.replace(key, value)
        for key, value in real_str_dict.items():
            str = str.replace(key, value)
        return str

    def visitExprAction(self, ctx: RuleEngineParser.ExprActionContext):
        return super().visitExprAction(ctx)

    def visitAssignChinese(self, ctx: RuleEngineParser.AssignChineseContext):
        name = ctx.CHINESE_VAR().getText()
        value = self.visit(ctx.expression())
        self.vars.update({name: value})
        return value

    def visitAction_exp(self, ctx: RuleEngineParser.Action_expContext):
        return super().visitAction_exp(ctx)

    def visitChineseVar(self, ctx: RuleEngineParser.ChineseVarContext):
        name = ctx.CHINESE_VAR().getText()
        if name in self.vars:
            return self.vars[name]

        token = ctx.LOCAL_VAR().symbol
        raise RuleSyntaxError(
            "chinese Variable " + name + " is referenced but not initialized. "
            "at line {0}, pos {1}".format(token.line, token.column + 1))
