class Bank:
    bank_information="Bank_details :"
    def __init__(self,bname,baddr,bcode,bifsc):
        self.bank_name=bname
        self.bank_addr=baddr
        self.branch_code=bcode
        self.branch_IFSC=bifsc
    def bank(self):
        print(Bank.bank_information)
    def display_bank(self):
        print("Enter the bank name :",self.bank_name)
        print("Enter the bank address :",self.bank_addr)
        print("Enter the branch code :",self.branch_code)
        print("Enter the IFSC code :",self.branch_IFSC)
a=input("Enter the bank_name :")
b=input("Enter the Bank_address :")
c=int(input("Enter the Branch_code :"))
d=int(input("Enter the IFSC code :"))
b1=Bank(a,b,c,d)
b1.bank()
b1.display_bank()
print("~"*40)
a1=input("Enter the bank_name :")
b1=input("Enter the Bank_address :")
c1=int(input("Enter the Branch_code :"))
d1=int(input("Enter the IFSC code :"))
b2=Bank(a1,b1,c1,d1)
print("~"*40)
b2.display_bank()
