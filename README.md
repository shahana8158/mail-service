# Mail Service Project

This is a simple mail service built using **Python** and **Serverless Framework**.  
It allows sending emails via Gmail SMTP. The service is tested locally using **serverless-offline**.

**Note:** Email sending part is currently implemented using Gmail SMTP with App Passwords.  
In real-world deployment, this can also be integrated with AWS SES or any SMTP provider.

---

## ✨ Features
- Send email using Gmail SMTP  
- Input validation (receiver, subject, body required)  
- Local testing with `serverless-offline`  

---

## 🛠 Tech Stack

- **Python** (handler function)
- **Serverless Framework**
- **serverless-offline** (for local API testing)
- **Node.js & npm**
- **Gmail SMTP** (App Password based)

---


## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/shahana8158/mail-service.git
   cd mail-service
