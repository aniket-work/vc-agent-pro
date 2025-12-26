from ..core.a2a import AgentMessage, AgentState
from ..core.mcp_client import MCPClient
from typing import Dict, Any

class MarketAnalystAgent:
    def __init__(self):
        self.name = "MarketAnalyst"
        self.mcp = MCPClient(self.name)

    def process(self, message: AgentMessage, state: AgentState) -> Dict[str, Any]:
        sector = message.payload.get("sector", "Tech")
        state.add_log(f"{self.name} analyzing market for sector: {sector}")
        
        # Use MCP to get competitor data
        data = self.mcp.call_tool("competitor_lookup", {"sector": sector})
        
        market_view = "Market is consolidated."
        if "competitors" in data:
            top_comp = data['competitors'][0]['name']
            market_view = f"Highly competitive sector dominated by {top_comp}."
            
        return {"market_sentiment": market_view, "competitors": data.get("competitors", [])}
