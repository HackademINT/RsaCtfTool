#! /usr/bin/env python3
import gmpy2
import binascii

class chinese_attack:
    def __init__(self):
        self.ln = [1]*len(self.attackobjs)
        self.ntot = 0
        self.m = 0
        self.test = False
    def system_solve(self)
    """
    This function find the solution of the congruency system
    """
        for i in range(self.len):
            self.ntot *= self.attackobjs[k].pub_key.n
            for j in range(self.len):
                if i != j:
                    self.ln[i] *= self.attackobjs[k].pub_key.n
        for i in range(self.len):
            self.ln[i] *= gmpy2.invert(self.ln[i], self.attackobjs[k].pub_key.n)
        for i in range(self.len):
            self.m += self.attackobjs[k].cipherdec * self.ln[i]
        self.m = m % self.ntot

        self.m, self.test = gmpy2.iroot(self.m, 3)

        if not self.test:
                print("Racine non entiere")
                exit()
        def print_value(self):
            self.m=str(hex(self.m))[2:] #long
            self.m=binascii.unhexlify(self.m)
            return self.m
