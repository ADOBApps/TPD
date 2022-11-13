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

mygraph = Graphmaker()

# ==========================================================================

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


if __name__ == "__main__":
    Makegrap()
