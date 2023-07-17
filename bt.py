khoa=int(input("nhap so khoa: \t"))
bang=int(input("nhap so bang: \t"))
nong=int(input("nhap so nong: \t"))

s=khoa*45+bang*30+nong*25

if s<=1000:
    hh=s*10/100
elif s<=1800:
    hh=s*15/100
else: hh=s*20/100
print("tong tien",hh)
print("tong tien",s)