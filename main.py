import random
from random import randint

print("Sayı Tahmin Oyununa Hoşgeldiniz!")

goalNumber = random.randint(1,100)
tahminHakki = 10

try:
    playerGuess = int(input("Lütfen 1'den 100'e kadar bir sayı giriniz: "))
    if playerGuess < 0:
        print("Lütfen 1'den 100'e kadar bir sayı giriniz!!!")
    elif playerGuess > 100:
        print("Lütfen 1'den 100'e kadar bir sayı giriniz!!!")
    else:
        while tahminHakki > 0:

            if playerGuess > goalNumber:
                print("Daha küçük bir sayı giriniz")
            elif playerGuess < goalNumber:
                print("Daha büyük bir sayı giriniz")
            else:
                print("Tebrikler kazandınız!!!")
                break

            tahminHakki = tahminHakki - 1
            playerGuess = int(input("Tekrar deneyin: "))

        if tahminHakki == 0:
            print(f"Kaybettiniz!!! Cevap {goalNumber} olacaktı!!!")

except:
    print("Lütfen 1'den 100'e kadar bir sayı giriniz!!!")


