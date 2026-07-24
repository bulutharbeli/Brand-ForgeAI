# Deployment Guide - Brand Forge AI

## Production Deployment Checklist

### 1. Security Configuration
- [ ] Change `SECRET_KEY` in `.env` to a secure random value
- [ ] Enable HTTPS with SSL/TLS certificates
- [ ] Configure CORS for production domains only
- [ ] Set up rate limiting
- [ ] Enable input validation and sanitization
- [ ] Configure secure HTTP headers

### 2. Database Setup
- [ ] Migrate from SQLite to PostgreSQL for production
- [ ] Set up database backups
- [ ] Configure connection pooling
- [ ] Set up database migrations

### 3. Performance Optimization
- [ ] Enable Gzip compression
- [ ] Configure caching (Redis recommended)
- [ ] Set up CDN for static assets
- [ ] Optimize database queries
- [ ] Enable Flask production mode

### 4. Monitoring & Logging
- [ ] Set up application monitoring (New Relic, DataDog, etc.)
- [ ] Configure log rotation
- [ ] Set up error tracking (Sentry, Rollbar)
- [ ] Monitor API endpoint performance
- [ ] Set up uptime monitoring

### 5. Scalability
- [ ] Use Gunicorn or uWSGI instead of Flask's dev server
- [ ] Set up load balancer (Nginx recommended)
- [ ] Configure horizontal scaling
- [ ] Set up Redis for session management
- [ ] Use async task queue (Celery) for heavy AI operations

## Deployment Options

### Option 1: Traditional VPS (DigitalOcean, Linode, AWS EC2)

1. **Server Setup**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3-pip python3-venv nginx postgresql redis-server -y

# Clone repository
git clone https://github.com/bulutharbeli/Brand-ForgeAI.git
cd Brand-ForgeAI

# Run setup
bash setup.sh
```

2. **Configure PostgreSQL**
```bash
# Create database
sudo -u postgres psql
CREATE DATABASE brand_forge;
CREATE USER brandforge WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE brand_forge TO brandforge;
\q
```

3. **Update Configuration**
```python
# config.py
import os

class ProductionConfig:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'postgresql://brandforge:password@localhost/brand_forge'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    REDIS_URL = 'redis://localhost:6379/0'
```

4. **Set up Gunicorn**
```bash
# Install gunicorn
pip install gunicorn

# Create systemd service
sudo nano /etc/systemd/system/brand-forge.service
```

Service file content:
```ini
[Unit]
Description=Brand Forge AI
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/Brand-ForgeAI
Environment="PATH=/home/ubuntu/Brand-ForgeAI/venv/bin"
ExecStart=/home/ubuntu/Brand-ForgeAI/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

5. **Configure Nginx**
```nginx
# /etc/nginx/sites-available/brand-forge
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /home/ubuntu/Brand-ForgeAI/static;
    }
}
```

6. **Start Services**
```bash
sudo systemctl start brand-forge
sudo systemctl enable brand-forge
sudo nginx -t
sudo systemctl restart nginx
```

### Option 2: Docker Deployment

1. **Create Dockerfile**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

2. **Create docker-compose.yml**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db:5432/brand_forge
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=brand_forge
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
  
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

volumes:
  postgres_data:
```

3. **Deploy**
```bash
docker-compose up -d
```

### Option 3: Cloud Platform (Heroku, Railway, Render)

#### Heroku Deployment

1. **Create Procfile**
```
web: gunicorn app:app
```

2. **Configure for Heroku**
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create brand-forge-ai

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Add Redis
heroku addons:create heroku-redis:hobby-dev

# Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your_secure_key

# Deploy
git push heroku main
```

#### Railway Deployment

1. Connect GitHub repository to Railway
2. Add PostgreSQL and Redis plugins
3. Set environment variables
4. Deploy automatically on push

### Option 4: Serverless (AWS Lambda, Google Cloud Functions)

For serverless deployment, you'll need to:
1. Refactor app.py to use serverless handlers
2. Use Aurora Serverless for database
3. Use ElastiCache for Redis
4. Configure API Gateway

## Environment Variables

Create a `.env` file with the following:

```bash
# Flask
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-super-secure-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost/brand_forge

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
CORS_ORIGINS=https://yourdomain.com
RATE_LIMIT=100 per hour

# Optional: AI/ML API Keys (for future enhancements)
OPENAI_API_KEY=sk-...
HUGGINGFACE_API_KEY=hf_...
```

## Performance Tuning

### 1. Enable Caching
```python
# Install Flask-Caching
pip install Flask-Caching

# Configure in app.py
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'redis'})

def create_app():
    app = Flask(__name__)
    cache.init_app(app)
    return app

# Use in routes
@cache.cached(timeout=300)
def generate_brand_name():
    ...
```

### 2. Database Optimization
```python
# Use connection pooling
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
```

### 3. Async Processing
For heavy AI operations, use Celery:

```python
# tasks.py
from celery import Celery

celery = Celery('brand_forge', broker=REDIS_URL)

@celery.task
def async_generate_brand(data):
    # Heavy processing here
    return result
```

## Backup Strategy

### Database Backup
```bash
# Daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d)
pg_dump brand_forge > backups/brand_forge_$DATE.sql
gzip backups/brand_forge_$DATE.sql

# Keep only last 7 days
find backups/ -name "*.sql.gz" -mtime +7 -delete
```

### File Backup
```bash
# Backup exports and uploads
rsync -avz /path/to/exports/ /backup/exports/
rsync -avz /path/to/uploads/ /backup/uploads/
```

## SSL/HTTPS Setup

### Using Let's Encrypt (Free)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Generate certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo certbot renew --dry-run
```

## Monitoring Setup

### 1. Application Monitoring with New Relic
```bash
# Install New Relic
pip install newrelic

# Configure
newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini

# Run with New Relic
newrelic-admin run-program gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 2. Error Tracking with Sentry
```bash
# Install Sentry SDK
pip install sentry-sdk[flask]

# Configure in app.py
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="YOUR_SENTRY_DSN",
    integrations=[FlaskIntegration()],
    environment="production"
)
```

## Scaling Considerations

### Horizontal Scaling
- Use load balancer (Nginx, HAProxy)
- Sticky sessions or Redis for session management
- Database read replicas
- CDN for static assets

### Vertical Scaling
- Increase server resources (CPU, RAM)
- Optimize database queries
- Use connection pooling
- Enable caching layers

## Security Hardening

1. **Firewall Configuration**
```bash
# UFW (Uncomplicated Firewall)
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS
sudo ufw enable
```

2. **Fail2Ban for Brute Force Protection**
```bash
sudo apt install fail2ban
sudo systemctl enable fail2ban
```

3. **Regular Updates**
```bash
# Automatic security updates
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

## Troubleshooting

### Common Issues

1. **Application won't start**
   - Check logs: `journalctl -u brand-forge`
   - Verify environment variables
   - Check database connection

2. **Slow performance**
   - Enable caching
   - Check database indexes
   - Monitor server resources

3. **Database connection errors**
   - Verify DATABASE_URL
   - Check PostgreSQL is running
   - Verify user permissions

## Support

For deployment support:
- Check GitHub Issues
- Review application logs
- Contact: support@brandforgeai.com

---

**Last Updated**: 2024
**Author**: Brand Forge AI Team
