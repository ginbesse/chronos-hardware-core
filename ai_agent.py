import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [CHRONOS-AI] - %(levelname)s - %(message)s")

class ChronosAIEngine:
    def __init__(self):
        self.entropy_threshold = 85.0
        self.temp_threshold = 310.0

    def evaluate_safety(self, metrics: dict) -> dict:
        entropy = metrics.get("entropy_level_pct", 50.0)
        temp = metrics.get("containment_temp_k", 300.0)
        
        risk_score = (entropy * 0.6) + ((temp - 290) * 1.5)
        status = "STABLE"
        action = "NONE"

        if risk_score > self.entropy_threshold:
            status = "CRITICAL_ANOMALY"
            action = "INITIATE_MAGNETIC_SHIELD_COMPENSATION"
            logging.warning(f"Anomali tespit edildi! Risk Skoru: {risk_score}")

        return {
            "ai_status": status,
            "risk_score": round(risk_score, 2),
            "recommended_action": action,
            "confidence": 0.99
        }
