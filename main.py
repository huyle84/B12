import sys

from bra12 import Context, Bra12
from utils.core import tests as tests_utils_core
from utils.regev import tests as tests_utils_regev
from utils.bra import tests as tests_utils_bra
from math import log2


def main():
    n = 3
    q = 2 ** 16
    L = 1
    ctx = Context(n, q, L)
    bra = Bra12(ctx)

    print("Params: n (modulus)={}, N = {}, q (decomposition)={}".format(ctx.n, (ctx.n + 1) * int((log2(ctx.q) + 1)),
                                                                        ctx.q))
    print("Secrete key sk = {}, shape = {}".format(bra.sk, bra.sk.shape))
    print("Evaluation keys evks = {}, shape = {}".format(bra.evks, len(bra.evks)))
    print("Public key pk = {}, shape = {}".format(bra.pk, bra.pk.shape))

    # Addition 1
    m_1 = 0
    m_2 = 0
    c_1 = bra.encrypt(m_1)
    c_2 = bra.encrypt(m_2)
    res = bra.decrypt(c_1 + c_2)
    print(f'{m_1} + {m_2} = {res}')
    assert res == (m_1 + m_2) % 2
    print("message 1,m_1 =", m_1)
    print("message 2,m_2 =", m_2)
    print("ciphertext c_1 =", c_1)
    print("ciphertext c_2 =", c_2)
    print("{} + {} = {}".format(m_1, m_2, res))

    # Addition 2
    m_1 = 0
    m_2 = 1
    c_1 = bra.encrypt(m_1)
    c_2 = bra.encrypt(m_2)
    res = bra.decrypt(c_1 + c_2)
    print(f'{m_1} + {m_2} = {res}')
    assert res == (m_1 + m_2) % 2
    print("message 1,m_1 =", m_1)
    print("message 2,m_2 =", m_2)
    print("ciphertext c_1 =", c_1)
    print("ciphertext c_2 =", c_2)
    print("{} + {} = {}".format(m_1, m_2, res))

    # Multiplication 1
    m_1 = 1
    m_2 = 1
    c_1 = bra.encrypt(m_1)
    c_2 = bra.encrypt(m_2)
    res = bra.decrypt(c_1 * c_2)
    assert res == (m_1 * m_2) % 2
    print(f'{m_1} * {m_2} = {res}')
    print("message 1,m_1 =", m_1)
    print("message 2,m_2 =", m_2)
    print("ciphertext c_1 =", c_1)
    print("ciphertext c_2 =", c_2)
    print("{} * {} = {}".format(m_1, m_2, res))

    # Multiplication 2
    m_1 = 1
    m_2 = 1
    c_1 = bra.encrypt(m_1)
    c_2 = bra.encrypt(m_2)
    res = bra.decrypt(c_1 * c_2)
    print(f'{m_1} * {m_2} = {res}')
    assert res == (m_1 * m_2) % 2
    print(f'{m_1} * {m_2} = {res}')
    print("message 1,m_1 =", m_1)
    print("message 2,m_2 =", m_2)
    print("ciphertext c_1 =", c_1)
    print("ciphertext c_2 =", c_2)
    print("{} * {} = {}".format(m_1, m_2, res))

    # Multiplication 3
    m_1 = 0
    m_2 = 0
    c_1 = bra.encrypt(m_1)
    c_2 = bra.encrypt(m_2)
    res = bra.decrypt(c_1 * c_2)
    print(f'{m_1} * {m_2} = {res}')
    assert res == (m_1 * m_2) % 2
    print(f'{m_1} * {m_2} = {res}')
    print("message 1,m_1 =", m_1)
    print("message 2,m_2 =", m_2)
    print("ciphertext c_1 =", c_1)
    print("ciphertext c_2 =", c_2)
    print("{} * {} = {}".format(m_1, m_2, res))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    if len(sys.argv) > 1 and 'core' in sys.argv[1]:
        tests_utils_core()
    if len(sys.argv) > 1 and 'regev' in sys.argv[1]:
        tests_utils_regev()
    if len(sys.argv) > 1 and 'bra' in sys.argv[1]:
        tests_utils_bra()

