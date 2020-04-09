import numpy as np
import itertools as it
import copy as cp
from src.alg.exceptions import SimplexAlgorithmException, \
    NotSolveSimplex


def del_null(A, c):
    null_id = list()
    for id, column in enumerate(A):
        if all_null(column):
            null_id.append(id)
    null_id.reverse()
    for id in null_id:
        A = np.delete(A, id, axis=0)
        c = np.delete(c, id)
    return A, c


def all_null(column):
    for elem in column:
        if elem != 0:
            return False
    return True


def plusList(ref_vector):
    N_plus_index = []
    for id, x in enumerate(ref_vector):
        if x > 0:
            N_plus_index.append(id)
    return N_plus_index


def artificial_basis(A, b, c):
    rows, columns = A.shape
    rank = np.linalg.matrix_rank(A)
    if rank != rows:
        print("error")
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
        return A_N, N_k
    id_A = list(it.combinations(N_null_index, delta))
    for id in id_A:
        sub_A = list()
        for column in A_N.transpose():
            sub_A.append(column)
        for i in id:
            sub_A.append(A.transpose()[i])
        sub_A = np.array(sub_A).transpose()
        if np.linalg.det(sub_A) != 0:
            for i in id:
                N_k.append(i)
            A_N = cp.deepcopy(sub_A)
            return A_N, N_k


# вычисление обратной
def find_new_B(B, N_k, i_k, sub_u):
    F = np.eye(len(N_k))
    for id in range(len(N_k)):
        if F[id][N_k.index(i_k)] != 1:
            F[id][N_k.index(i_k)] = -sub_u[id] / sub_u[N_k.index(i_k)]
        else:
            F[id][N_k.index(i_k)] = 1 / sub_u[N_k.index(i_k)]
    new_B = np.dot(F, B)
    return new_B


def main_algorithm(N_k, A, c, ref_vector, B):
    M, N = A.shape
    A_N = list()
    c_N = list()
    L = list()
    A_L = list()
    c_L = list()

    for id in N_k:
        A_N.append(A.transpose()[id])
        c_N.append(c[id])
    c_N = np.array(c_N)
    A_N = np.array(A_N)
    A_N = A_N.transpose()

    for id in range(N):
        if id not in N_k:
            L.append(id)
            A_L.append(A.transpose()[id])
            c_L.append(c[id])

    A_L = np.array(A_L)
    A_L = A_L.transpose()
    c_L = np.array(c_L)

    Y = np.dot(c_N.transpose(), B)
    d_L = c_L - np.dot(Y, A_L)
    j_k = 0

    for id, d in enumerate(d_L):
        if abs(d) <= 1e-14:
            d_L[id] = 0
    if pos_vector(d_L):
        return True, ref_vector, N_k, B

    for id, d in enumerate(d_L):
        if d < 0:
            j_k = L[id]
            break
    A_j = A.transpose()[j_k]
    u = np.zeros(N)
    sub_u = np.dot(B, A_j.transpose())
    i_k_list = list()

    for id, n_k in enumerate(N_k):
        u[n_k] = sub_u[id]
        if u[n_k] > 0:
            i_k_list.append(n_k)

    u[j_k] = -1

    if len(i_k_list) == 0:
        return False, np.zeros(N), N_k, B

    i_k = i_k_list[0]
    coeff = ref_vector[i_k] / u[i_k]

    for i in i_k_list:
        if (ref_vector[i] / u[i]) < coeff:
            i_k = i
            coeff = ref_vector[i_k] / u[i_k]

    N_plus_index = plusList(ref_vector)
    B = find_new_B(B, N_k, i_k, sub_u)

    if len(N_plus_index) != len(N_k):
        index = list()
        for id in N_k:
            if id not in N_plus_index:
                index.append(id)
        for id in index:
            if u[id] > 0:
                N_k = find_new_basis(N_k, index, L, A)
                return False, ref_vector, N_k, B

    new_ref_vector = ref_vector - coeff * u
    N_k[N_k.index(i_k)] = j_k
    return False, new_ref_vector, N_k, B


def first_step(A, c, ref_vector):
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
    A_N, N_k = find_A_N(A, A_N, N_k, N_null_index)
    return N_k, ref_vector, B


def transform_ref_vector(ref_vector, B, N_k, A):
    M, N = A.shape
    ref_vector = ref_vector[:N]
    L = list()
    A_N = list()
    N_k_old = list(N_k)
    N_k.sort()
    new_B = list()
    for id in N_k:
        A_N.append(A.transpose()[id])
        new_B.append(B[N_k_old.index(id), :])
    new_B = np.array(new_B)
    B = new_B

    for id in range(N):
        if id not in N_k:
            L.append(id)

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
    return ref_vector, B, N_k


def start_simplex_method(A, b, c):
    plot_points = list()
    try:
        sub_A, sub_c, ref_vector = artificial_basis(A, b, c)
    except NotSolveSimplex:
        raise NotSolveSimplex()

    N_k, ref_vector, B = first_step(sub_A, sub_c, ref_vector)
    end = False

    while not end:
        end, ref_vector, N_k, B = main_algorithm(N_k, sub_A,
                                                 sub_c, ref_vector, B)
        if all_null(ref_vector):
            print('Error')
            raise SimplexAlgorithmException()
        plot_points.append(ref_vector)

    ref_vector, B, N_k = transform_ref_vector(ref_vector, B, N_k, A)
    end = False

    while not end:
        end, ref_vector, N_k, B = main_algorithm(N_k, A,
                                                 c, ref_vector, B)
        if all_null(ref_vector):
            print('Error')
            raise SimplexAlgorithmException()
        plot_points.append(ref_vector)

    return ref_vector, plot_points
