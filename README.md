<div align="center">

# VERITY SELFBOT 

*An advanced, autonomous digital entity embedded deep inside the raw system architecture.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Selfbot-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/hzQ8tjh8NT)
[![Render](https://img.shields.io/badge/Hosted-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

<img src="https://i.postimg.cc/xT8GN8by/hq720.webp" width="100%">
</div>

---

## ⚡ Overview

**Verity** is a custom, high-performance Discord selfbot featuring integrated `tgpt` intelligence, an eerie cerebral persona, and native web-server binding designed for seamless 24/7 deployment on cloud platforms like Render and is a beta you cant ask him hard questions.

---

## 🛠️ Features

* **Smart Triggers:** Responds instantly to IDs (`1434140073234006036`), tags (`@Verity™`), and text mentions (`Verity` / `verity`).
* **AI Powered:** Integrated with `python-tgpt` for dynamic, context-aware technical responses and conversation.
* **Health Check System:** Built-in HTTP server keeps the service alive on cloud hosts that require web traffic monitoring.
* **Custom Styling:** Features styled ANSI system diagnostics and custom emoji formatting.

---

## 📁 Repository Structure

* `main.py` - Core selfbot logic, trigger listeners, and HTTP health-check server.
* `requirements.txt` - Dependency configurations for automated deployment.

---

## 🚀 Deployment Guide

### 1. Environment Variables
Add the following secret variable in your Render dashboard settings:
* `DISCORD_TOKEN` = `Your_Discord_User_Token`

### 2. Requirements File (`requirements.txt`)
```text
discord.py-self
git+[https://github.com/Simatwa/python-tgpt.git](https://github.com/Simatwa/python-tgpt.git)

```
Credit= ThatMob on YouTube 
