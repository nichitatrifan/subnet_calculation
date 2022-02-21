
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

    ################ GET IP ADDRESS ################
    ip_arr_decimal = []
    flag = False
    while not flag:
        ip_addr = str(input('Enter the IPV4 address (0.0.0.0): '))
        if ip_addr.count('.') == 3:
            flag = True
            ip_arr_decimal = ip_addr.split('.')
        else:
            print('Enter a valid IP address!')
    
    ################ GET MASK BITS ################
    mask_bits = int(input('Enter the mask bits: '))
    while mask_bits <= 0 or mask_bits > 32:
        print('Mask bits range: 1 - 32')
        print('Try again!')
        mask_bits = int(input('Enter the mask bits: '))

    ################ CONVERT IP TO INT ################
    for i, val in enumerate(ip_arr_decimal):
        ip_arr_decimal[i] = int(val)

    ################ CONVERT IP TO BIN ################
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

    ################ NETWORK ID ################
    network_id_addr_bin = []    
    for i in range(mask_bits):
        network_id_addr_bin.append(ip_addr_bin[i])

    for i in range(32-mask_bits):
        network_id_addr_bin.append(0)

    network_id_addr_dec = []
    bin_list_to_dec(network_id_addr_bin,network_id_addr_dec)

    ################ BROADCAST IP ################
    broadcast_ip_addr_bin = []
    copy_list(ip_addr_bin, broadcast_ip_addr_bin)
    for i in range(mask_bits, 32):
        broadcast_ip_addr_bin[i] = 1
    
    broadcast_ip_addr_dec = []
    bin_list_to_dec(broadcast_ip_addr_bin, broadcast_ip_addr_dec)

    ################ SUBNET MASK IP ################
    subnet_mask_ip_addr_bin = []
    copy_list(ip_addr_bin, subnet_mask_ip_addr_bin)
    for i in range(mask_bits):
        subnet_mask_ip_addr_bin[i] = 1

    for i in range(mask_bits, 32):
        subnet_mask_ip_addr_bin[i] = 0

    subnet_mask_ip_addr_dec = []
    bin_list_to_dec(subnet_mask_ip_addr_bin, subnet_mask_ip_addr_dec)

    ################ HOST RANGE ################
    if mask_bits <= 30:
        min_host_dec = []
        min_host_bin = []
        
        max_host_dec = []
        max_host_bin = []

        copy_list(network_id_addr_dec, min_host_dec)
        
        if min_host_dec[-1] == 255:
            if min_host_dec[-2] == 255: 
                if min_host_dec[-3] == 255:
                    min_host_dec[-4] += 1
                else:
                    min_host_dec[-3] += 1
            else:
                min_host_dec[-2] += 1
        else:
            min_host_dec[-1] += 1

        for dec_num in min_host_dec:
            min_host_bin.append(bin(dec_num))

        copy_list(broadcast_ip_addr_dec, max_host_dec)

        if max_host_dec[-1] == 0:
            if max_host_dec[-2] == 0: 
                if max_host_dec[-3] == 0:
                    max_host_dec[-4] -= 1
                else:
                    max_host_dec[-3] -= 1
            else:
                max_host_dec[-2] -= 1
        else:
            max_host_dec[-1] -= 1

        for dec_num in max_host_dec:
            max_host_bin.append(bin(dec_num))
        
        # usable_hosts = 1
        # for i in range(4):
        #     usable_hosts += abs(max_host_dec[i] - min_host_dec[i])
        # total_hosts = usable_hosts + 2

        total_hosts = 2**(32-mask_bits)
        usable_hosts = total_hosts - 2

    elif mask_bits == 31:
        min_host_dec = 'N/A'
        max_host_dec = 'N/A'
        usable_hosts = 0
        total_hosts = 2
    else:
        min_host_dec = 'N/A'
        max_host_dec = 'N/A'
        usable_hosts = 0
        total_hosts = 1
    
    ################ OUTPUT ################
    ip = {
        'binary': ip_addr_bin,
        'decimal': ip_arr_decimal
    }

    network_id_addr = {
        'decimal': network_id_addr_dec,
        'binary': network_id_addr_bin
    }

    subnet_mask_ip_addr = {
        'decimal': subnet_mask_ip_addr_dec,
        'binary': subnet_mask_ip_addr_bin
    }
    
    broadcast_ip_addr = {
        'decimal': broadcast_ip_addr_dec,
        'binary': broadcast_ip_addr_bin
    }

        
    host_range = {
        'max': max_host_dec,
        'min': min_host_dec,
        'allowed_hosts': usable_hosts,
        'total_hosts': total_hosts
    }

    # print('IP decimal:            ', ip['decimal'])
    # print('Net ID decimal:        ', network_id_addr['decimal'])
    # print('Broadcast IP decimal:  ', broadcast_ip_addr['decimal'])
    # print('Subnet Mask decimal:   ', subnet_mask_ip_addr['decimal'])
    # print('Host Range:             ' + str(host_range['min']) + ' - ' + str(host_range['max']))
    # print('Number of Usable Hosts: ', host_range['allowed_hosts'])
    # print('Total Nuber of Hosts:   ', host_range['total_hosts'])

    ################ OUTPUT IP Address ################
    print('IP: ', end='')
    for i, num in enumerate(ip['decimal']):
        if i==3:
            print(int(num))
        else:  
            print(int(num),end='.')
    
    print('Net ID: ', end='')
    for i, num in enumerate(network_id_addr['decimal']):
        if i==3:
            print(int(num))
        else:  
            print(int(num),end='.')
    
    print('Broadcast IP: ', end='')
    for i, num in enumerate(broadcast_ip_addr['decimal']):
        if i==3:
            print(int(num))
        else:  
            print(int(num),end='.')
    
    print('Subnet Mask: ', end='')
    for i, num in enumerate(subnet_mask_ip_addr['decimal']):
        if i==3:
            print(int(num))
        else:  
            print(int(num),end='.')
    
    print('Host Range: ', end='')
    for i, num in enumerate(host_range['min']):
        if i==3:
            print(int(num), end=' - ')
        else:  
            print(int(num),end='.')
    
    for i, num in enumerate(host_range['max']):
        if i==3:
            print(int(num))
        else:  
            print(int(num),end='.')

    print('Allowed Hosts: ' + str(host_range['allowed_hosts']))
    print('Total Hosts: ' + str(host_range['total_hosts']))
    
