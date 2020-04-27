import numpy as np
import itertools as it
import copy as cp
from src.alg.exceptions import SimplexAlgorithmException, \
    NotSolveSimplex


def del_null(A, c):
    null_id = list()
    for index, column in enumerate(A):
        if all_null(column):
            null_id.append(index)
    null_id.reverse()
    for index in null_id:
        A = np.delete(A, index, axis=0)
        c = np.delete(c, index)
    return A, c


def all_null(column):
    for elem in column:
        if elem != 0:
            return False
    return True


def plusList(ref_vector):
    N_plus_index = []
    for index, x in enumerate(ref_vector):
        if x > 0:
            N_plus_index.append(index)
    return N_plus_index


def artificial_basis(A, b, c):
    rows, columns = A.shape
    rank = np.linalg.matrix_rank(A)
    if rank != rows:
        raise NotSolveSimplex
    E = np.eye(rows)
    sub_A = np.append(A, E, axis=1)
    arr_zero = np.zeros(columns, float)
    sub_c = np.append(arr_zero, np.ones(rows))
    ref_vector = np.append(arr_zero, b)
    return sub_A, sub_c, ref_vector


def pos_vector(vector):
    for x in vector:
        if x < 0:
            return False
    return True


def find_new_basis(N_k, index, L, A):
    sub_A = list()
    for i in index:
        for j in N_k:
            if j != i:
                sub_A.append(A.transpose()[j])
        for id in L:
            new_A_N = cp.deepcopy(sub_A)
            new_A_N.append(A.transpose()[id])
            new_A_N = np.array(new_A_N)
            if np.linalg.det(new_A_N) != 0:
                N_k[N_k.index(i)] = id
                return N_k
        N_k.append(i)


def find_A_N(A, A_N, N_k, N_null_index):
    new_M, new_N = A_N.shape
    delta = new_M - new_N
    if delta == 0:
        return N_k
    column_A_combinations = list(it.combinations(N_null_index, delta))
    for column_A in column_A_combinations:
        sub_A = list()
        for column in A_N.transpose():
            sub_A.append(column)
        for index in column_A:
            sub_A.append(A.transpose()[index])
        sub_A = np.array(sub_A).transpose()
        if np.linalg.det(sub_A) != 0:
            for index in column_A:
                N_k.append(index)
            return N_k


def find_new_B(B, N_k, i_k, sub_u):  # вычисление обратной
    F = np.eye(len(N_k))
    for id in range(len(N_k)):
        if F[id][N_k.index(i_k)] != 1:
            F[id][N_k.index(i_k)] = -sub_u[id] / sub_u[N_k.index(i_k)]
        else:
            F[id][N_k.index(i_k)] = 1 / sub_u[N_k.index(i_k)]
    new_B = np.dot(F, B)
    return new_B


def update_d_L(d_L):
    for index, d in enumerate(d_L):
        if abs(d) <= 1e-14:
            d_L[index] = 0


def simplex_dates_L_dimension(N_k, A, c, B):
    M, N = A.shape
    c_N = list()
    L = list()
    A_L = list()
    c_L = list()
    for index in N_k:
        c_N.append(c[index])
    c_N = np.array(c_N)
    for index in range(N):
        if index not in N_k:
            L.append(index)
            A_L.append(A.transpose()[index])
            c_L.append(c[index])
    A_L = np.array(A_L).transpose()
    c_L = np.array(c_L)
    Y = np.dot(c_N.transpose(), B)
    return c_L - np.dot(Y, A_L), L


def calc_j_k(d_L, L):
    for index, d in enumerate(d_L):
        if d < 0:
            return L[index]
    return 0


def calc_list_i_k(N_k, sub_u, u):
    i_k_list = list()
    for index, n_k in enumerate(N_k):
        u[n_k] = sub_u[index]
        if u[n_k] > 0:
            i_k_list.append(n_k)
    return i_k_list


def calc_coefficients(i_k_list, ref_vector, u):
    i_k = i_k_list[0]
    coefficient = ref_vector[i_k] / u[i_k]
    for i in i_k_list:
        if (ref_vector[i] / u[i]) < coefficient:
            i_k = i
            coefficient = ref_vector[i_k] / u[i_k]
    return coefficient, i_k


