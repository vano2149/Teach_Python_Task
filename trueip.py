
import ipaddress
def is_valid_IP(strng):
    """
    Проверка валидности IP.
    """
    try:
        ipaddress.ip_address(strng)
        return print(True)
    except:
        return print(False)


is_valid_IP()