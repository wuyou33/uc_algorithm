# -*- coding: utf-8 -*-
import sympy as sp
import rst_symbtools.symb_tools as st

n = 2  # Anzahl der Freiheitsgrade
nq = 1  # Anzahl der Eingänge

Neq = n - nq  # Anzahl der mechanischen Gleichungen (ohne definitorische)


eq_coeffsA = []
eq_coeffsB = []
eq_coeffsC = []

all_coeffs = []
# iterieren über die Gleichungen
for i in xrange(Neq):
    coeffsA = []
    coeffsB = []
    coeffsC = []
    coeffs = []
    # iterieren über die einzelnen Freiheitsgrade
    for j in xrange(n):
        # drei Ableitungsordnungen
        A = sp.Symbol("A%i_%i" % (i + 1, j + 1))
        B = sp.Symbol("B%i_%i" % (i + 1, j + 1))
        C = sp.Symbol("C%i_%i" % (i + 1, j + 1))
        
        coeffsA.append(A)
        coeffsB.append(B)
        coeffsC.append(C)
        
        coeffs.extend([A, B, C])
     
     # jede Gleichung bekommt eine separate Liste
    eq_coeffsA.append(coeffsA)
    eq_coeffsB.append(coeffsB)
    eq_coeffsC.append(coeffsC)
     
    all_coeffs.extend(coeffs)
        

diff_symbols = sp.Matrix(all_coeffs)

#x1, x2, x3, x4, x5, x6 = sp.symbols("x1, x2, x3, x4, x5, x6")


vec_x = sp.Matrix( sp.symbols("x1:%i" % (n*2 + 1)) )

theta = vec_x[:n, :]
mu = vec_x[n:, :]

vec_xdot = st.perform_time_derivative(vec_x, vec_x)
thetadot = st.perform_time_derivative(theta, vec_x)
mudot = st.perform_time_derivative(mu, vec_x)


# definitorische Gleichungen
eq_defin = thetadot - mu


# Container um zusätzliche Information über das Beispiel zu speichern
data = st.Container()

data.P0 = AA = sp.Matrix(eq_coeffsA) # P0
data.P1 = BB = sp.Matrix(eq_coeffsB) # P1
data.P2 = CC = sp.Matrix(eq_coeffsC) # P2


#eq_mech = AA*theta + BB*mu + CC*mudot
from ipHelp import IPS
IPS()
eq_mech = AA*theta + BB*thetadot + CC*mudot

F_eq_orig = F_eq = st.row_stack(eq_defin, eq_mech)

sys_name = "mechanik_generisch_n2_nq1_wagen_pendel"



#F_eq = sp.Matrix([
        #[ xdot1 - x4 ],
        #[ xdot2 - x5 ],
        #[ xdot3 - x6 ],
        #[ a2*xdot4 + b2*xdot5 + c2*xdot6 + b1*x5 + c1*x6 + b0*x2 + c0*x3 ]])
        #~ [ a2*xdot4 + b2*xdot5 + c2*xdot6 + b1*x5 + c1*x6 + b0*x2 + c0*x3 + a0*x1 + a1*x4]])
