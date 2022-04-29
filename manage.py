from ruleEngine.RuleEngineWrapper import HyperParser

hr_parser = HyperParser()

'''

温度 = 20;
温度 <= 20;
if (温度 <= 20) {a=5;} else {a = 3;} ;

a = 20;
a <= 20;
if (a <= 20) {a=5;} else {a = 3;} ;



'''
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    try:
        x = hr_parser.parse(s)
        print("{0}".format(x))
    except Exception as e:
        print(e)

