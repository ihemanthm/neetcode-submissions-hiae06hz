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
            op1_int_pos, op2_int_pos = max(op1_int, -1*op1_int), max(op2_int, op2_int*-1)
            op_res = op1_int_pos // op2_int_pos
            if op1_int < 0:
                op_res *=-1
            if op2_int < 0:
                op_res *=-1
            return op_res

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