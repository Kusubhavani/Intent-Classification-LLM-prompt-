# 🤖 **LLM-Powered Prompt Router - Complete Guide**

## 🎯 **About The Project**

**LLM-Powered Prompt Router** is an intelligent chatbot that automatically detects what you're asking about and routes your question to the right AI expert. Instead of using one generic AI for everything, it uses specialized prompts for different topics.

### **The Problem It Solves**
Most AI chatbots treat every question the same way. But asking about **code** is different from asking about **career advice**. This router understands the context and gives you better, more focused answers.

### **Intent Categories**

| Intent | What It Means | Example |
|--------|---------------|---------|
| 💻 **code** | Programming questions | "How to sort a list in Python?" |
| 📊 **data** | Data analysis questions | "What's the average of these numbers?" |
| ✍️ **writing** | Grammar and writing help | "Is this sentence correct?" |
| 💼 **career** | Job and career advice | "How to prepare for interviews?" |
| ❓ **unclear** | Can't determine intent | "Hello, how are you?" |

---

## 🔄 **How It Works**

```
Your Question → Intent Detected → Specialized Prompt → AI Response → Logged
     ↓                ↓                  ↓                  ↓            ↓
  "How to      →    code           →  "You are a      →  Python     →  Saved to
  reverse?"        (98% sure)         senior dev"       code        route_log.jsonl
```
---

## 📁 **Project Structure**

```
LLM-Powered-Prompt/
├── 📄 web_app.py          # Main Flask web app (run this for web)
├── 📄 main.py             # Terminal chat version (run this for CLI)
├── 📄 classifier.py       # Intent detection logic
├── 📄 router.py           # Routes to correct prompt
├── 📄 prompts.py          # Specialized AI prompts
├── 📄 logger.py           # Logging functionality
├── 📄 requirements.txt    # Python dependencies
├── 📄 .env.example        # Example environment file
├── 🐳 Dockerfile          # Docker configuration
├── 🐳 docker-compose.yml  # Docker Compose setup
├── 📄 route_log.jsonl     # Auto-generated log file
└── 📖 README.md           # This documentation
```
---

## ✨ **Key Features**

✅ **Smart Intent Detection** - Automatically categorizes your questions  
✅ **Specialized AI Experts** - Different prompts for different topics  
✅ **Confidence Scoring** - Shows how sure it is about your intent  
✅ **Multiple Interfaces** - PowerShell, Web, and Docker  
✅ **Logging & Analytics** - Tracks all conversations  
✅ **Clean Web UI** - Modern interface with suggestion chips  
✅ **REST API** - Programmatic access for developers  

---

## 📦 **Prerequisites**

