def valid_ip_check(i):
    try:
        i_list = i.split(".")
    except ValueError as e:
        return print(e)
    if len(i_list) != 4:
        return print("This is an invalid IP address")

    for each in i_list:
        if len(each) > 3:
            return print("This is an invalid IP address")
        if int(each) > 256 or int(each) < 0:
            return print("This is an invalid IP address")
    return print("This is a valid IP address")


# user_input = input("Please enter the IP address(IPV4) :")
# valid_ip_check(user_input)
valid_ip_check("100.00000.0.0")
