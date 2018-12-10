# Hesap Makinesi:
seçenek1="(t) topla"
seçenek2="(ç) çıkar"
seçenek3="(çr) çarp"
seçenek4="(b) böl"
seçenek5="(k) karesini hesapla"
seçenek6="(kk) karekök hesapla"
print(seçenek1,seçenek2,seçenek3,seçenek4,seçenek5,seçenek6,sep="\n")
soru=input("Yapmak istediğiniz işlemim başharfini yazın: ") 
if soru=="t":
    sayı1=int(input("Toplama işlemi için ilk sayı: "))
    sayı2=int(input("Toplama işlemi için ikinci sayı: "))
    print("İşlemin sonucu: ",sayı1+sayı2)

elif soru=="ç":
    sayı3=int(input("Çıkarma işlemi için ilk sayı: "))
    sayı4=int(input("Çıkarma işlemi için ikinci sayı: "))
    print("İşlemin sonucu: ",sayı3-sayı4)

elif soru=="çr":
    sayı5=int(input("Çarpma işlemi için ilk sayı: "))
    sayı6=int(input("Çarpma işlemi için ikinci sayı: "))
    print("İşlemin sonucu: ",sayı5*sayı6)
    
elif soru=="b":
    sayı7=int(input("Bölme işlemi için ilk sayı: "))
    sayı8=int(input("Bölme işlemi için ikinci sayı: "))
    print("İşlemin sonucu: ",sayı7/sayı8)

elif soru=="k":
    sayı9=int(input("Karesini hesaplamak istediğin sayı: "))
    print(sayı9, "Sayısının karesi: ",sayı9**2)

elif soru=="kk":
    sayı10=int(input("Körekökünü öğrenmek istediğin sayı: "))
    print(sayı10,"Sayısının karekökü: ",sayı10**0.5)

else:
    print("Yanlış giriş.")
    print("Aşağıdaki seçenekleri kullanın: ",
          seçenek1,seçenek2,seçenek3,seçenek4,seçenek5,seçenek6,sep="\n")    
