# AI Support Engineer Copilot

A LangGraph and LangSmith workflow that automates support issue classification, routing, troubleshooting, escalation summary generation, and workflow evaluation.

## Project Overview

This project simulates an AI-powered support engineering assistant. Given a support issue, the workflow:

1. Classifies the issue into a support category
2. Routes the issue to the appropriate troubleshooting workflow
3. Generates recommended troubleshooting steps
4. Creates an escalation-ready summary
5. Evaluates workflow performance using LangSmith

## Features

* Issue classification using GPT-4o-mini
* Conditional routing with LangGraph
* Specialized troubleshooting workflows
* Escalation summary generation
* LangSmith tracing and observability
* Dataset-driven evaluation
* Deterministic category accuracy scoring
* LLM-as-Judge summary quality evaluation

## Supported Categories

* Authentication
* SSL
* Kubernetes
* Connectivity
* Performance

## Architecture

Support Issue

→ Classification

→ Conditional Routing

→ Authentication | SSL | Kubernetes | Connectivity | Performance

→ Troubleshooting

→ Escalation Summary

## Evaluation Results

Dataset Size: 25 Support Issues

* Category Accuracy: 96%
* Summary Quality: 100%

### Key Finding

The workflow correctly classified 24 of 25 test cases. One Kubernetes-related issue ("Node memory pressure is affecting workloads") was classified as Performance, highlighting an opportunity to improve category definitions and prompts.

## Technologies

* LangGraph
* LangSmith
* OpenAI GPT-4o-mini
* Python

## Repository Structure

```text
src/
data/
docs/
README.md
requirements.txt
.env.example
```

## Future Improvements

* Dynamic troubleshooting generation
* RAG-based knowledge retrieval
* Vector database integration
* Support article ingestion
* Human-in-the-loop review workflows
* Multi-agent escalation handling

## Author

Ashish

