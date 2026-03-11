import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="SOC Analyst Toolkit", layout="wide")

st.title("🛡️ Cybersecurity Analyst Dashboard")
st.markdown("🔍 *Project by Anjleen Kaur - Information System Security*")

# Create the Tabs to separate the two tools
tab1, tab2 = st.tabs(["🔗 Phishing Link Scanner", "📊 SIEM Log Investigator"])

# --- OPTION 1: PHISHING SCANNER ---
with tab1:
    st.header("URL Threat Intelligence")
    url_input = st.text_input("Paste a suspicious URL to analyze:")
    
    if url_input:
        score = 0
        checks = []
        
        # Security Logic 1: Missing HTTPS
        if not url_input.startswith("https"):
            score += 40
            checks.append("❌ Connection is NOT encrypted (No HTTPS)")
        
        # Security Logic 2: IP-based URL
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url_input):
            score += 50
            checks.append("🚨 Critical: URL uses an IP address instead of a domain name (Highly Suspicious)")

        # Security Logic 3: Suspicious Keywords
        keywords = ['login', 'bank', 'secure', 'verify', 'update-account']
        if any(k in url_input.lower() for k in keywords):
            score += 20
            checks.append("⚠️ Contains phishing keywords")

        # Display Result
        st.subheader(f"Risk Level: {'HIGH' if score > 50 else 'MEDIUM' if score > 0 else 'LOW'}")
        st.progress(min(score, 100))
        for c in checks:
            st.write(c)

# --- OPTION 3: LOG INVESTIGATOR ---
with tab2:
    st.header("Security Event Investigator")
    st.info("Upload server logs to identify Brute Force attacks.")
    
    uploaded_logs = st.file_uploader("Upload CSV Logs", type="csv")
    
    if uploaded_logs:
        log_df = pd.read_csv(uploaded_logs)
        st.dataframe(log_df.head())
        
        # Check for 'status' and 'ip' columns
        if 'ip' in log_df.columns and 'status' in log_df.columns:
            failed = log_df[log_df['status'] == 'Failed']
            # Count failures per IP
            attack_counts = failed['ip'].value_counts()
            
            # Flag IPs with more than 5 failed attempts
            threats = attack_counts[attack_counts > 5]
            
            if not threats.empty:
                st.error(f"🚨 ALERT: {len(threats)} Potential Brute Force Attackers Detected!")
                st.table(threats)
            else:
                st.success("✅ Log Integrity Verified: No brute force patterns found.")