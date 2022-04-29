# Generated from RuleEngine.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RuleEngineParser import RuleEngineParser
else:
    from RuleEngineParser import RuleEngineParser

# This class defines a complete generic visitor for a parse tree produced by RuleEngineParser.

class RuleEngineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RuleEngineParser#statements.
    def visitStatements(self, ctx:RuleEngineParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#statements_block.
    def visitStatements_block(self, ctx:RuleEngineParser.Statements_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#exprStmt.
    def visitExprStmt(self, ctx:RuleEngineParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#exprAction.
    def visitExprAction(self, ctx:RuleEngineParser.ExprActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#assignStmt.
    def visitAssignStmt(self, ctx:RuleEngineParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#ifStmt.
    def visitIfStmt(self, ctx:RuleEngineParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#assignLocal.
    def visitAssignLocal(self, ctx:RuleEngineParser.AssignLocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#assignRef.
    def visitAssignRef(self, ctx:RuleEngineParser.AssignRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#assignChinese.
    def visitAssignChinese(self, ctx:RuleEngineParser.AssignChineseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#if_statement.
    def visitIf_statement(self, ctx:RuleEngineParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#condition.
    def visitCondition(self, ctx:RuleEngineParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#branchStmt.
    def visitBranchStmt(self, ctx:RuleEngineParser.BranchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#branchBlock.
    def visitBranchBlock(self, ctx:RuleEngineParser.BranchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#action_exp.
    def visitAction_exp(self, ctx:RuleEngineParser.Action_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Add.
    def visitAdd(self, ctx:RuleEngineParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Date_diff.
    def visitDate_diff(self, ctx:RuleEngineParser.Date_diffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Or.
    def visitOr(self, ctx:RuleEngineParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Max.
    def visitMax(self, ctx:RuleEngineParser.MaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Uminus.
    def visitUminus(self, ctx:RuleEngineParser.UminusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#BooleanLiteral.
    def visitBooleanLiteral(self, ctx:RuleEngineParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Add_to_date.
    def visitAdd_to_date(self, ctx:RuleEngineParser.Add_to_dateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Count.
    def visitCount(self, ctx:RuleEngineParser.CountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Eq.
    def visitEq(self, ctx:RuleEngineParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#To_date.
    def visitTo_date(self, ctx:RuleEngineParser.To_dateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Gt.
    def visitGt(self, ctx:RuleEngineParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Is_null.
    def visitIs_null(self, ctx:RuleEngineParser.Is_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Substr.
    def visitSubstr(self, ctx:RuleEngineParser.SubstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Ne.
    def visitNe(self, ctx:RuleEngineParser.NeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#RefVar.
    def visitRefVar(self, ctx:RuleEngineParser.RefVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Le.
    def visitLe(self, ctx:RuleEngineParser.LeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#IntLiteral.
    def visitIntLiteral(self, ctx:RuleEngineParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#To_float.
    def visitTo_float(self, ctx:RuleEngineParser.To_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Sub.
    def visitSub(self, ctx:RuleEngineParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Mod.
    def visitMod(self, ctx:RuleEngineParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Log.
    def visitLog(self, ctx:RuleEngineParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Trim.
    def visitTrim(self, ctx:RuleEngineParser.TrimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Mul.
    def visitMul(self, ctx:RuleEngineParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:RuleEngineParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Sqrt.
    def visitSqrt(self, ctx:RuleEngineParser.SqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Lt.
    def visitLt(self, ctx:RuleEngineParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Is_int.
    def visitIs_int(self, ctx:RuleEngineParser.Is_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Sum.
    def visitSum(self, ctx:RuleEngineParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#To_int.
    def visitTo_int(self, ctx:RuleEngineParser.To_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Is_number.
    def visitIs_number(self, ctx:RuleEngineParser.Is_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#To_str.
    def visitTo_str(self, ctx:RuleEngineParser.To_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Div.
    def visitDiv(self, ctx:RuleEngineParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#ChineseVar.
    def visitChineseVar(self, ctx:RuleEngineParser.ChineseVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Not.
    def visitNot(self, ctx:RuleEngineParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Avg.
    def visitAvg(self, ctx:RuleEngineParser.AvgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Min.
    def visitMin(self, ctx:RuleEngineParser.MinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#StringLiteral.
    def visitStringLiteral(self, ctx:RuleEngineParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Len.
    def visitLen(self, ctx:RuleEngineParser.LenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#And.
    def visitAnd(self, ctx:RuleEngineParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#StringLiteralRefVar.
    def visitStringLiteralRefVar(self, ctx:RuleEngineParser.StringLiteralRefVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Sysdate.
    def visitSysdate(self, ctx:RuleEngineParser.SysdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Pow.
    def visitPow(self, ctx:RuleEngineParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#LocalVar.
    def visitLocalVar(self, ctx:RuleEngineParser.LocalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Floor_Div.
    def visitFloor_Div(self, ctx:RuleEngineParser.Floor_DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#NullLiteral.
    def visitNullLiteral(self, ctx:RuleEngineParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Ge.
    def visitGe(self, ctx:RuleEngineParser.GeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#Paren.
    def visitParen(self, ctx:RuleEngineParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#paralist.
    def visitParalist(self, ctx:RuleEngineParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RuleEngineParser#para.
    def visitPara(self, ctx:RuleEngineParser.ParaContext):
        return self.visitChildren(ctx)



del RuleEngineParser