import random
import time
import logging
from typing import Dict, Any

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - [CHRONOS-TELEMETRY] - %(levelname)s - %(message)s"
)

class ChronosTelemetryUnit:
    def __init__(self, port: str = "COM3", baudrate: int = 115200):
        self.port = port
        self.baudrate = baudrate
        self.is_connected = False
        self.calibration_factor = 1.024

    def initialize_hardware_interface(self) -> bool:
        logging.info(f"Donanım arayüzü başlatılıyor. Port: {self.port}, Baudrate: {self.baudrate}")
        time.sleep(0.5) 
        self.is_connected = True
        logging.info("Donanım bağlantısı başarılı. Sensörler senkronize edildi.")
        return self.is_connected

    def read_quantum_oscillators(self) -> float:
        if not self.is_connected:
            raise ConnectionError("Kritik Hata: Donanım bağlantısı kopuk!")
        return round(random.uniform(4.8e12, 5.4e12), 2)

    def read_gravitational_flux(self) -> float:
        raw_val = random.uniform(1.5, 4.2)
        return round(raw_val * self.calibration_factor, 4)

    def read_entropy_level(self) -> float:
        return round(random.uniform(30.0, 95.0), 2)

    def read_containment_temperature(self) -> float:
        return round(random.uniform(290.0, 315.5), 2)

    def fetch_all_telemetry(self) -> Dict[str, Any]:
        try:
            return {
                "timestamp": time.time(),
                "status_code": 200 if self.is_connected else 500,
                "metrics": {
                    "quantum_frequency_hz": self.read_quantum_oscillators(),
                    "flux_density_t": self.read_gravitational_flux(),
                    "entropy_level_pct": self.read_entropy_level(),
                    "containment_temp_k": self.read_containment_temperature()
                }
            }
        except Exception as e:
            logging.error(f"Telemetri hatası: {str(e)}")
            return {"timestamp": time.time(), "status_code": 500, "error": str(e)}
