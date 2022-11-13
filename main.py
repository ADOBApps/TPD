# _*_ coding: utf-8 _*_
"""
Created on 08/07/2022
    Functions to graph DTP data
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

# from mycontrollers.math.linearmath import LSOnlyGraph
# from mycontrollers.math.linearmath import LinearSolveComp
# from mycontrollers.math.linearmath import LinearSolve
from myviews.graphmaker import Graphmaker

# ==========================================================================
''' Fraction surface coverage, C_{A}^{n}=0,2 '''

x_activation_e = [80, 110, 140, 170, 210]
y1_T_Beta1 = [285.778, 390.278, 492.328, 595.194, 729.9]
y2_T_Beta3 = [294.759, 405.529, 508.656, 613.971, 754.392]
y3_T_Beta10 = [305.372, 416.402, 526.616, 636.014, 780.517]
# Desorption rate
r1_T_Beta1 = [0.0232021, 0.018691, 0.0147355, 0.0113909, 0.00962549]
r2_T_Beta3 = [0.0655879, 0.0513954, 0.0398743, 0.033988, 0.0276233]
r3_T_Beta10 = [0.216331, 0.160310, 0.129230, 0.106845, 0.0884966]

'''Activation energy = 120 kJ/mol'''
x_CA = [0.2, 0.4, 0.6, 0.8, 1.0]
ca_T_r1_Beta1 = [0.00333646, 0.00682132, 0.010232, 0.0135684, 0.0166823]
ca_T_r2_Beta3 = [0.00945724, 0.0189516, 0.028543, 0.037829, 0.047081]
ca_T_r3_Beta10 = [0.0295631, 0.0589407, 0.0886336, 0.118178, 0.147815]

ca_t1_Beta1 = [614.373, 613.665, 613.665, 613.665, 615.788]
ca_t2_Beta3 = [213.193, 213.193, 213.193, 213.193, 213.193]
ca_t3_Beta10 = [66.7311, 66.7311, 66.7311, 66.7311, 66.7311]
# ==========================================================================


mygraph = Graphmaker()

# Plot graph and linearRegression type Time vs Temperature


def Makegrap():

    # Temperature vs Activation energy
    mygraph.GraphX3Y3(
        r"Energía de activación en función de la temperatura",
        r"Temperatura (K)",
        r"Energía de activación $(\frac{KJ}{mol})$",
        "EAvsT.png",
        y1_T_Beta1,
        y2_T_Beta3,
        y3_T_Beta10,
        x_activation_e,
        x_activation_e,
        x_activation_e,
        '4', 'd', '+',
        r'$\beta_{1}$',
        r'$\beta_{3}$',
        r'$\beta_{10}$',
        4
    )

    # Desorption rate vs Temperature
    mygraph.GraphX3Y3(
        r"Velocidad de desorción en función de la temperatura",
        r"Temperatura (K)",
        r"Velocidad de desorción $(\frac{mol}{L\dot{}s})$",
        "VDvsT.png",
        y1_T_Beta1,
        y2_T_Beta3,
        y3_T_Beta10,
        r1_T_Beta1,
        r2_T_Beta3,
        r3_T_Beta10,
        '4', 'd', '+',
        r'$\beta_{1}$',
        r'$\beta_{3}$',
        r'$\beta_{10}$',
        2
    )

    # Desorption rate vs Fractional surface coverage
    '''
    "Velocidad de desorción en función
    de la fracción de cobertura superficial"
    '''
    mygraph.GraphX1Y3(
        r"$\nu{}=f(C_{A}^{n})$",
        r"$C_{A}^{n}$",
        r"$\nu{}(\frac{mol}{L\dot{}s})$",
        "VDvsCA.png",
        x_CA,
        ca_T_r1_Beta1,
        ca_T_r2_Beta3,
        ca_T_r3_Beta10,
        '*', 's', '8',
        r'$\beta_{1}$',
        r'$\beta_{3}$',
        r'$\beta_{10}$',
        1
    )

    # Desorption time vs Fractional surface coverage
    '''
    "Tiempo de desorción en función
    de la fracción de cobertura superficial"
    '''
    mygraph.GraphX1Y3(
        r"$t=f(C_{A}^{n})$",
        r"$C_{A}^{n}$",
        r"$Tiempo(s)$",
        "TimevsCA.png",
        x_CA,
        ca_t1_Beta1,
        ca_t2_Beta3,
        ca_t3_Beta10,
        'd', 'h', '1',
        r'$\beta_{1}$',
        r'$\beta_{3}$',
        r'$\beta_{10}$',
        2
    )


if __name__ == "__main__":
    Makegrap()
