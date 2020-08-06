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
        shipping = 8
        drone_total = weight * shipping
    return drone_total


# testing the function
print(drone_shipping(1.5))


def premium_shipping(weight):
    if (weight <= 3):
        shipping = 4.50
        premium_total = weight * shipping
    else:
        shipping = 8
        premium_total = weight * shipping
    return premium_total


def user_statement(weight):
    ground = cost_of_ground(weight)
    drone = drone_shipping(weight)
    premium = premium_shipping(weight)
    msg = "The cheapest shipping is: "

    if drone < ground and drone < premium:
        print(str(msg) + str
              (drone) + '.')
        return drone
    elif ground < drone and ground < premium:
        print(str(msg) + str(ground) + '.')
        return ground
    else:
        print(str(msg) + str(premium))
        return premium


print(user_statement(4.8))
print(user_statement(41.5))
