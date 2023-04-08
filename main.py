import utility
import shopping.shopping_cart as sh
import sys
if __name__== '__main__':
    print(utility.mul(int(sys.argv[1]),int(sys.argv[2])),utility.div(int(sys.argv[3]),int(sys.argv[4])))
    print(sh.buy('mango','apple','banana'))