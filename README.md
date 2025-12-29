# Autonomous AI Decision & Reasoning Platform

## Overview
This project showcases how Large Language Models (LLMs) can be used safely
in real-world decision-making systems. Instead of blindly trusting AI outputs,
the platform combines AI reasoning with deterministic business rules and
confidence-based safety checks.

## Problem Statement
Customer complaints and operational incidents are often handled manually,
resulting in slow response times and inconsistent decisions. This platform
automates decision-making while maintaining transparency, auditability, and
human oversight.

## System Flow
Webhook → n8n → FastAPI → OpenAI → Decision Engine → Action → MLflow Audit

## Key Features
- AI-assisted reasoning using OpenAI with structured JSON outputs
- Rule-based decision engine to enforce business logic
- Confidence threshold gating for safe automation
- Automatic execution or human escalation
- Complete audit trail using MLflow

## Tech Stack
- Python (FastAPI)
- OpenAI API
- n8n (workflow orchestration)
- MLflow (decision logging and auditing)

## Use Case
Can be applied to customer support automation, refund processing,
incident triaging, or compliance-sensitive workflows.

## 👨‍💻 **AUTHOR**

**Rupansh Kumar**
M.Tech CSE — AI Platform and Workflow Automation Engineer 
Focused on building **production‑safe, governable AI systems**
 
