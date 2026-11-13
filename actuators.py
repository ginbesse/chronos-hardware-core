import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [CHRONOS-ACTUATORS] - %(levelname)s - %(message)s")

class ChronosActuators:
    def __init__(self):
        self.magnetic_shield_active = True
        self.power_regulator_level = 50.0 # yüzde

    def adjust_magnetic_shield(self, intensity: float):
        self.magnetic_shield_active = intensity > 0
        logging.info(f"Manyetik kalkan yoğunluğu ayarlandı: {intensity}%")
        return True

    def emergency_shutdown(self):
        logging.critical("ACİL DURUM: Tüm alan jeneratörleri kapatılıyor!")
        self.power_regulator_level = 0.0
        self.magnetic_shield_active = False
        return {"status": "SHUTDOWN_SUCCESS", "timestamp": time.time()}
