# Name=(input('Enter your Name:'))
# print("Hello "+ Name)
questions = [
    ["Who is Prime Minster of India?", "Modi", "Rahul", "Yogi", "Veeru" , 1
    ],
[
    "Ekatha Harbour is the biggest Indian grant-in-aid projects in which country?", "Bangladesh", "Maldives", "Nepal", "Myanmar" , 2
    ],
[
    "U.T. Khader was unanimously elected Speaker of which state Legislative Assembly?", "Tamil Nadu", "Karnataka", "Kerala", "Telangana" , 2
    ],
[
    "Stable Auroral Red (SAR) Arc has been observed recently in which state/UT?", "West Bengal", "Ladakh", "Assam", "Goa" , 2
    ],
[
    "Which institution will launch the ONDC Academy?" ,"SEBI", "EXIM Bank", "ONDC", "ECGC" , 3
    ],
[
    "Araku Valley Coffee, which was seen in the news, is from which state?" ,"Tamil Nadu", "Andhra Pradesh", "Assam", "West Bengal" , 2
    ],
[
    "Special Protection Group (SPG) is the force responsible for the security of which personality?" ,"President", "Prime Minister", "Chief Justice of India", "Vice President" , 2
    ],
[
    "Prime Minister Narendra Modi released which coin to mark the inauguration of the new Parliament building?" ,"Rs 50", "Rs 75", "Rs 100", "Rs 200" , 2
    ],
[
    "Who is Cricketer of India in this?" ,"Virat", "Rahul Gandhi", "Modi", "Veeru" , 1
    ]]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0 
try:
 for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"a.{questions[i][1]}               b.{questions[i][2]}")
    print(f"c.{questions[i][3]}               d.{questions[i][4]}")
    reply = int(input("Enter ur answer(1-4): "))
    if reply == question[-1]:
        print(f"Correct Answer u have won Rs.{levels[i]}")
        if (i==4):
            money == 10000
        elif(i==9):
            money == 320000
        elif(i==14):
            money == 10000000
    else:
        print("Wrong Answer")
        break
 print(f"Ur take home Money is {money}")
except:
   print("Invaild Input")
