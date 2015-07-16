#####################################################################
# Double Trouble
# ------------------------------------------------------------------
# Description:
# ------------------------------------------------------------------
# If X = 421052631578947368, it  is
# a double-trouble number, since 2X = 842105263157894736 
# which is a right rotation of X.
# The number X is a double-trouble number in the number system 
# with base 10. Any number system with base p >= 2, however, 
# has many such double-trouble numbers. 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Run it like:
# python dyson_parasitic.py --n 2
# ipython: %run dyson_parasitic.py --n 2
# 
# ------------------------------------------------------------------
# Original Author: Akul Mathur - @codecakes
# Maintainer(s):
# - Akul Mathur - @codecakes
#####################################################################

import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)


def n_parasitic(n, base=10):
    '''Get n-parasitic number for base'''
    constant = (base*n - 1)
    for m in xrange(1, constant+1):
        res = (base**m - 1)/constant
        res_str = str(res)
        res_str0 = '0' + res_str
        full = n * res
        rotate = res_str0[-1] + res_str0[:-1]
        #print res*n, full
        if res != 0 and int(rotate) == full:
            return ' '.join(list(res_str0))if int(res_str0) == res \
            else ' '.join(list(res_str))

def b_parasitic(base):
    '''A Brute Force approach to non base 10 numbers'''
    num = 1
    res = None
    while 1:
        new_num = num << 1
        num_base_str = int2base(num, base)
        new_num_base_str = int2base(new_num, base)
        if num_base_str[-1] + num_base_str[:-1] == new_num_base_str:
            #print num
            res=  num_base_str
        if num_base_str[-1] + num_base_str[:-1] +'0'  == new_num_base_str:
            #print num
            res = '0' + num_base_str[-1] + num_base_str[:-1]
        if res:
            res = list(res)
            return ' '.join([str(string.letters.index(let) + 10) \
            if let in string.letters else str(let) for let in res])
        num += 1
        
    
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dry', action='store_true', dest='dry', \
    default=False, help='Run a dry test first')
    
    parser.add_argument('--n', type=int, nargs ='?', \
    action='store', dest='n',\
    default=2, help='which n-Parasitic number for base 10?')
    
    args = parser.parse_args()
    
    assert isinstance(args.n, int)
    
    if args.dry:
        for i in xrange(2, 10):
            print n_parasitic(i)
    
    if 1 < args.n <= 9:
        print "For base %s the double-trouble number is" %(args.n)
        print n_parasitic(args.n)
    
    bases = raw_input("Enter the bases for double trouble numbers: ").split()
    for base in bases:
        print "For base %s the double-trouble number is" %(base)
        if int(base) == 10:
            print n_parasitic(2)
        else:
            print b_parasitic(int(base))