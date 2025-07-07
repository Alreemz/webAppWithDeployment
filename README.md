webapp-deployment/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components/
│   │   │   ├── TeamForm.js
│   │   │   ├── RoleForm.js
│   │   │   └── AssignRole.js
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── provider.tf
├── ansible/
│   ├── inventory.ini
│   └── playbook.yml
└── README.md

# WebApp Deployment Project

## 📦 Project Overview
This is a full-stack web application that allows users to manage **Teams and Roles**. It includes:
- **Backend**: Flask REST API with PostgreSQL
- **Frontend**: React.js
- **Deployment**: Docker, Terraform (EC2), and Ansible (container automation)

---

## 🧱 Folder Structure
```
webapp-deployment/
├── backend/               # Flask application
├── frontend/              # React.js frontend
├── docker-compose.yml     # Multi-container config
├── terraform/             # EC2 provisioning
├── ansible/               # Docker deployment
└── README.md              # Setup guide
```

---

## 🚀 Local Setup with Docker Compose

### Step 1: Clone the Repository
```bash
git clone <repo-url>
cd webapp-deployment
```

### Step 2: Run Docker Compose
```bash
docker-compose up --build
```

### Access URLs
- React Frontend: http://localhost:3000
- Flask API: http://localhost:5000/api
- Swagger UI: http://localhost:5000/

---

## ☁️ Deploying to AWS EC2

### Step 1: Provision EC2 Using Terraform
```bash
cd terraform
terraform init
terraform apply
```
Note the public IP output.

### Step 2: Update Inventory File
```ini
# ansible/inventory.ini
[web]
<EC2_PUBLIC_IP> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/key.pem
```

### Step 3: Deploy with Ansible
```bash
cd ansible
ansible-playbook -i inventory.ini playbook.yml
```

---

## ✅ Features
- CRUD operations for Teams and Roles
- Assign roles to teams
- Swagger UI for API docs

---

## 🔧 Tech Stack
- Flask, Flask-RESTX, SQLAlchemy
- PostgreSQL
- React.js, Axios
- Docker, Terraform, Ansible

---

## 👩‍💻 Author
Your Name  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)


