from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from config import R1, R1_CONFIG


def configure_r1():
    try:
        conn = ConnectHandler(**R1)
        conn.enable()
        output = conn.send_config_set(R1_CONFIG)
        crypto = conn.send_command("show crypto isakmp sa")
        conn.save_config()
        conn.disconnect()
        return True, output, crypto
    except NetmikoTimeoutException:
        return False, "ALERTA: R1 no responde por red.", ""
    except NetmikoAuthenticationException:
        return False, "ALERTA: Credenciales incorrectas en R1.", ""
    except Exception as exc:
        return False, f"ALERTA: Error inesperado en R1: {exc}", ""


if __name__ == "__main__":
    ok, output, crypto = configure_r1()
    print(output)
    print(crypto)
