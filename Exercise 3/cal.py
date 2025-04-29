class Calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Division by 0 is not possible"
        return a/b