class Solution:
    def operation(self, op1, op2, opd):
        op1_int, op2_int = int(op1), int(op2)
        if opd=="+":
            return op1_int+op2_int
        elif opd=="-":
            return op1_int-op2_int
        elif opd=="*":
            return op1_int*op2_int
        else:
            return int(float(op1_int)) / int(float(op2_int))

    def evalRPN(self, tokens: List[str]) -> int:
        operands = list()
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                op2 = operands.pop()
                op1 = operands.pop()
                op_result = self.operation(op1, op2, token)
                operands.append(op_result)
            else:
                operands.append(token)
        return int(operands[-1])