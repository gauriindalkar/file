banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"]
for i in banks_list:
    file=open("bankfile.txt","a")
    file.write(i)
    file.close()
    