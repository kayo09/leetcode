#mf made me lose my streak :P
class Solution(object):
    def judgeSquareSum(self, c):
        potential=list(primerange(1,c))
        print(potential)
        residual=c
        if c==2 or c==1 or c==0: return True
        for num in potential: 

            if pow(num,2)>c: 
                potential.remove(num)
            
            residual-=pow(num,2)
            if(residual==0): return True
       
            if(c-pow(num,2))==1 or c-pow(num,2)==0:

                return True 
            if c%pow(num,2)==0 and c-2*pow(num,2)==0:
                return True
        
        return False  
            

def primerange(start, end):
    if end <= 2:
        return []
    sieve = [True] * end
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(end**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end, i):
                sieve[j] = False
    return [x for x in range(start, end) if sieve[x]]



        
        
solution=Solution()
c=16
geek=solution.judgeSquareSum(c)
print(geek)
