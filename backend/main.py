from fastapi import FastAPI
from pydantic import BaseModel
from .agents.orchestrator import Orchestrator

app = FastAPI(title="VC-Agent Pro API")

class AnalysisRequest(BaseModel):
    startup_url: str

@app.post("/analyze")
async def analyze_startup(request: AnalysisRequest):
    # Simply parse name from URL for demo
    name = request.startup_url.replace("https://", "").replace("www.", "").split(".")[0]
    
    orchestrator = Orchestrator()
    final_state = orchestrator.run_analysis(name)
    
    return final_state.dict()

@app.get("/health")
def health():
    return {"status": "ok", "system": "functioning"}
