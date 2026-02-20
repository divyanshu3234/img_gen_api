# AI Image Generation API (FastAPI + Vertex AI Imagen)

A simple image generation API built using FastAPI and Google Vertex AI (Imagen 3), deployed on Google Cloud Run.

This project demonstrates how to build and deploy a production-ready AI-powered backend for generating images from text prompts.

# 🚀 Features

Text-to-Image generation using Vertex AI (Imagen 3)

FastAPI backend

Cloud Run deployment

CORS enabled

Health check endpoint

Demo-safe rate limiting

Base64 image response


# 🏗 Architecture

Frontend / Client
→ FastAPI (Cloud Run)
→ Vertex AI (Imagen 3)
→ Base64 Image Response

# 📦 Tech Stack

Python 3.11

FastAPI

Uvicorn

Google Cloud Vertex AI

Cloud Run

Docker

# CURL REQUEST

curl https://image-api-322039733047.us-central1.run.app/health


