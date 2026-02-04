import streamlit as st
from dotenv import load_dotenv
import os
import sys

# Add the parent directory to sys.path to allow importing ai_ops_assistant modules
# This is necessary because app.py is inside ai_ops_assistant/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_ops_assistant.main import AIOpsAssistant

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Operations Assistant", page_icon="🤖")

st.title("🤖 AI Operations Assistant")
st.markdown("Enter a task below, and the multi-agent system will plan, execute, and verify it for you.")

# Sidebar for API Keys (optional, good for demo)
with st.sidebar:
    st.header("Configuration")
    if not os.environ.get("OPENAI_API_KEY"):
        st.warning("⚠️ OPENAI_API_KEY not found in environment.")
    else:
        st.success("✅ OPENAI_API_KEY loaded")
    
    if not os.environ.get("GITHUB_TOKEN"):
        st.warning("⚠️ GITHUB_TOKEN not found.")
    else:
        st.success("✅ GITHUB_TOKEN loaded")
        
    if not os.environ.get("OPENWEATHER_API_KEY"):
        st.warning("⚠️ OPENWEATHER_API_KEY not found.")
    else:
         st.success("✅ OPENWEATHER_API_KEY loaded")

user_query = st.text_area("What would you like me to do?", height=100, placeholder="Example: Find a popular python weather library on GitHub and check the weather in San Francisco.")

if st.button("Run Task", type="primary"):
    if not user_query:
        st.error("Please enter a task.")
    else:
        try:
            with st.spinner("Initializing Agents..."):
                assistant = AIOpsAssistant()
            
            with st.status("Processing Task...", expanded=True) as status:
                st.write("🧠 Planner Agent creating a plan...")
                # We can't easily stream the internal steps without callbacks, 
                # so we'll run the whole thing and then display.
                # In a more advanced version, we'd add callbacks to update the UI in real-time.
                
                result = assistant.run(user_query)
                st.write("✅ Plan created and executed.")
                st.write("🕵️ Verifier Agent generating final details...")
                status.update(label="Task Completed!", state="complete", expanded=False)
            
            # Display Results
            st.divider()
            st.subheader("Final Answer")
            st.markdown(result["final_response"])
            
            with st.expander("View Execution Details"):
                st.subheader("1. Plan")
                st.json(result["plan"])
                
                st.subheader("2. Execution Results")
                st.json(result["execution_results"])
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
