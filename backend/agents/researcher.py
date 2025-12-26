from ..core.a2a import AgentMessage, AgentState
from ..core.mcp_client import MCPClient
from typing import Dict, Any

class ResearcherAgent:
    def __init__(self):
        self.name = "Researcher"
        self.mcp = MCPClient(self.name)

    def process(self, message: AgentMessage, state: AgentState) -> Dict[str, Any]:
        target = message.payload.get("target")
        state.add_log(f"{self.name} received request to research: {target}")
        
        # Use MCP to get data
        search_data = self.mcp.call_tool("web_search", {"query": target})
        
        analysis = f"Based on search results, {target} is a high-growth startup."
        if "results" in search_data:
            analysis += f" Key findings: {search_data['results'][0]['snippet']}"
            
        return {"technical_analysis": analysis, "raw_data": search_data}
