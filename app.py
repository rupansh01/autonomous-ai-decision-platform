#fastAPI
from mlflow_logger import log_ai_decision
from openai_agent import analyze_complaint
from fastapi import FastAPI
from pydantic import BaseModel
from decision import final_decision

app = FastAPI(title="Autonomous AI Decision Platform")

class ComplaintRequest(BaseModel):
    complaint_text: str
    customer_type: str
    past_complaints: int
    severity: int

@app.post("/decide")
def decide(req: ComplaintRequest):

    ai_analysis = analyze_complaint(req.complaint_text)

    final = final_decision(
        severity=ai_analysis["severity"],
        customer_type=req.customer_type,
        past_complaints=req.past_complaints
    )

    confidence = round(ai_analysis["severity"] / 10, 2)

    action_taken = "AUTO_EXECUTE" if confidence >= 0.8 else "ESCALATE_TO_HUMAN"

    # 🔥 MLflow log
    log_ai_decision(
        decision=final,
        confidence=confidence,
        action_taken=action_taken,
        reasoning=ai_analysis["reasoning"]
    )

    return {
        "decision": final,
        "confidence": confidence,
        "action_taken": action_taken,
        "reason": ai_analysis["reasoning"]
    }
