from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json
from firmware.telemetry import ChronosTelemetryUnit
from firmware.actuators import ChronosActuators
from ai_core.ai_agent import ChronosAIEngine

app = FastAPI(title="Physical Chronos Control System (PCCS)", version="1.0.0")

telemetry_unit = ChronosTelemetryUnit()
actuators = ChronosActuators()
ai_engine = ChronosAIEngine()

@app.on_event("startup")
async def startup_event():
    telemetry_unit.initialize_hardware_interface()

@app.get("/")
def read_root():
    return {"system": "PCCS Core Online", "status": "Operational"}

@app.websocket("/ws/telemetry")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            packet = telemetry_unit.fetch_all_telemetry()
            metrics = packet.get("metrics", {})
            
            ai_analysis = ai_engine.evaluate_safety(metrics)
            
            payload = {
                "telemetry": packet,
                "ai_analysis": ai_analysis
            }
            
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        print("İstemci bağlantısı koptu.")
