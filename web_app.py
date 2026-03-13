# web_app.py - Simple Flask interface
from flask import Flask, request, jsonify, render_template_string
from classifier import classify_intent
from router import route_and_respond
from logger import log_route
import json
import os
from datetime import datetime

app = Flask(__name__)

def get_recent_stats(limit=5):
    """Get recent statistics from log file"""
    stats = {
        "total_interactions": 0,
        "recent": [],
        "intent_counts": {}
    }
    
    try:
        if os.path.exists("route_log.jsonl"):
            with open("route_log.jsonl", "r") as f:
                lines = f.readlines()
                stats["total_interactions"] = len(lines)
                
                # Get last 5 interactions
                for line in lines[-5:]:
                    try:
                        data = json.loads(line)
                        stats["recent"].append(data)
                        
                        # Count intents
                        intent = data.get("intent", "unknown")
                        stats["intent_counts"][intent] = stats["intent_counts"].get(intent, 0) + 1
                    except:
                        pass
    except Exception as e:
        stats["error"] = str(e)
    
    return stats

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM Prompt Router</title>
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            margin-top: 0;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        .message { 
            margin: 15px 0; 
            padding: 15px; 
            border-radius: 8px; 
        }
        .user { 
            background: #e3f2fd; 
            border-left: 4px solid #007bff;
        }
        .response { 
            background: #f5f5f5; 
            border-left: 4px solid #28a745;
        }
        .intent { 
            color: #666; 
            font-size: 0.9em; 
            margin-top: 8px;
            font-style: italic;
        }
        textarea { 
            width: 100%; 
            height: 100px; 
            margin: 10px 0; 
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 14px;
            resize: vertical;
        }
        textarea:focus {
            outline: none;
            border-color: #007bff;
        }
        button { 
            padding: 12px 30px; 
            background: #007bff; 
            color: white; 
            border: none; 
            border-radius: 6px;
            cursor: pointer; 
            font-size: 16px;
            transition: background 0.3s;
        }
        button:hover {
            background: #0056b3;
        }
        .stats { 
            margin-top: 30px; 
            padding: 20px; 
            background: #f8f9fa; 
            border-radius: 8px;
            border: 1px solid #dee2e6;
        }
        .stats h3 {
            margin-top: 0;
            color: #495057;
        }
        pre {
            background: white;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
            font-size: 12px;
        }
        .suggestions {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin: 15px 0;
        }
        .suggestion {
            background: #e9ecef;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .suggestion:hover {
            background: #007bff;
            color: white;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }
        .welcome {
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            margin: 20px 0;
        }
        /* Confidence colors - defined as separate classes */
        .confidence-high {
            font-weight: bold;
            color: #28a745;
        }
        .confidence-medium {
            font-weight: bold;
            color: #ffc107;
        }
        .confidence-low {
            font-weight: bold;
            color: #dc3545;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 LLM Prompt Router</h1>
        <p>Ask me about coding, data analysis, writing, or career advice!</p>
        
        <div class="suggestions">
            <span class="suggestion" onclick="document.querySelector('textarea').value='How do I reverse a string in Python?'">💻 Python</span>
            <span class="suggestion" onclick="document.querySelector('textarea').value='What is the average of 10, 20, 30, 40?'">📊 Data</span>
            <span class="suggestion" onclick="document.querySelector('textarea').value='Fix my grammar: me and him went to store'">✍️ Writing</span>
            <span class="suggestion" onclick="document.querySelector('textarea').value='How to prepare for a tech interview?'">💼 Career</span>
        </div>
        
        <form method="POST">
            <textarea name="message" placeholder="Type your message here..." required>{% if user_message %}{{ user_message }}{% endif %}</textarea>
            <button type="submit">Send Message</button>
        </form>
        
        {% if error %}
        <div class="error">
            <strong>Error:</strong> {{ error }}
        </div>
        {% endif %}
        
        {% if response %}
        <div class="message user">
            <strong>You:</strong> {{ user_message }}
        </div>
        <div class="message response">
            <strong>Assistant:</strong> {{ response|safe }}
            <div class="intent">
                Intent: <strong>{{ intent }}</strong> | 
                Confidence: 
                <span class="{% if confidence > 0.7 %}confidence-high{% elif confidence > 0.4 %}confidence-medium{% else %}confidence-low{% endif %}">
                    {{ "%.1f"|format(confidence * 100) }}%
                </span>
            </div>
        </div>
        {% else %}
        <div class="welcome">
            <p>👋 Welcome! Type a message above to get started.</p>
            <p>Try clicking one of the suggestion chips!</p>
        </div>
        {% endif %}
        
        <div class="stats">
            <h3>📊 Statistics</h3>
            <p><strong>Total Interactions:</strong> {{ stats.total_interactions }}</p>
            
            {% if stats.intent_counts %}
            <p><strong>Intent Breakdown:</strong></p>
            <ul>
                {% for intent, count in stats.intent_counts.items() %}
                <li>{{ intent }}: {{ count }}</li>
                {% endfor %}
            </ul>
            {% endif %}
            
            {% if stats.recent %}
            <p><strong>Recent Interactions:</strong></p>
            <div style="max-height: 200px; overflow-y: auto;">
                <pre>{{ stats|tojson(indent=2) }}</pre>
            </div>
            {% endif %}
        </div>
    </div>
    
    <script>
        // Auto-submit with Enter (but allow Shift+Enter for new lines)
        document.querySelector('textarea').addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.form.submit();
            }
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize context with default values
    context = {
        'stats': get_recent_stats(),
        'user_message': '',
        'response': None,
        'intent': None,
        'confidence': 0.0,  # Always provide a default value
        'error': None
    }
    
    if request.method == 'POST':
        try:
            message = request.form.get('message', '').strip()
            context['user_message'] = message  # Store for form repopulation
            
            if not message:
                context['error'] = "Please enter a message"
                return render_template_string(HTML_TEMPLATE, **context)
            
            # Classify intent
            intent_data = classify_intent(message)
            
            # Get response
            response = route_and_respond(message, intent_data)
            
            # Log the interaction
            log_route(
                intent_data['intent'], 
                intent_data['confidence'], 
                message, 
                response
            )
            
            # Update context with response
            context.update({
                'response': response.replace('\n', '<br>'),
                'intent': intent_data['intent'],
                'confidence': intent_data['confidence'],
                'stats': get_recent_stats()  # Refresh stats
            })
            
        except Exception as e:
            context['error'] = str(e)
    
    return render_template_string(HTML_TEMPLATE, **context)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """JSON API endpoint for programmatic access"""
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        intent_data = classify_intent(message)
        response = route_and_respond(message, intent_data)
        
        log_route(
            intent_data['intent'], 
            intent_data['confidence'], 
            message, 
            response
        )
        
        return jsonify({
            'success': True,
            'intent': intent_data['intent'],
            'confidence': intent_data['confidence'],
            'response': response
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def api_stats():
    """JSON endpoint for statistics"""
    return jsonify(get_recent_stats())

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'LLM Router'})

if __name__ == '__main__':
    print("🚀 Starting LLM Router Web Interface...")
    print("📍 Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)