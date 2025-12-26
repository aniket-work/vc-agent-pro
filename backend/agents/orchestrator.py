from .researcher import ResearcherAgent
from .market import MarketAnalystAgent
from ..core.a2a import AgentMessage, AgentState
import uuid

class Orchestrator:
    def __init__(self):
        self.researcher = ResearcherAgent()
        self.market = MarketAnalystAgent()
        
    def run_analysis(self, startup_name: str) -> AgentState:
        # Initialize State
        state = AgentState(workflow_id=str(uuid.uuid4()))
        state.add_log(f"Orchestrator started analysis for {startup_name}")
        
        # Step 1: Research
        msg1 = AgentMessage(
            sender="Orchestrator", recipient="Researcher", 
            intent="research", payload={"target": startup_name}
        )
        tech_result = self.researcher.process(msg1, state)
        state.update_artifact("tech_analysis", tech_result)
        state.add_log("Tech analysis complete.")

        # Step 2: Market Analysis
        msg2 = AgentMessage(
            sender="Orchestrator", recipient="MarketAnalyst",
            intent="analyze_market", payload={"sector": "SaaS"} # Inferred
        )
        market_result = self.market.process(msg2, state)
        state.update_artifact("market_analysis", market_result)
        state.add_log("Market analysis complete.")
        
        # Step 3: Synthesis
        state.status = "completed"
        state.add_log("Final Investment Memo generated.")
        
        return state
