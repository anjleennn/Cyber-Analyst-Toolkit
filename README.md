# Cyber-Analyst-Toolkit
SOC Analyst Toolkit for Phishing URL Heuristics and Brute Force Log Analysis.
# 🛡️ SOC Analyst Intelligence Toolkit
**Anjleen Kaur | M.Eng Information System Security, Concordia University**

## 📌 Project Overview
In a modern Security Operations Center (SOC), speed and accuracy are critical. This toolkit is a specialized dashboard designed to assist analysts in the **Triage and Investigation** phases of incident response. 

It automates the detection of two high-frequency threats:
1. **Phishing Infiltration**: Using heuristic analysis to evaluate suspicious links.
2. **Identity Attacks**: Analyzing server logs to identify Brute Force patterns.

---

## 🛠️ Modules & Security Logic

### 1. 🔍 Phishing URL Scanner
Instead of simple blacklisting, this module uses **Heuristic Analysis** to assign a risk score based on architectural red flags:
* **Protocol Analysis**: Flags unencrypted `http` traffic as a primary risk.
* **IP-based Masking**: Detects URLs using raw IP addresses (Common in C2/Command-and-Control servers).
* **Social Engineering Keywords**: Scans for "urgency" strings like `login`, `bank`, and `verify`.



### 2. 📊 SIEM Log Investigator
This module functions as a lightweight **SIEM (Security Information and Event Management)** tool. It automates the "Log Hunting" process by:
* **Filtering Traffic**: Isolating `Failed` authentication events.
* **Correlating Events**: Grouping logs by Source IP.
* **Incident Alerting**: Triggering a high-priority alert when an IP exceeds a set threshold (e.g., >5 failures), indicating a scripted **Brute Force Attack**.



---

## 💻 Tech Stack
* **Language:** Python 3.11
* **Libraries:** Pandas (Data Analysis), Streamlit (UI/Deployment), Regex (Pattern Matching)
* **Environment:** Virtual Environments (venv) for dependency isolation.

---

## 🚦 Getting Started
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/anjleennn/Cyber-Analyst-Toolkit.git](https://github.com/anjleennn/Cyber-Analyst-Toolkit.git)
