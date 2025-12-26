from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid

class AgentMessage(BaseModel):
    """Standardized Agent-to-Agent Message Protocol"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    sender: str
    recipient: str
    intent: str  # e.g., "request_research", "provide_analysis", "ask_clarification"
    payload: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.now)

class AgentState(BaseModel):
    """Shared state for the agentic workflow"""
    workflow_id: str
    status: str = "idle"  # idle, working, completed, failed
    logs: List[str] = []
    artifacts: Dict[str, Any] = {}

    def add_log(self, message: str):
        self.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def update_artifact(self, key: str, value: Any):
        self.artifacts[key] = value
