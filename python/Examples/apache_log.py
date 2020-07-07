def apache_log(logs1):

    #print(logs1, "logs1")
    iplist = {}
    for line in logs1:
        #print(line,"line")
        #print("st",st)
        ip =  line.split()[0]
        print(ip, "ip")
        if ip in iplist :
            iplist[ip]  += 1
        else:
            iplist[ip] = 1
    ip_count = iplist.values()
    ips = iplist.keys()
    print(iplist.values())
    print(iplist.keys())
    print(max(ip_count))
    print(ips.index(max(ip_count)))

    return ips[ip_count.index(max(ip_count))]

lines= ["10.10.10.10 - testing1 testing3 testing4 testing5",
                 "10.10.10.10 - TESTING",
                 "10.10.10.9 ---- LAST ONE"]
print(apache_log(lines))

