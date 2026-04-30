
R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.10",
    "username": "admin",
    "password": "admin123",
    "secret": "admin123",
}

R2 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.20",
    "username": "admin",
    "password": "admin123",
    "secret": "admin123",
}

R3 = {
    "host": "192.168.122.30",
    "username": "admin",
    "password": "admin123",
}

R2_CONFIG = [
    "ip route 200.1.13.0 255.255.255.252 200.1.12.1",
    "ip route 192.168.10.0 255.255.255.0 200.1.12.1",
    "ip route 192.168.30.0 255.255.255.0 200.1.23.2",
]

R1_CONFIG = [
    "ip route 200.1.23.0 255.255.255.252 200.1.12.2",
    "ip route 192.168.30.0 255.255.255.0 200.1.13.2",
    "crypto isakmp policy 10",
    "encr aes",
    "hash sha",
    "authentication pre-share",
    "group 14",
    "lifetime 86400",
    "exit",
    "crypto isakmp key cisco123 address 200.1.13.2",
    "crypto ipsec transform-set TS-R1-R3 esp-aes 128 esp-sha-hmac",
    "mode tunnel",
    "exit",
    "ip access-list extended ACL-VPN-R1-R3",
    "permit ip 192.168.10.0 0.0.0.255 192.168.30.0 0.0.0.255",
    "exit",
    "crypto map CMAP-R1-R3 10 ipsec-isakmp",
    "set peer 200.1.13.2",
    "set transform-set TS-R1-R3",
    "match address ACL-VPN-R1-R3",
    "exit",
    "interface GigabitEthernet0/2",
    "crypto map CMAP-R1-R3",
    "exit",
]
