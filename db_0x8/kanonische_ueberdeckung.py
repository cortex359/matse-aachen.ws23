#!/usr/bin/env python3

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'

R = ('A', 'B', 'C', 'D', 'E', 'F')
FD = [
    ([A],    [B, E]),
    ([A, E], [B, D]),
    ([F],    [C, D]),
    ([C, D], [B, E, F]),
    ([C, F], [B])
]

def attribut_huelle(FD, A):
    print('AttrHülle({}, {})'.format(str(FD), A))
    ah = (A)
    for alpha, beta in FD:
        pass

# Linksreduktion
for alpha, beta in FD:
    if len(alpha) > 1:
        print(alpha, "->", beta)
        for A in alpha:
            alpha_without_A = alpha.replace(A, '')
            attribut_huelle(FD, alpha_without_A)