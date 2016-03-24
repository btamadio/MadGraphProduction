#!/usr/bin/env python
import math
def calculateAlpha(q,nf=6.0):
    alpha = 0.1185
    beta0 = 33.0-2.0*nf
    beta0 /= (12*math.pi)
    mu = 91.1876
    return alpha/(1+alpha*beta0*math.log((q*q)/(mu*mu)))

def calculateWidth(mg,mq):
    alpha = calculateAlpha(mq)
    w = 2*alpha/3
    w *= (mq*mq-mg*mg)*(mq*mq-mg*mg)
    w /= mq*mq*mq
    return w
