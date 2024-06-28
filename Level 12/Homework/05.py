#ვთხოვ მომხმარებელს შემოიტანოს 2 რიცხვი და ვარჩევ რიმელია უფრო დიდი
num_1 = int(input("please enter number:"))
num_2 = int(input("please enter number:"))
if (num_1 > num_2):
    print("num > num1")
if (num_2 > num_1):
    print("num_2 > num_1") 
if (num_1 == num_2):
    print("num_1 = num_2")
#ვწერ უმცირესი რიცხვიდან უდიდეს რიცხვამდე ყველა რიცხვს
for i in range(num_1,num_2):
    print(i)