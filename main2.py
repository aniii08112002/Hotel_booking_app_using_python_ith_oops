import pandas
import pandas as pd

dataframe = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark="The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = dataframe.loc[dataframe["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        dataframe.loc[dataframe["id"] == self.hotel_id, "available"] = "no"
        dataframe.to_csv("hotels.csv", index=False)

    def available(self):
        availability = dataframe.loc[dataframe["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"

class ReservationTickets:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"\n\nReservation Details:\nCustomer Name: {self.customer_name}\nHotel ID: {self.hotel_object.hotel_id}\nHotel Name: {self.hotel_object.name}"
        return content


class CreditCard:
    def __init__(self,number):
        self.number=number

    def validate(self,expiration,holder,cvc):
        card_date={"number":self.number,"expiration":expiration,"holder":holder,"cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self,given_password):
        password=df_cards_sectrity.loc[df_cards_sectrity["number"]==self.number,"password"].squeeze()
        if password=given_password:
            return True
        else:
            return False


        


print(dataframe)

hotel_ID = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card=SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expirationn="12/26",holder='AMIRUDH',cvc='123'):
        if credit_card.authenticate(given_password="mypass"):

            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationTickets(customer_name=name, hotel_object=hotel)
            ticket_content = reservation_ticket.generate()
            print(ticket_content)
        else:
            print("Credit Card authentication Failed")
    else:
        print("there as a problem with your payment")
else:
    print("Hotel unavailable")
hotel1=Hotel(hotel_iD="188")
hotel2=Hotel(hotel_id="134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)