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
  ground = ground_total(weight)
  drone = drone_shipping(weight)
  premium = premium_shipping
    
  if drone < ground and drone < premium:
    print('The cheapest shipping is ' + str
    (drone) + '.') 
  elif ground < drone and ground < premium:
    print('The cheapest shipping is ' + str(ground) + '.') 
  else: 
    print('You should ship with ' + str(premium)) 
  
  print(user_statement(4.8))
  print(user_statement(41.5))
