training_tax = int(input())

# • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

basketball_sneakers = training_tax - ((40 / 100) * training_tax)
basketball_suit = basketball_sneakers - ((20 / 100) * basketball_sneakers)
basketball_ball = basketball_suit / 4
basketball_accessories = basketball_ball / 5

total_price = training_tax + basketball_sneakers + basketball_suit + basketball_ball + basketball_accessories

print(total_price)