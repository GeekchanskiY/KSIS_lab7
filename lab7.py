def byte_str(string: str) -> str:
    return f"{int(string):08b}"


def str_int(string: str) -> str:
    return str(int(string, 2))


def defineSubnetClass(ip: str):
    bit_str = byte_str(ip.split(".")[0])
    if bit_str[0] == "0":
        return "A"
    else:
        if bit_str[1] == "0":
            return "B"
        else:
            if bit_str[2] == "0":
                return "C"
            else:
                if bit_str[3] == "0":
                    return "D"
                else:
                    return "E"


def hostid(ipand: str, snclass):
    res = ipand
    crkt: int
    if snclass == "A":
        crkt = 8
    elif snclass == "B":
        crkt = 16
    elif snclass == "C":
        crkt = 24
    else:
        return
    for i in range(0, crkt+1):
        res = res[:i] + "0" + res[i+1:]
    #print(res)
    return res








if __name__ == '__main__':
    ip = "172.16.192.1"
    mask = "255.255.128.0"

    ip_bytes = byte_str(ip.split(".")[0]) + byte_str(ip.split(".")[1])\
             + byte_str(ip.split(".")[2]) + byte_str(ip.split(".")[3])
    ip_int = int(ip_bytes, 2)
    mask_bytes = byte_str(mask.split(".")[0]) + byte_str(mask.split(".")[1])\
             + byte_str(mask.split(".")[2]) + byte_str(mask.split(".")[3])
    mask_int = int(mask_bytes, 2)

    print("логическое и (ID подсети)")
    mask_ip_and = f"{ip_int & mask_int:08b}"
    print(mask_ip_and)

    print(f"Класс ip адреса {ip}")
    print(defineSubnetClass(ip))

    #print("Номер подсети логическое или")


    print("ID подсети, ID хоста")
    host_id = (hostid(ip_bytes, defineSubnetClass(ip)))
    print(
        f"{int(mask_ip_and[0: 8], 2)}.{int(mask_ip_and[8: 16], 2)}."
        f"{int(mask_ip_and[16: 24], 2)}.{int(mask_ip_and[24: 32], 2)}")
    print(
        f"{int(host_id[0: 8], 2)}.{int(host_id[8: 16], 2)}."
        f"{int(host_id[16: 24], 2)}.{int(host_id[24: 32], 2)}")