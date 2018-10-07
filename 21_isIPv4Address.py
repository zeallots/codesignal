def isIPv4Address(inputString):
    """An IP address is a numerical label assigned to each device 
    (e.g., computer, printer) participating in a computer network that uses 
    the Internet Protocol for communication. There are two versions of the 
    Internet protocol, and thus two versions of addresses. One of them is the 
    IPv4 address.

    IPv4 addresses are represented in dot-decimal notation, which consists of 
    four decimal numbers, each ranging from 0 to 255 inclusive, separated by 
    dots, e.g., 172.16.254.1.

    Given a string, find out if it satisfies the IPv4 address naming rules.  """
    string_split = inputString.split('.')
    for string in string_split:
        # check for any non-numbers in string
        if not string.isdecimal():
            return False
    if len(string_split) != 4:
        return False
    num_list = [int(num) for num in string_split]
    return max(num_list) < 256 and min(num_list) >= 0
    