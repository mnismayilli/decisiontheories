import numpy as np

def tax_calc_ra():
'''
This function calculates TAX value of lottery for risk-averse decision-maker
'''
    sumw = 0
    sumx = 0
    beta=1
    if beta <= 1:
        delta = 1
    else:
        delta = -1
    for i in range(0, n_branch):
        p = prob[i]
        wa = p**gamma
        sumw = sumw +wa 
        sumx = sumx +wa* (out[i]**beta)
        for j in range(i, n_branch):
            pj = prob[j]
            if delta>0:
                omeg = (delta/(n_branch+1))*(p**gamma)
            else:
                omeg = (delta/(n_branch+1))*(pj**gamma)
            sumx = sumx +omeg*((out[j]**beta)-(out[i]**beta))

    sumx = sumx/sumw

    pred = sumx**(1/beta)
    return pred
    
def tax_calc_rt():
'''
This function calculates TAX value of lottery for risk-taker decision-maker
'''
    sumw = 0
    sumx = 0
    beta=1.1
    if beta <= 1:
        delta = 1
    else:
        delta = -1
    for i in range(0, n_branch):
        p = prob[i]
        wa = p**gamma
        sumw = sumw +wa 
        sumx = sumx +wa* (out[i]**beta)
        for j in range(i, n_branch):
            pj = prob[j]
            if delta>0:
                omeg = (delta/(n_branch+1))*(p**gamma)
            else:
                omeg = (delta/(n_branch+1))*(pj**gamma)
            sumx = sumx +omeg*((out[j]**beta)-(out[i]**beta))

    sumx = sumx/sumw

    pred = sumx**(1/beta)
    return pred
    
    
    
    
