import json
from datetime import datetime

def log_route(intent, confidence, message, response):
    """Log routing decisions to file"""
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "intent": intent,
        "confidence": confidence,
        "user_message": message,
        "final_response": response[:200] + "..." if len(response) > 200 else response
    }
    
    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log_data) + "\n")

def get_recent_stats(limit=10):
    """Get recent statistics from log file"""
    import os
    
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
                
                # Get last N interactions
                for line in lines[-limit:]:
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