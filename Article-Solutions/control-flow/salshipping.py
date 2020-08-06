def cost_of_ground(weight):
      if (weight >= 8):
    shipping = 4
    ground_total = weight * shipping 
  else:
    shipping = 1
    ground_total = weight * shipping
  return ground_total 

  # testing the function
  print(cost_of_ground(8.4) + 20)

def drone_shipping(weight):
  if (weight <= 3):
    shipping = 4.50
    drone_total = weight * shipping
  else:
    hipping = 8
    drone_total = weight * shipping 
  return drone_total

  # testing the function
  print(drone_shipping(1.5)) 

def user_statement(weight): 
  if (cost_of_ground < drone_shipping):
    print('The cheapest shipping is ' + cost_of_ground + '.')
  elif (cost_of_ground > drone_shipping):
    print('The cheapest shipping is ' + drone_shipping + '.')
  else:
    print('Shipping ground and drone is the same cost.') 
