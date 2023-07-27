airline_name = str(input())
number_tickets_adults = int(input())
number_children_tickets = int(input())
net_price_adult_ticket = float(input())
price_service_charge = float(input())

net_price_child_ticket = net_price_adult_ticket - ((70 / 100) * net_price_adult_ticket)
adult_ticket_price_service_charge = net_price_adult_ticket + price_service_charge
child_ticket_price_service_fee = net_price_child_ticket + price_service_charge

total_price = (number_children_tickets * child_ticket_price_service_fee) + (number_tickets_adults * adult_ticket_price_service_charge)
profit = (20 * total_price) / 100

print(f"The profit of your agency from {airline_name} tickets is {profit:.2f} lv.")