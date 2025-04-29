class Calculator:
    # this function adds two values 
    def add(self,a,b):
        return a+b
    
    # this function subtracts two values 
    def sub(self,a,b):
        return a-b
    
    # this function multiplies two values 
    def mul(self,a,b):
        return a*b
    
    # this function divides two values 
    def div(self,a,b):
        if b==0:
            #handling an exception
            return "Division by 0 is not possible"
        return a/b