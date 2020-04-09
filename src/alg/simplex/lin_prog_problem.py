import numpy as np
import copy as cp
import math as mt


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

    def print_task(self):
        print(' + '.join(str(value) + 'x' + str(id) for id, value in
                         enumerate(self.c)), '->', self.extr)
        for id in range(self.lim_cnt):
            print(' + '.join(str(value) + 'x' + str(j) for j, value in
                             enumerate(self.A[id])), self.signs[id],
                  self.b[id])
        for id, sign in enumerate(self.var_signs):
            if sign == 'positive':
                print('x' + str(id), '>= 0')

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
        for id, sign in enumerate(self.signs):
            if sign == '<=' or sign == '>=':
                self.var_signs.append('positive')
                self.var_cnt += 1
                self.c = np.append(self.c, 0)
                self.A = np.append(
                    self.A, np.zeros((self.lim_cnt, 1), float), axis=1)
                if sign == '<=':
                    self.A[id][self.var_cnt - 1] = 1
                if sign == '>=':
                    self.A[id][self.var_cnt - 1] = -1
                self.signs[id] = '='

    def convert_var_sign(self):
        for id, var in enumerate(self.var_signs):
            if var == 'any':
                self.var_signs[id] = 'positive'
                self.var_signs.append('positive')
                self.conf_X[id].append(self.var_cnt)
                self.var_cnt += 1
                self.c = np.append(self.c, self.c[id] * (-1))
                self.A = np.append(
                    self.A, np.array(
                        [[(-1) * self.A[j, id]] for j in range(
                            self.lim_cnt)], float), axis=1)

    def convert_b_sign(self):
        for id, var in enumerate(self.b):
            if var < 0:
                self.b[id] *= (-1)
                self.A[id] = (-1) * self.A[id]

    def create_dual_lp(self):
        self.sort_conditions()
        A_dual = self.A.transpose()
        b_dual = self.c
        c_dual = self.b
        if self.extr == 'max':
            extr_dual = 'min'
        else:
            extr_dual = 'max'
        lim_cnt_dual, var_cnt_dual = A_dual.shape
        var_signs_dual = list('any' for _ in range(var_cnt_dual))
        signs_dual = list('=' for _ in range(lim_cnt_dual))

        for id, sign in enumerate(self.signs):
            if (sign == '>=' and self.extr == 'min') or \
                    (sign == '<=' and self.extr == 'max'):
                var_signs_dual[id] = 'positive'

        for id, sign in enumerate(self.var_signs):
            if sign == 'positive':
                if extr_dual == 'min':
                    signs_dual[id] = '>='
                else:
                    signs_dual[id] = '<='
        return LinearProgramProblem(c_dual, extr_dual,
                                    A_dual, signs_dual, b_dual, var_signs_dual)

    def sort_conditions(self):
        for id, sign in enumerate(self.signs):
            if (sign == '<=' and self.extr == 'min') or \
                    (sign == '>=' and self.extr == 'max'):
                self.A[id] *= (-1)
                self.b[id] *= (-1)
                if sign == '<=':
                    self.signs[id] = '>='
                elif sign == '>=':
                    self.signs[id] = '<='

    def find_init_X(self, X):
        init_X = np.zeros(len(self.conf_X))

        for id, nums in enumerate(self.conf_X):
            if len(nums) == 1:
                init_X[id] = X[nums[0]]
            elif len(nums) == 2:
                init_X[id] = X[nums[0]] - X[nums[1]]
        return init_X

    def find_dual_result(self, result_X):
        rows, columns = self.A.shape
        result_Y = np.zeros(rows)
        null_y = list()
        not_null_y = list()
        not_equal_lim = list()

        for i in range(rows):
            value = 0
            for j in range(columns):
                value += result_X[j] * self.A[i][j]
            if mt.fabs(value - self.b[i]) > 1e-14:
                null_y.append(i)
            else:
                not_null_y.append(i)

        for i in range(columns):
            if result_X[i] == 0:
                not_equal_lim.append(i)
        A = cp.deepcopy(self.A.transpose())
        c = cp.deepcopy(self.c)
        null_y.reverse()
        not_equal_lim.reverse()

        for id in null_y:
            A = np.delete(A, id, axis=1)
        for id in not_equal_lim:
            A = np.delete(A, id, axis=0)
            c = np.delete(c, id)
        sub_Y = np.linalg.solve(A, c)

        for id, i in enumerate(not_null_y):
            result_Y[i] = sub_Y[id]
        return result_Y
