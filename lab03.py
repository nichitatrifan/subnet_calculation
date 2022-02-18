
def decimal_to_binary(num, bin_list:list):
    if num >= 1:
        decimal_to_binary(num // 2, bin_list)
        # do smth
        bin_list.append(num % 2)

def copy_list(copy_from:list, copy_to:list):
    for val in copy_from:
        copy_to.append(val)

def bin_list_to_dec(bin_list:list, dec_list:list):
    for i in range(0,32,8):
        dec_sum = 0
        for j, bit in enumerate(reversed(bin_list[i:i+8])):
            dec_sum += bit*(2**j)
        dec_list.append(dec_sum)

if __name__ == '__main__':

    # get IP address
    ip_arr_decimal = []
    flag = False
    while not flag:
        ip_addr = str(input('Enter the IPV4 address (0.0.0.0): '))
        if ip_addr.count('.') == 3:
            flag = True
            ip_arr_decimal = ip_addr.split('.')
        else:
            print('Enter a valid IP address!')
    
    # convert ip to int
    for i, val in enumerate(ip_arr_decimal):
        ip_arr_decimal[i] = int(val)

    # convert ip to bin
    ip_addr_bin = []
    for num in ip_arr_decimal:
        bin_num =[] 
        decimal_to_binary(num, bin_num)
        bin_size = len(bin_num) 
        if bin_size < 8:
            for i in range(8 - bin_size):
                bin_num.insert(0, 0)

        ip_addr_bin.append(bin_num)
    
    temp = []
    for i in ip_addr_bin:
        for j in i:
            temp.append(j)
    ip_addr_bin = temp

    mask_bits = int(input('Enter the mask bits: '))
    print('total occupied bits: ', mask_bits)
    network_id_addr_bin = []
    
    for i in range(mask_bits):
        network_id_addr_bin.append(ip_addr_bin[i])

    for i in range(32-mask_bits):
        network_id_addr_bin.append(0)

    network_id_addr_dec = []
    bin_list_to_dec(network_id_addr_bin,network_id_addr_dec)
    
    # A subnet consists of a “Network ID” and a “Broadcast ID”.
    # (first IP address in the network range)
    # The Network ID is its beginning number and 
    # it is always an even number. 
    # It designates a particular subnet to give it an identity 
    # on the network. 
    # When a subnet is refer to, 
    # the Network ID and the subnet's subnet mask is used.

    broadcast_ip_addr_bin = []
    copy_list(ip_addr_bin, broadcast_ip_addr_bin)
    for i in range(mask_bits, 32):
        broadcast_ip_addr_bin[i] = 1
    
    broadcast_ip_addr_dec = []
    bin_list_to_dec(broadcast_ip_addr_bin, broadcast_ip_addr_dec)
    
    ip = {
        'binary': ip_addr_bin,
        'decimal': ip_arr_decimal
    }

    network_id_addr = {
        'decimal': network_id_addr_dec,
        'binary': network_id_addr_bin
    }
    
    broadcast_ip_addr = {
        'decimal': broadcast_ip_addr_dec,
        'binary': broadcast_ip_addr_bin
    }

    print('IP decimal:            ', ip['decimal'])
    print('IP binary:             ', ip['binary'])
    print('Net ID decimal:        ', network_id_addr['decimal'])
    print('Net ID binary:         ', network_id_addr['binary'])
    print('Broadcast IP decimal:  ', broadcast_ip_addr['decimal'])
    print('Broadcast IP binary:   ', broadcast_ip_addr['binary'])

    # A broadcast address is an IP address 
    # that is used to target all systems on a specific subnet network 
    # instead of single hosts. 
    # In other words broadcast address allows information 
    # to be sent to all machines on a given subnet rather than to a specific machine.

    subnet_mask_ip_addr_bin = []
    copy_list(ip_addr_bin, subnet_mask_ip_addr_bin)
    for i in range(mask_bits):
        subnet_mask_ip_addr_bin[i] = 1

    for i in range(mask_bits, 32):
        subnet_mask_ip_addr_bin[i] = 0

    subnet_mask_ip_addr_dec = []
    bin_list_to_dec(subnet_mask_ip_addr_bin, subnet_mask_ip_addr_dec)

    subnet_mask_ip_addr = {
        'decimal': subnet_mask_ip_addr_dec,
        'binary': subnet_mask_ip_addr_bin
    }

    print('Subnet Mask decimal:   ', subnet_mask_ip_addr['decimal'])
    print('Subnet Mask binary:    ', subnet_mask_ip_addr['binary'])

    
    # in decimal representation

    max_num_host = None
    
    min_host_dec = []
    min_host_bin = []
    
    max_host_dec = []
    max_host_bin = []

    copy_list(network_id_addr_bin, min_host_bin)
    # Need to add 1
    bin_list_to_dec(min_host_bin, min_host_dec)
    print(bin(min_host_dec[0]))
