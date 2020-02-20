#!/usr/bin/env python


class Solution:
    def evaluate(self, expression: str) -> int:
        def get_num(exps, i, var_val):
            if exps[i] == '(':
                num, i = parse(exps, i+1, var_val)
            else:
                try:
                    num, i = int(exps[i]), i+1
                except:
                    num, i = var_val[exps[i]], i+1
            return num, i

        def parse(exps, i, var_val):
            var_val = var_val.copy()
            op, i = exps[i], i+1
            if op == 'let':
                while True:
                    try:
                        var = exps[i]
                        val, i = get_num(exps, i+1, var_val)
                        var_val[var] = val
                    except:
                        expr, i = get_num(exps, i, var_val)
                        return expr, i+1
            else:
                num1, i = get_num(exps, i, var_val)
                num2, i = get_num(exps, i, var_val)
                val = num1 + num2 if op == 'add' else num1 * num2
                return val, i+1

        expression = expression.replace(')', ' )').replace('(', '( ')
        return parse(expression.split(), 1, {})[0]