| Requirement | Check Command |
|-------------|---------------|
| **Python 3.9+** | `python --version` |
| **Git** | `git --version` |
| **Docker (optional)** | `docker --version` |
| **Groq API Key** | Get free at [console.groq.com](https://console.groq.com) |

---

## 🚀 **Execution Steps**

### **Step 0: Get Your API Key (1 minute)**

```powershell
# 1. Go to https://console.groq.com
# 2. Sign up with Google/GitHub
# 3. Click "Create API Key"
# 4. Copy the key (looks like: gsk_xxxxxxxxx)
```

---

## 🔹 **POWERSHELL/TERMINAL METHOD**

### **Step 1: Download the Project**
```powershell
# Clone the repository
git clone https://github.com/Kusubhavani/Intent-Classification-LLM-prompt-.git

# Enter the project folder
cd Intent-Classification-LLM-prompt-

# Check files (you should see all .py files)
dir
```

### **Step 2: Set Up API Key**
```powershell
# Create .env file with your API key
echo "GROQ_API_KEY=your_key_here" > .env

# Verify it was created
cat .env
# Should show: GROQ_API_KEY=gsk_xxxxxxxxx
```

### **Step 3: Install Dependencies**
```powershell
# Install required Python packages
pip install groq python-dotenv flask flask-cors

# Verify installation
pip list | findstr "groq flask"
```

### **Step 4: Run the Application**

#### **Option A: Run Terminal Chat Version**
```powershell
# Start interactive chat in terminal
python main.py
```

**What you'll see:**
```
User: 
```
Type your question and press Enter. Example:
```
User: How do I reverse a string in Python?

Detected Intent: code
Confidence: 0.98

AI Response:
You can reverse a string using slicing: text[::-1]

Example:
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # Output: "olleh"
```

**To exit:** Press `Ctrl+C`

#### **Option B: Run Web Interface Version**
```powershell
# Start the Flask web server
python web_app.py
```

**Expected output:**
```
🚀 Starting LLM Router Web Interface...
📍 Open http://localhost:5000 in your browser
 * Serving Flask app 'web_app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

**Keep this terminal window open!**

### **Step 5: Open New Terminal for Testing**
```powershell
# Open a NEW PowerShell window
cd C:\Users\BHAVANI\OneDrive\Desktop\LLM-Powered-Prompt

# Test health endpoint
curl http://localhost:5000/health

# Test API
curl -X POST http://localhost:5000/api/chat `
  -H "Content-Type: application/json" `
  -d '{"message": "Hello"}'
```

### **Step 6: Stop the Server**
```powershell
# Go back to the first terminal and press:
Ctrl+C
```
🎯 5 Essential Questions to Test Your LLM Router
Try These 5 Questions - One for Each Intent!


1️⃣ CODE INTENT


How do I reverse a string in Python?
What to expect: Python code with slicing example

text
Expected: text[::-1] explanation with code blocks
2️⃣ DATA INTENT



What's the average of 10, 20, 30, 40, 50?
What to expect: Calculation and explanation

text
Expected: Average = 30 with step-by-step math
3️⃣ WRITING INTENT


Fix my grammar: me and him went to the store
What to expect: Grammar correction

text
Expected: "He and I went to the store" with explanation
4️⃣ CAREER INTENT


How to prepare for a Python developer interview?
What to expect: Career advice

text
Expected: Interview tips, topics to study, common questions
5️⃣ UNCLEAR INTENT


Hello, how are you?
What to expect: Asks for clarification

text
Expected: "I'm doing well! What would you like help with today? (coding, data, writing, or career)"
---

## 🔹 **WEB BROWSER METHOD**

### **Step 1: Start the Web Server**
```powershell
# Make sure you're in the project folder
cd C:\Users\BHAVANI\OneDrive\Desktop\LLM-Powered-Prompt

# Start the Flask app
python web_app.py
```

### **Step 2: Open Your Browser**
```
http://localhost:5000
```

### **Step 3: Use the Web Interface**

**What you'll see:**
```
┌─────────────────────────────────────┐
│  🤖 LLM Prompt Router               │
│  Ask me about coding, data, writing,│
│  or career advice!                   │
├─────────────────────────────────────┤
│  [💻 Python] [📊 Data] [✍️ Writing]  │
│  [💼 Career]                         │
├─────────────────────────────────────┤
│  ┌───────────────────────────────┐ │
│  │ Type your message here...     │ │
│  └───────────────────────────────┘ │
│  ┌─────────┐                        │
│  │  Send   │                        │
│  └─────────┘                        │
├─────────────────────────────────────┤
│  Welcome! Type a message to start.  │
├─────────────────────────────────────┤
│  📊 Statistics                      │
│  Total Interactions: 0              │
└─────────────────────────────────────┘
```

### **Step 4: Try These Examples**

Click the suggestion chips or type:

| Click This | Types This |
|------------|------------|
| 💻 **Python** | "How do I reverse a string in Python?" |
| 📊 **Data** | "What's the average of 10, 20, 30, 40?" |
| ✍️ **Writing** | "Fix my grammar: me and him went to store" |
| 💼 **Career** | "How to prepare for a tech interview?" |

### **Step 5: See the Response**
```
┌─────────────────────────────────────┐
│ You: How do I reverse a string?     │
├─────────────────────────────────────┤
│ Assistant:                          │
│ Use slicing: text[::-1]              │
│                                      │
│ Example:                             │
│ text = "hello"                       │
│ reversed = text[::-1]                │
│ print(reversed)  # "olleh"           │
│                                      │
│ Intent: code (98% confident)         │
└─────────────────────────────────────┘
```

### **Step 6: Check Statistics**
Scroll down to see:
- Total interactions
- Intent breakdown
- Recent conversations

---

## 🔹 **DOCKER METHOD**

### **Step 1: Ensure Docker is Running**
```powershell
# Check if Docker is installed
docker --version

# Check if Docker is running
docker ps

# If not running, start Docker Desktop from Start Menu
```

### **Step 2: Create Docker Files**

**Create `Dockerfile`:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "web_app.py"]
```

**Create `docker-compose.yml`:**
```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: llm-router-app
    ports:
      - "5000:5000"
    env_file:
      - .env
    volumes:
      - ./route_log.jsonl:/app/route_log.jsonl
    restart: unless-stopped
