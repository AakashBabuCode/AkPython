class Mystore:
    product_code=[]
    name=[]
    price=[]
    quant=[]
    #def __init__(self):
        #self.product_code=""
        #self.name=""
        #self.price=""
        #self.quant=""
    def getdata(self):
        self.p=int(input("Enter The no.products store:"))
        for x in range(self.p):
            self.product_code.append(int(input("Enter the Product Code:\n")))
            self.name.append(str(input("Enter the Name of the product:\n")))
            self.price.append(int(input("Enter the price of the product:\n")))
    def display(self):
        print("Aakash Department Store\n")
        print("---------------------------------------------\n")
        print("PRODUCT CODE\tPRODUCT NAME\tPRICE")
        for x in range(self.p):
            print(self.product_code[x],"\t\t",self.name[x],"\t\t",self.price[x])
        print("---------------------------------------------\n")
    def print_bill(self):
        total_amt=0
        for x in range(self.p):
            q=input("Enter Quantity of the prouduct Code of %d",self.product_code[x])
        self.quant.append(q)
        total_amt=total_amt+self.price[x]*self.quant[x]
        print("\tAakash Department Store\n")
        print("---------------------------------------------\n")
        print("PRODUCT CODE\tPRODUCT NAME\tPRICE\tQUANTITY\tTOTAL AMOUNT")
        for x in range(self.p):
            print(self.product_code[x],"\t\t",self.name[x],"\t\t",self.price[x],"\t\t",self.quant[x],"\t\t",self.price[x]*self.quant[x])
            print("---------------------------------------------\n")
            print("                                                          Total Amount=",total_amt)
            print("Thank you,Visit again!!!")
s=Mystore()
s.getdata()
s.display()
s.print_bill()
