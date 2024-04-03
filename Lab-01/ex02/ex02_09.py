def kiem_tra_so_nguyen_to(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# Kiểm tra số nguyên tố và in kết quả 
number = int (input("Nhập vào số cần kiểm tra: ")) 
if kiem_tra_so_nguyen_to (number): print (number, "là số nguyên tố.")
else:
    print (number, "không phải là số nguyên tố.")