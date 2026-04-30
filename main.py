import subprocess
from automate_r2 import configure_r2
from automate_r1 import configure_r1
from automate_r3 import configure_r3


def ping_host(ip):
    result = subprocess.run(
        ["ping", "-c", "2", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


def main():
    targets = ["192.168.122.10", "192.168.122.20", "192.168.122.30"]

    for ip in targets:
        if not ping_host(ip):
            print(f"ALERTA: no hay conectividad con {ip}")
            return

    ok_r2, out_r2, routes_r2 = configure_r2()
    print(out_r2)
    if not ok_r2:
        return
    print(routes_r2)

    ok_r1, out_r1, crypto_r1 = configure_r1()
    print(out_r1)
    if not ok_r1:
        return
    print(crypto_r1)

    ok_r3, out_r3 = configure_r3()
    print(out_r3)
    if not ok_r3:
        return

    print("Proceso de automatización completado.")


if __name__ == "__main__":
    main()
