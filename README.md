#  **LLM-Powered Prompt Router - Clear Execution Steps**

## 📋 **Complete Step-by-Step Guide to Run This Project**

---

## **🔧 PREREQUISITES (What You Need)**

| Requirement | Check Command |
|-------------|---------------|
| **Python 3.9+** | `python --version` |
| **Git** | `git --version` |
| **Docker (optional)** | `docker --version` |
| **Groq API Key** | Get free at [console.groq.com](https://console.groq.com) |

---

## **📥 STEP 1: Download the Project**

```bash
# Clone the repository
git clone https://github.com/Kusubhavani/LLM-Powered-Prompt-Router.git

# Enter the project folder
cd LLM-Powered-Prompt-Router
```

---

## **🔑 STEP 2: Set Up Your API Key**

```bash
# Create .env file
echo "GROQ_API_KEY=your_actual_api_key_here" > .env

# Verify it was created
cat .env
# Should show: GROQ_API_KEY=your_key_here
```

**Don't have an API key?**
1. Go to https://console.groq.com
2. Sign up with Google/GitHub
3. Click "Create API Key"
4. Copy the key and paste above

---

## **🚀 STEP 3: Choose How to Run**

---

## **🔹 OPTION A: Run with Python (Simplest)**

### **A1: Install Dependencies**
```bash
pip install groq python-dotenv flask flask-cors
```

### **A2: Start the Web App**
```bash
python web_app.py
```
**Expected output:**
```
🚀 Starting LLM Router Web Interface...
📍 Open http://localhost:5000 in your browser
```

### **A3: Open in Browser**
```
http://localhost:5000
```

### **A4: Alternative - Run Terminal Version**
```bash
python main.py
```
Then type your questions directly in the terminal.

---

## **🔹 OPTION B: Run with Docker (Easiest)**

### **B1: Make sure Docker is running**
- Windows: Start "Docker Desktop"
- Mac: Start "Docker Desktop"
- Linux: `sudo systemctl start docker`

### **B2: One Command to Start Everything**
```bash
docker-compose up --build
```

**Wait for:**
```
✔ Container llm-prompt-web-1  Started
Web interface ready at http://localhost:5000
```

### **B3: Open Browser**
```
http://localhost:5000
```

### **B4: Stop Docker (when done)**
```bash
# Press Ctrl+C, then:
docker-compose down
```

---

## **🔹 OPTION C: Run with Python Virtual Environment (Cleanest)**

### **C1: Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **C2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **C3: Run the App**
```bash
python web_app.py
```

---

## **🧪 STEP 4: Test That It's Working**

### **Test 1: Health Check**
```bash
# Open new terminal, run:
curl http://localhost:5000/health
```
**Expected:** `{"status":"healthy","service":"LLM Router"}`

### **Test 2: API Test**
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Hello\"}"
```
**Expected:** JSON response with intent and reply

### **Test 3: Web Interface**
Open `http://localhost:5000` and try typing:
```
How do I reverse a string in Python?
```

---

## **🎯 STEP 5: Try These Examples**

Click the suggestion chips or type these:

| Category | Try This Question |
|----------|-------------------|
| 💻 **Code** | "Write a function to check if a number is prime" |
| 📊 **Data** | "What's the average of 10, 20, 30, 40, 50?" |
| ✍️ **Writing** | "Fix my grammar: me and him went to the store yesterday" |
| 💼 **Career** | "How do I prepare for a Python developer interview?" |
| ❓ **Unclear** | "What's the weather like today?" |

---

## **📊 STEP 6: View Statistics**

### **Via Web Interface**
- Scroll to bottom of the page
- See total interactions and intent breakdown

### **Via API**
```bash
curl http://localhost:5000/api/stats
```

### **Via Log File**
```bash
cat route_log.jsonl
```

---

## **🛑 STEP 7: Stop the Application**

### **If running with Python:**
```
Press Ctrl+C in the terminal where web_app.py is running
```

### **If running with Docker:**
```bash
# Stop containers
docker-compose down

# Remove everything (including logs)
docker-compose down -v
```

---

## **📋 QUICK REFERENCE - All Commands in One Place**

```bash
# 1. Clone
git clone https://github.com/yourusername/LLM-Powered-Prompt.git
cd LLM-Powered-Prompt

# 2. Setup API key
echo "GROQ_API_KEY=your_key_here" > .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run web app
python web_app.py

# 5. Open browser
# http://localhost:5000

# 6. Test API (in new terminal)
curl http://localhost:5000/health
```

---

## **🐳 DOCKER QUICK REFERENCE**

```bash
# Build and start
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down

# Rebuild after changes
docker-compose up --build
```

---

## **❓ TROUBLESHOOTING**

| Problem | Solution |
|---------|----------|
| **"No module named flask"** | Run `pip install flask flask-cors` |
| **"Address already in use"** | Port 5000 is busy - kill the process or change port in web_app.py |
| **"Connection refused"** | Make sure the app is running first! |
| **API key error** | Check `.env` file exists and has correct key |
| **Docker: permission denied** | Run Docker Desktop first |
| **No response from AI** | Check internet connection and API key validity |

---

## **✅ SUCCESS CHECKLIST**

- [ ] Cloned the repository
- [ ] Created `.env` file with valid API key
- [ ] Installed dependencies
- [ ] Ran `python web_app.py` or `docker-compose up`
- [ ] Opened `http://localhost:5000` in browser
- [ ] Typed a question and got response
- [ ] Saw intent and confidence displayed
- [ ] Checked statistics

---

## **📁 PROJECT FILES**

| File | Purpose | When to Use |
|------|---------|-------------|
| `web_app.py` | Web interface | Run for browser access |
| `main.py` | Terminal chat | Run for command-line |
| `classifier.py` | Detects intent | Auto-loaded |
| `router.py` | Gets responses | Auto-loaded |
| `prompts.py` | AI instructions | Edit to customize |
| `logger.py` | Saves history | Auto-run |
| `requirements.txt` | Dependencies | Install once |
| `Dockerfile` | Docker setup | For container |
| `docker-compose.yml` | Docker compose | For easy start |
| `.env` | Your API key | Create this! |

---

## **🎉 YOU'RE DONE!**

Your LLM-Powered Prompt Router is now running! 

- **Web Interface:** http://localhost:5000
- **Terminal Chat:** `python main.py`
- **API:** http://localhost:5000/api/chat


**Enjoy chatting with your AI router!** 🤖

