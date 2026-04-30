import json
import requests
import urllib3
from config import R3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def configure_r3():
    url = f"https://{R3['host']}/rest/ip/ipsec/policy"
    payload = {
        "src-address": "192.168.30.0/24",
        "dst-address": "192.168.10.0/24",
        "sa-src-address": "200.1.13.2",
        "sa-dst-address": "200.1.13.1",
        "tunnel": "yes",
        "action": "encrypt",
        "proposal": "prop-r1",
        "peer": "peer-r1"
    }

    try:
        response = requests.put(
            url,
            auth=(R3["username"], R3["password"]),
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            verify=False,
            timeout=10,
        )
        data = response.json()
        return True, data
    except requests.exceptions.Timeout:
        return False, "ALERTA: Timeout al conectar con R3."
    except requests.exceptions.ConnectionError:
        return False, "ALERTA: R3 no responde por API REST."
    except Exception as exc:
        return False, f"ALERTA: Error inesperado en R3: {exc}"


if __name__ == "__main__":
    ok, output = configure_r3()
    print(output)

