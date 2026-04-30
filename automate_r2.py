from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from config import R2, R2_CONFIG


def configure_r2():
    try:
        conn = ConnectHandler(**R2)
        conn.enable()
        output = conn.send_config_set(R2_CONFIG)
        routes = conn.send_command("show ip route static")
        conn.save_config()
        conn.disconnect()
        return True, output, routes
    except NetmikoTimeoutException:
        return False, "ALERTA: R2 no responde por red.", ""
    except NetmikoAuthenticationException:
        return False, "ALERTA: Credenciales incorrectas en R2.", ""
    except Exception as exc:
        return False, f"ALERTA: Error inesperado en R2: {exc}", ""


if __name__ == "__main__":
    ok, output, routes = configure_r2()
    print(output)
    print(routes)
