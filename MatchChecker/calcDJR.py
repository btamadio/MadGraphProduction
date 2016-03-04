#!/usr/bin/env python
from math import sqrt
from ROOT import *
import sys
from pprint import pprint
class DJRcalculator:
    """Calculates the transition values Q_{n->n-1} given a list of TLorentzVectors"""
    Qn = []
    p4List = []
    def __init__(self,p4):
        self.p4List = p4
        self.calcQn()
    def calcQn(self):
        if len(self.p4List) == 0:
            print 'No elements found in p4List. Something has gone wrong! Exiting.'
            sys.exit(1)
        elif len(self.p4List) == 1:
            self.Qn.append(self.calcKT(self.p4List[0]))
            self.Qn.reverse()
            return
        else:
            res = self.calcKTmin()
            i = res[0]
            j = res[1]
            ktMin = res[2]
            self.Qn.append(ktMin)
            if i == j:
                self.p4List.pop(i)
            elif j > i:
                self.deleteAndCombine(i,j)
            else:
                print 'Index i less than j. Something has gone horribly wrong! Exiting.'
                sys.exit(1)
            self.calcQn()
    def getQ(self,n):
        if len(self.Qn) == 0:
            print 'Error. No particles in list. Exiting.'
            sys.exit(1)
        elif n > len(self.Qn):
            print 'Highest allowed transition rate is %i->%i. Requested %i->%i. Exiting' %(len(self.Qn),len(self.Qn)-1,n,n-1)
            sys.exit(1)
        elif n < 1:
            print 'Lowest allowed transition rate is 1->0. Requested %i->%i. Exiting.' % (n,n-1)
            sys.exit(1)
        else:
            return self.Qn[n-1]
    def calcKT(self,p4a,p4b=0,d=0.4):
        if 'TLorentzVector' in type(p4b).__name__:
            deltaY = p4a.Rapidity() - p4b.Rapidity()
            deltaPhi = p4a.Phi() - p4b.Phi()
            kt = min(p4a.Pt()*p4a.Pt(),p4b.Pt()*p4b.Pt())
            kt *= (deltaY*deltaY+deltaPhi*deltaPhi)/(d*d)
            return sqrt(kt)
        else:
            return p4a.Pt()
    def calcKTmin(self):
        ktMin = float("inf")
        iMin = -1
        jMin = -1
        ktij = 0
        for i in range(len(self.p4List)):
            for j in range(i,len(self.p4List)):
                if i==j:
                    ktij = self.calcKT(self.p4List[i])
                else:
                    ktij = self.calcKT(self.p4List[i],self.p4List[j])
                print i,j,ktij
                if ktij < ktMin:
                    iMin = i
                    jMin = j
                    ktMin = ktij
        print 'Minimum found: ',iMin,jMin,ktMin
        return(iMin,jMin,ktMin)
    def deleteAndCombine(self,i,j):
        p4a = self.p4List.pop(j)
        p4b = self.p4List.pop(i)
        p4tot = p4a+p4b
        self.p4List.append(p4tot)
p41 = TLorentzVector(10,10,11,150)
p42 = TLorentzVector(15,1,0.5,200)
p43 = TLorentzVector(15,1.1,0.5,200)
d = DJRcalculator([p41,p42,p43])
print 'Q_3->2 = ',d.getQ(3)
print 'Q_2->1 = ',d.getQ(2)
print 'Q_1->0 = ',d.getQ(1)
