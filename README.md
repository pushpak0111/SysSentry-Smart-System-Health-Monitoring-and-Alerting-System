🖥️ SysSentry — Real-Time System Monitoring & Alerting Dashboard

SysSentry is a real-time system monitoring tool built with Python, Streamlit, and Supabase.
It continuously tracks CPU, Memory, and Disk usage, visualizes trends with sliding graphs, and generates automated alerts with smart diagnostic suggestions.

This project demonstrates skills in:

Live data streaming

Backend–frontend integration

Performance monitoring

Real-time dashboards

Cloud database (Supabase)

Plotly visualizations

Python systems programming

**🚀 Features
✅ Real-Time Monitoring**

Tracks system CPU, Memory, and Disk usage

Displays live-updating charts with a sliding time window

Automatically fetches new data without manual refresh

🧠 Intelligent Alerts

Detects threshold breaches (high CPU/memory/disk)

Logs alerts with timestamps into Supabase

Provides diagnostic suggestions for each alert

**📊 Modern Dashboard
**
Built with Streamlit

Clean UI with dark mode Plotly charts

Real-time KPIs, graphs, and alert logs

**☁️ Cloud Synced Backend**

Supabase stores metrics & alerts

Dashboard fetches and updates continuously

Scalable backend architecture

🧩 Project Structure
SysSentry/
│
├── monitor.py              # Collects system metrics and sends to Supabase
├── alerts.py               # Checks thresholds and generates alerts
├── diagnostics.py          # Maps alerts to recommended fixes
├── dashboard.py            # Streamlit dashboard (real-time UI)
├── database.py             # Supabase connection client
├── requirements.txt        # Dependencies
├── .env.example            # Template for environment variables
└── README.md               # Project documentation

🛠️ Tech Stack
Layer	Tools
Frontend	Streamlit, Plotly
Backend	Python, Supabase Realtime & PostgreSQL
System Data	psutil
Languages	Python
Cloud	Supabase
Environment	dotenv
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/pushpakkore0111/SysSentry.git
cd SysSentry

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure Supabase

Create a .env file:

SUPABASE_URL=your_supabase_project_url

SUPABASE_SERVICE_ROLE=your_service_role_key

SUPABASE_ANON_KEY=your_public_anon_key

⚠️ Never upload your actual .env to GitHub.

5️⃣ Start the monitoring service

Runs in background and streams system data to Supabase.

python monitor.py

6️⃣ Launch the dashboard
streamlit run dashboard.py

📸 Dashboard Preview

<img width="1905" height="909" alt="image" src="https://github.com/user-attachments/assets/1d225438-60c2-4895-aa62-21c14055dbc0" />


🧠 How It Works (Architecture Overview)

monitor.py

Uses psutil to collect live CPU, memory, and disk stats

Sends each metric to Supabase every 1–2 seconds

alerts.py

Checks new metrics

Generates alerts (e.g., “High CPU Usage”)

Pushes alerts to Supabase

diagnostics.py

Suggests fixes for alerts

Integrated into Streamlit UI

dashboard.py

Reads live metrics & alerts from Supabase

Shows sliding line charts

Updates automatically

Displays smart alert suggestions

🧠 Future Enhancements

✔ Smooth real-time animations (Plotly extendTraces)

✔ WebSocket live updates via Supabase Realtime

✔ Mobile-responsive UI

✔ Automated email/Discord notifications

✔ Docker deployment