def calc_indices_not_plus_element(N_k, N_plus_index):
    indices_not_plus_element = list()
    for index in N_k:
        if index not in N_plus_index:
            indices_not_plus_element.append(index)
    return indices_not_plus_element


def main_algorithm(N_k, A, c, ref_vector, B):
    M, N = A.shape
    d_L, L = simplex_dates_L_dimension(N_k, A, c, B)
    update_d_L(d_L)
    if pos_vector(d_L):
        return True, ref_vector, B, N_k
    j_k = calc_j_k(d_L, L)
    A_j = A.transpose()[j_k]
    u = np.zeros(N)
    sub_u = np.dot(B, A_j.transpose())
    i_k_list = calc_list_i_k(N_k, sub_u, u)
    u[j_k] = -1
    if len(i_k_list) == 0:
        return False, np.zeros(N), B, N_k
    coefficient, i_k = calc_coefficients(i_k_list, ref_vector, u)
    N_plus_index = plusList(ref_vector)
    B = find_new_B(B, N_k, i_k, sub_u)
    if len(N_plus_index) != len(N_k):
        indices_not_plus_element = calc_indices_not_plus_element(N_k, N_plus_index)
        for index in indices_not_plus_element:
            if u[index] > 0:
                N_k = find_new_basis(N_k, indices_not_plus_element, L, A)
                return False, ref_vector, B, N_k
    new_ref_vector = ref_vector - coefficient * u
    N_k[N_k.index(i_k)] = j_k
    return False, new_ref_vector, B, N_k


def first_step(A, ref_vector):
    M, N = A.shape
    N_k = list()
    N_null_index = list()
    N_plus_index = list()
    A_N = list()
    for id, x in enumerate(ref_vector):
        if x > 0:
            N_plus_index.append(id)
            N_k.append(id)
            A_N.append(A.transpose()[id])
        elif x == 0:
            N_null_index.append(id)
    A_N = np.array(A_N)
    A_N = A_N.transpose()
    B = np.eye(M)
    N_k = find_A_N(A, A_N, N_k, N_null_index)
    return N_k, B


def N_K_dates_L_dimensions(N, N_k):
    L = list()
    for index in range(N):
        if index not in N_k:
            L.append(index)
    return L


def transform_ref_vector(ref_vector, B, N_k, A):
    M, N = A.shape
    ref_vector = ref_vector[:N]
    A_N = list()
    N_k_old = list(N_k)
    N_k.sort()
    new_B = list()
    for id in N_k:
        A_N.append(A.transpose()[id])
        new_B.append(B[N_k_old.index(id), :])
    B = np.array(new_B)
    L = N_K_dates_L_dimensions(N, N_k)
    A_N = np.array(A_N).transpose()
    E = np.eye(M)
    for i in range(M):
        for j in range(M):
            if np.array_equal(A_N[:, i], E[:, j]):
                for id in L:
                    A_N[:, i] = A[:, id]
                    if np.linalg.det(A_N) != 0:
                        i_k = N_k[i]
                        j_k = id
                        A_j = A.transpose()[j_k]
                        sub_u = np.dot(B, A_j.transpose())
                        B = find_new_B(B, N_k, i_k, sub_u)
                        N_k[i] = j_k
                        L.remove(id)
                        break
    return ref_vector, B


def start_simplex_method(A, b, c):
    plot_points = list()
    try:
        sub_A, sub_c, ref_vector = artificial_basis(A, b, c)
    except NotSolveSimplex:
        raise NotSolveSimplex()
    N_k, B = first_step(sub_A, ref_vector)
    ref_vector, B, N_k = start_alg_iterations(N_k, ref_vector, B, sub_A, sub_c, plot_points)
    ref_vector, B = transform_ref_vector(ref_vector, B, N_k, A)
    ref_vector, B, N_k = start_alg_iterations(N_k, ref_vector, B, A, c, plot_points)
    return ref_vector, plot_points


def start_alg_iterations(N_k, ref_vector, B, A, c, plot_points):
    end = False
    while not end:
        end, ref_vector, B, N_k = main_algorithm(N_k, A,
                                                 c, ref_vector, B)
        if all_null(ref_vector):
            raise SimplexAlgorithmException()
        plot_points.append(ref_vector)
    return ref_vector, B, N_k
