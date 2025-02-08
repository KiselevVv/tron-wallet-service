import logging

from tronpy import Tron
from tronpy.exceptions import AddressNotFound, BadAddress


# client = Tron()  основная сеть
client = Tron(network="nile")  # тестовая сеть

logging.basicConfig(level=logging.INFO)


def get_account_energy(address: str):
    try:
        resources = client.get_account_resource(address)

        total_energy_used = resources.get("TotalEnergyWeight", None)
        total_energy_limit = resources.get("TotalEnergyLimit", None)

        if total_energy_used is None or total_energy_limit is None:
            raise ValueError("Не удалось получить корректные данные об энергии")

        remaining_energy = total_energy_limit - total_energy_used

        return remaining_energy
    except ValueError as e:
        logging.error(
            f"Ошибка при вычислении энергии для адреса {address}")
        return {"error": str(e)}
    except Exception as e:
        logging.error(
            f"Произошла ошибка при получении энергии для адреса {address}: {e}")
        return {"error": "Произошла ошибка при получении энергии"}


def get_wallet_info(address: str):
    try:
        energy = get_account_energy(address)

        return {
            "address": address,
            "balance": client.get_account_balance(address),
            "bandwidth": client.get_bandwidth(address),
            "energy": energy
        }

    except (AddressNotFound, BadAddress):
        logging.error(f"Неверный адрес {address}")
        return {"error": "Неверный адрес"}
    except Exception as e:
        logging.error(f"Произошла ошибка при получении информации о "
                      f"кошельке для {address}: {e}")
        return {"error": "Произошла ошибка при получении информации о кошельке"}
