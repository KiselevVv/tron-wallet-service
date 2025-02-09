import logging

from fastapi import HTTPException
from tronpy import Tron
from tronpy.exceptions import AddressNotFound, BadAddress

logger = logging.getLogger(__name__)

# client = Tron()  основная сеть
client = Tron(network="nile")  # тестовая сеть


def get_account_energy(address: str):
    try:
        resources = client.get_account_resource(address)

        total_energy_used = resources.get("TotalEnergyWeight", None)
        total_energy_limit = resources.get("TotalEnergyLimit", None)

        if total_energy_used is None or total_energy_limit is None:
            raise ValueError(
                "Не удалось получить корректные данные об энергии")

        remaining_energy = total_energy_limit - total_energy_used
        return remaining_energy
    except Exception as e:
        logger.error(f"Ошибка при получении энергии для {address}: {e}")
        return None


def get_wallet_info(address: str):
    try:
        balance = client.get_account_balance(address)
        bandwidth = client.get_bandwidth(address)
        energy = get_account_energy(address)

        return {
            "address": address,
            "balance": balance,
            "bandwidth": bandwidth,
            "energy": energy
        }
    except (AddressNotFound, BadAddress):
        logger.error(f"Неверный адрес: {address}")
        raise HTTPException(status_code=400, detail="Неверный адрес")
    except Exception as e:
        logger.exception(f"Неожиданная ошибка: {e}")
        raise HTTPException(status_code=500, detail="Внутрення ошибка сервера")
