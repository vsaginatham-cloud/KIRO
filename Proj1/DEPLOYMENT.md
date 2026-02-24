# 🚀 Deployment Guide - TTD Chatbot

## Local Deployment (Recommended for Testing)

### Step 1: Install Python
Ensure Python 3.8+ is installed:
```bash
python --version
```

### Step 2: Install Dependencies
```bash
cd Proj1
pip install -r requirements.txt
```

### Step 3: Get Gemini API Key
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key

### Step 4: Configure Environment
Create `.env` file:
```bash
GEMINI_API_KEY=AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA
```

### Step 5: Run Application
```bash
streamlit run app.py
```

Access at: http://localhost:8501

---

## Cloud Deployment Options

### Option 1: Streamlit Cloud (FREE & EASIEST)

**Advantages:**
- Free hosting
- Automatic updates from GitHub
- Easy setup
- HTTPS included

**Steps:**

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin your-repo-url
git push -u origin main
```

2. **Deploy on Streamlit Cloud**
- Visit: https://streamlit.io/cloud
- Sign in with GitHub
- Click "New app"
- Select your repository
- Select branch: main
- Main file path: app.py
- Click "Deploy"

3. **Add Secrets**
- In Streamlit Cloud dashboard
- Go to App Settings → Secrets
- Add:
```toml
GEMINI_API_KEY = "AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA"
```

4. **Access Your App**
- URL: https://your-app-name.streamlit.app

---

### Option 2: Heroku

**Advantages:**
- Free tier available
- Easy scaling
- Custom domain support

**Additional Files Needed:**

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

**Deployment Steps:**
```bash
heroku login
heroku create your-app-name
heroku config:set GEMINI_API_KEY=AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA
git push heroku main
```

---

### Option 3: AWS EC2

**Advantages:**
- Full control
- Scalable
- Professional deployment

**Steps:**

1. **Launch EC2 Instance**
- Ubuntu 22.04 LTS
- t2.micro (free tier)
- Open port 8501

2. **Connect and Setup**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip -y

# Clone repository
git clone your-repo-url
cd Proj1

# Install dependencies
pip3 install -r requirements.txt

# Create .env file
nano .env
# Add: GEMINI_API_KEY=AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA
```

3. **Run with Screen**
```bash
screen -S ttd-chatbot
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
# Press Ctrl+A then D to detach
```

4. **Access**
- http://your-ec2-ip:8501

**Optional: Setup Nginx + Domain**
```bash
sudo apt install nginx -y
sudo nano /etc/nginx/sites-available/ttd-chatbot
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

Enable:
```bash
sudo ln -s /etc/nginx/sites-available/ttd-chatbot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

### Option 4: Google Cloud Run

**Advantages:**
- Pay per use
- Auto-scaling
- Serverless

**Additional Files Needed:**

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Deployment:**
```bash
gcloud init
gcloud builds submit --tag gcr.io/your-project-id/ttd-chatbot
gcloud run deploy ttd-chatbot \
  --image gcr.io/your-project-id/ttd-chatbot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA
```

---

### Option 5: Docker (Any Platform)

**Create Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build and Run:**
```bash
docker build -t ttd-chatbot .
docker run -p 8501:8501 -e GEMINI_API_KEY=your_key ttd-chatbot
```

**Docker Compose (docker-compose.yml):**
```yaml
version: '3.8'
services:
  ttd-chatbot:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    restart: unless-stopped
```

Run:
```bash
docker-compose up -d
```

---

## Production Checklist

### Security
- [ ] API key stored in environment variables (not in code)
- [ ] `.env` file in `.gitignore`
- [ ] HTTPS enabled (for cloud deployments)
- [ ] Rate limiting configured (if needed)
- [ ] Input validation enabled

### Performance
- [ ] Caching enabled for static content
- [ ] Session state optimized
- [ ] API calls optimized
- [ ] Error handling implemented

### Monitoring
- [ ] Error logging configured
- [ ] Usage analytics (optional)
- [ ] Uptime monitoring
- [ ] API quota monitoring

### Maintenance
- [ ] Backup strategy
- [ ] Update schedule for knowledge base
- [ ] API key rotation plan
- [ ] Documentation updated

---

## Environment Variables

Required:
```
GEMINI_API_KEY=AIzaSyBInuifjGCWi1OB3t6dxVRp5Akm_2G9EnA
```

Optional (for future enhancements):
```
TTD_API_KEY=official_ttd_api_key_if_available
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email
SMTP_PASSWORD=your_password
```

---

## Updating the Application

### Update Knowledge Base
Edit `data/ttd_knowledge_base.py` with new information

### Update Booking Calendar
Edit `data/booking_calendar.py` for new year schedules

### Update Translations
Edit `utils/translator.py` to add more languages

### Deploy Updates

**Streamlit Cloud:**
- Just push to GitHub, auto-deploys

**Heroku:**
```bash
git push heroku main
```

**AWS/Docker:**
```bash
git pull
# Restart application
```

---

## Troubleshooting Deployment

### Issue: Port already in use
```bash
# Find process
lsof -i :8501
# Kill process
kill -9 PID
```

### Issue: Module not found
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: API key not working
- Check `.env` file exists
- Verify key is correct
- Check API quota not exceeded

### Issue: Slow performance
- Enable Streamlit caching
- Optimize API calls
- Use CDN for static assets

---

## Cost Estimates

### Free Options
- **Streamlit Cloud**: Free (with limits)
- **Heroku Free Tier**: Free (sleeps after 30 min)
- **AWS Free Tier**: Free for 12 months (t2.micro)

### Paid Options
- **Heroku Hobby**: $7/month
- **AWS t2.small**: ~$15/month
- **Google Cloud Run**: Pay per use (~$5-20/month)
- **DigitalOcean Droplet**: $6/month

### API Costs
- **Google Gemini**: Free tier available
- Check: https://ai.google.dev/pricing

---

## Support & Maintenance

### Regular Updates
- Update booking calendar yearly
- Update seva information as needed
- Monitor API changes
- Update dependencies quarterly

### Backup Strategy
- Daily database backups (if using database)
- Weekly code backups
- Environment variable backups (encrypted)

---

## Recommended Deployment

**For Personal Use:**
→ Local deployment or Streamlit Cloud

**For Small Organization:**
→ Streamlit Cloud or Heroku

**For Large Scale:**
→ AWS EC2 with load balancer or Google Cloud Run

---

**Need Help?** Check the README.md or contact support.

**Om Namo Venkatesaya** 🙏