```

### **Step 3: Build and Run with Docker**
```powershell
# Build the Docker image
docker-compose build

# Run the container
docker-compose up
```

**Expected output:**
```
[+] Building 15.2s (10/10) FINISHED
...
✔ Container llm-router-app  Started
Web interface ready at http://localhost:5000
```

### **Step 4: Access the Application**
```
http://localhost:5000
```

### **Step 5: Docker Management Commands**

```powershell
# Run in background mode
docker-compose up -d

# View running containers
docker ps

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Rebuild after changes
docker-compose up --build

# Run terminal version in container
docker-compose run web python main.py

# Open bash shell in container
docker exec -it llm-router-app bash
```

### **Step 6: Stop Docker**
```powershell
# If running in foreground: Ctrl+C

# If running in background:
docker-compose down

# Remove everything (including volumes)
docker-compose down -v
```

---

## 🔍 **Testing & Verification**

### **Test 1: Health Check**
```powershell
curl http://localhost:5000/health
```
**Expected:** `{"status":"healthy","service":"LLM Router"}`

### **Test 2: API Test**
```powershell
curl -X POST http://localhost:5000/api/chat `
  -H "Content-Type: application/json" `
  -d '{"message": "Hello"}'
```
**Expected:** JSON with intent and response

### **Test 3: Stats API**
```powershell
curl http://localhost:5000/api/stats
```
**Expected:** JSON with interaction statistics

### **Test 4: Check Log File**
```powershell
cat route_log.jsonl
```
**Expected:** JSON lines of past conversations

---

## 📝 **Sample Questions to Try**

| Category | Question |
|----------|----------|
| 💻 **Code** | "Write a function to check if a number is prime" |
| 💻 **Code** | "How do I sort a dictionary by value in Python?" |
| 📊 **Data** | "What's the median of 5, 2, 8, 1, 9?" |
| 📊 **Data** | "Explain correlation vs causation" |
| ✍️ **Writing** | "Fix this: The boy he run fast to school" |
| ✍️ **Writing** | "How can I make this sentence clearer: 'The car which was red and fast went down the street'?" |
| 💼 **Career** | "What should I put in my resume for a Python job?" |
| 💼 **Career** | "How do I answer 'Tell me about yourself' in an interview?" |
| ❓ **Unclear** | "What's up?" |

---

## ❓ **Troubleshooting**

| Problem | Solution |
|---------|----------|
| **"No module named flask"** | Run `pip install flask flask-cors` |
| **"Address already in use"** | Port 5000 is busy - kill process or change port |
| **"Connection refused"** | Make sure the app is running first! |
| **API key error** | Check `.env` file exists and has valid key |
| **Docker: permission denied** | Start Docker Desktop first |
| **No response from AI** | Check internet connection and API key |
| **"python is not recognized"** | Install Python from python.org |
| **"git is not recognized"** | Install Git from git-scm.com |

### **Fix Port 5000 Already in Use**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual number)
taskkill /PID 1234 /F
```

---

## 📡 **API Reference**

### **Chat Endpoint**
```http
POST /api/chat
Content-Type: application/json

{
  "message": "Your question here"
}
```

**Response:**
```json
{
  "success": true,
  "intent": "code",
  "confidence": 0.98,
  "response": "AI response text here..."
}
```

### **Statistics Endpoint**
```http
GET /api/stats
```

**Response:**
```json
{
  "total_interactions": 42,
  "intent_counts": {
    "code": 20,
    "data": 10,
    "writing": 8,
    "career": 4
  },
  "recent": [...]
}
```

### **Health Check**
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "LLM Router"
}
```

---

## 🎯 **Quick Command Summary**

```powershell
# 1. Clone and enter
git clone https://github.com/yourusername/LLM-Powered-Prompt.git
cd LLM-Powered-Prompt

# 2. Add API key
echo "GROQ_API_KEY=your_key_here" > .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run web app
python web_app.py

# 5. Open browser
# http://localhost:5000

# 6. OR run terminal version
python main.py

# 7. OR run with Docker
docker-compose up --build
```

---

# Author:
KUSU BHAVANI
Artificial Intelligence and Machine Learning
bhavanikusu92@gmail.com

Built with ❤️ for developers everywhere

**Happy Routing!** 🤖✨



