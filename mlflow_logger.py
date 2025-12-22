import mlflow
import json
import os
from datetime import datetime

# -----------------------------------------
# MLflow Setup
# -----------------------------------------
EXPERIMENT_NAME = "AI_Decision_Audit"

mlflow.set_experiment(EXPERIMENT_NAME)

# -----------------------------------------
# Log one AI decision
# -----------------------------------------
def log_ai_decision(decision, confidence, action_taken, reasoning, source="AI_DECISION_PLATFORM"):

    with mlflow.start_run(run_name=f"decision_{datetime.now()}"):

        # Metrics
        mlflow.log_metric("confidence", confidence)

        # Params
        mlflow.log_param("decision", decision)
        mlflow.log_param("action_taken", action_taken)
        mlflow.log_param("source", source)

        # Save reasoning as artifact
        artifact_file = "reasoning.json"
        with open(artifact_file, "w") as f:
            json.dump(
                {
                    "decision": decision,
                    "confidence": confidence,
                    "action_taken": action_taken,
                    "reasoning": reasoning,
                },
                f,
                indent=2
            )

        mlflow.log_artifact(artifact_file)

        # Cleanup local file
        os.remove(artifact_file)
