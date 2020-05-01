import numpy as np


class LinearProgramProblem:
    def __init__(self, c, extr, A, signs, b, var_sings):
        self.c = c
        self.extr = extr
        self.A = A
        self.signs = signs
        self.b = b
        self.var_signs = var_sings
        self.lim_cnt, self.var_cnt = self.A.shape
        self.conf_X = list([i] for i in range(self.var_cnt))

    def convert_canon_type(self):
        self.convert_extr()
        self.convert_limit_sign()
        self.convert_var_sign()
        self.convert_b_sign()
        return self.A, self.b, self.c

    def convert_extr(self):
        if self.extr == 'max':
            self.c = (-1) * self.c
            self.extr = 'min'

    def convert_limit_sign(self):
        for ind, sign in enumerate(self.signs):
            if sign == '<=' or sign == '>=':
                self.var_signs.append('positive')
                self.var_cnt += 1
                self.c = np.append(self.c, 0)
                self.A = np.append(
                    self.A, np.zeros((self.lim_cnt, 1), float), axis=1)
                if sign == '<=':
                    self.A[ind][self.var_cnt - 1] = 1
                if sign == '>=':
                    self.A[ind][self.var_cnt - 1] = -1
                self.signs[ind] = '='

    def convert_var_sign(self):
        for ind, var in enumerate(self.var_signs):
            if var == 'any':
                self.var_signs[ind] = 'positive'
                self.var_signs.append('positive')
                self.conf_X[ind].append(self.var_cnt)
                self.var_cnt += 1
                self.c = np.append(self.c, self.c[ind] * (-1))
                self.A = np.append(
                    self.A, np.array(
                        [[(-1) * self.A[j, ind]] for j in range(
                            self.lim_cnt)], float), axis=1)

    def convert_b_sign(self):
        for ind, var in enumerate(self.b):
            if var < 0:
                self.b[ind] *= (-1)
                self.A[ind] = (-1) * self.A[ind]

    def sort_conditions(self):
        for ind, sign in enumerate(self.signs):
            if (sign == '<=' and self.extr == 'min') or \
                    (sign == '>=' and self.extr == 'max'):
                self.A[ind] *= (-1)
                self.b[ind] *= (-1)
                if sign == '<=':
                    self.signs[ind] = '>='
                elif sign == '>=':
                    self.signs[ind] = '<='

    def find_init_X(self, X):
        init_X = np.zeros(len(self.conf_X))
        for ind, nums in enumerate(self.conf_X):
            if len(nums) == 1:
                init_X[ind] = X[nums[0]]
            elif len(nums) == 2:
                init_X[ind] = X[nums[0]] - X[nums[1]]
        return init_X
