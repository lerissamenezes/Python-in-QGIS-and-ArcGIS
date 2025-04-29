class Shopping:
    #Instantiating the class
    def __init__(self):
        self.cart={}
        
    #adding an item to the cart    
    def add_item(self,item,q=1):
        if item in self.cart:
            self.cart[item]+=q
        else:
            self.cart[item]=q
            
    #removing an item from the cart     
    def rem_item(self,item,q):
        #handles the case when the item is not in the cart
        if item not in self.cart:
            print(f"{item} not in cart")
            return
        if self.cart[item]>q:
            self.cart[item]-=q
        elif self.cart[item]==q:
            del self.cart[item]
        
            
    #displaying items in the cart         
    def show_cart(self):
        t=0
        for i,q in self.cart.items():
            t+=q
            print(f"{i}: {q}")
        print("Total:",t)
            