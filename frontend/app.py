import streamlit as st
import requests
import time
import json

# Configuration
API_URL = "http://localhost:8000/analyze"
st.set_page_config(page_title="VC-Agent Pro", page_icon="🚀", layout="wide")

# Custom CSS for "The Void" Aesthetic
st.markdown("""
<style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stButton>button {
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 6px;
    }
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🤖 Agent Control")
st.sidebar.markdown("---")
st.sidebar.success("System Status: ONLINE")
st.sidebar.info("Orchestrator: READY")
st.sidebar.info("MCP Clients: CONNECTED")

# Main Interface
st.title("VC-Agent Pro: Autonomous Due Diligence")
st.markdown("### 🔍 Enter Startup URL for Deep Analysis")

url = st.text_input("Startup URL", "https://stripe.com")

if st.button("🚀 Start Analysis Agent Swarm"):
    with st.spinner("Initializing Agent Protocol (A2A)..."):
        try:
            # Simulate real-time event streaming visualization
            status_placeholder = st.empty()
            
            steps = [
                "📡 Orchestrator: Delegating tasks...",
                "🕵️ Researcher: Querying MCP (Brave Search)...",
                "📊 Analyst: Querying MCP (Competitor DB)...",
                "🧠 Orchestrator: Synthesizing Investment Memo..."
            ]
            
            for step in steps:
                status_placeholder.markdown(f"### {step}")
                time.sleep(1.5) # UX delay
            
            # Actual API Call
            response = requests.post(API_URL, json={"startup_url": url})
            
            if response.status_code == 200:
                data = response.json()
                
                status_placeholder.markdown("### ✅ Analysis Complete")
                
                # Tech Analysis
                st.markdown("---")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.subheader("🛠 Technical Analysis")
                    st.json(data['artifacts']['tech_analysis'])
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.subheader("📈 Market Analysis")
                    st.json(data['artifacts']['market_analysis'])
                    st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown("---")
                st.subheader("📝 Audit Logs")
                st.code("\n".join(data['logs']))
                
            else:
                st.error("Failed to connect to Agent API")
                
        except Exception as e:
            st.error(f"Error: {e}. Is the backend running?")
            st.info("Run: `uvicorn backend.main:app --reload`")

st.markdown("---")
st.caption("Powered by Agno (Simulated), MCP, and A2A Protocol")
