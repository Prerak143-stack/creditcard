

card_number = input("Please enter your card number : ")

total = 0
while len(card_number) != 16:
    print("Please enter valid 16 digit card number")
    card_number = input("Please enter your card number : ")

for i in range(16,0,-1):
    if (i-1)%2 == 0:
        temporary = int(card_number[i-1:i])*2
        if temporary > 9:
            half_sum = (temporary // 10 ) + (temporary % 10)
        else:
            half_sum = temporary
        total = total + half_sum
    else:
        total = total + int(card_number[i-1:i])

if total % 10 == 0:
    validity = " is valid"
else:
    validity = " is invalid"

count = 0

type_of_card = "null"

for c in range (1,16,1):
 
    count = count + 1
     
    if ((int(card_number[0:c])) == 37 or (int(card_number[0:c])) == 34 )  :
        type_of_card = "American Express"
        
    elif (int(card_number[0:c])) == 6011 :
        type_of_card = "Discover"

    elif (int(card_number[0:c])) == 4 :
        type_of_card = "Visa"

    elif ((int(card_number[0:c])) == 51 or (int(card_number[0:c])) == 52 or (int(card_number[0:c])) == 53 \
          or (int(card_number[0:c])) == 54 or (int(card_number[0:c])) == 55):
        type_of_card = "MasterCard"


if type_of_card == str("null") :
    print("We do not accept this kind of card")
    
else:
    print("Your " + type_of_card + " with number " + card_number[:16] + validity)






