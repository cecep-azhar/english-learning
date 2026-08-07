# PRD: English for Remote Full-Stack Developer
## FathForce Academy — english.tool.biz.id

**Author:** Cecep Saeful Azhar Hidaya, ST
**Version:** 1.0
**Date:** July 2026
**Status:** Phase 1-2 Complete, Phase 3-5 Planning

---

## 📋 Table of Contents

1. [Product Overview](#1-product-overview)
2. [Target Market](#2-target-market)
3. [Problem & Solution](#3-problem--solution)
4. [Architecture](#4-architecture)
5. [Features Roadmap](#5-features-roadmap)
6. [SEO Strategy](#6-seo-strategy)
7. [Monetization](#7-monetization)
8. [Payment Integration (Mayar.id)](#8-payment-integration-mayarid)
9. [AI Token Usage](#9-ai-token-usage)
10. [Database Schema](#10-database-schema)
11. [Technical Specifications](#11-technical-specifications)
12. [Deployment](#12-deployment)
13. [Timeline](#13-timeline)
14. [Success Metrics](#14-success-metrics)

---

## 1. Product Overview

### What
Interactive English learning platform specifically designed for Indonesian full-stack developers who want to work remotely for international companies.

### Why
- **80%** Indonesian developers cannot pass English interview stage
- **90%** remote job listings require conversational English
- **0** existing platforms tailored for "English + Developer context"

### How
Gamified learning app with 4 core skills:
- 🎧 **Listening** — Comprehension quizzes with audio
- 🎤 **Speaking** — Speech recognition + pronunciation scoring
- 📖 **Reading** — Context-based comprehension
- ✍️ **Writing** — AI-graded writing exercises

### Unique Value
- **Developer-specific content** (not generic English)
- **Real scenarios** (interview, client call, standup meeting)
- **Free tier** accessible to everyone
- **Indonesian UI** with English content

---

## 2. Target Market

### Primary Persona
```
Name: Indonesian Full-Stack Developer
Age: 22-35
Income: Rp 5-15 juta/bulan
Goal: Apply remote job luar negeri ($1000-3000/bulan)
Pain: Tidak percaya diri bahasa Inggris
Platform: Mobile-first (Android 80%, iOS 20%)
```

### Market Size
| Segment | Size |
|---------|------|
| Indonesian developers | ~500,000 |
| Interested in remote work | ~150,000 |
| Willing to pay for English | ~30,000 |
| **TAM (Total Addressable)** | **~Rp 36 Miliar/tahun** |

### Competitors
| Competitor | Weakness |
|------------|----------|
| Duolingo | Generic, no developer context |
| English First | Expensive (Rp 2-5jt/bulan) |
| Coursera English | Not interactive, no speaking |
| YouTube tutorials | No structure, no practice |

**Our advantage:** Developer-specific + affordable + interactive

---

## 3. Problem & Solution

### Problem Statement
> "Indonesian full-stack developers have the technical skills for remote work but cannot pass English interviews and struggle with daily English communication, costing them $1000-3000/month in potential income."

### Solution Matrix
| Problem | Solution | Feature |
|---------|----------|---------|
| Can't understand English interviews | Practice with real scripts | Listening Quiz |
| Can't speak English confidently | Speech recognition + scoring | Speaking Module |
| Can't write professional emails | AI-graded writing | Writing Exercises |
| Don't know developer vocabulary | Curated vocab list | Vocabulary Builder |
| No time for classes | 5-10 min daily practice | Mobile-first app |
| Expensive courses | Freemium model | Free tier + Premium |

---

## 4. Architecture

### Current (Phase 1-2) — Static
```
Nginx (Docker) → Static HTML + JS
                 ↓
            scripts.json (content)
            audio/*.mp3 (TTS)
```

### Target (Phase 3+) — Fullstack Go
```
┌─────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                  │
│  HTML + HTMX + Tailwind CSS                         │
│  Web Speech API (Speaking)                           │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP / HX-Request
                       ▼
┌─────────────────────────────────────────────────────┐
│                  GO SERVER (Echo)                    │
│  ├── Handlers (HTMX responses)                      │
│  ├── Middleware (Auth, Rate Limit, CORS)             │
│  ├── Templates (html/template)                      │
│  └── AI Proxy (rate-limited)                        │
├─────────────────────────────────────────────────────┤
│                  SERVICES                           │
│  ├── AuthService (JWT + Refresh Token)              │
│  ├── ProgressService (XP, Streak, Level)            │
│  ├── PaymentService (Mayar.id webhook)              │
│  ├── AIService (Writing grading, feedback)          │
│  └── ContentService (Scripts, Audio)                │
├─────────────────────────────────────────────────────┤
│                  DATA LAYER                         │
│  ├── PostgreSQL (Users, Progress, Payments)         │
│  └── Redis (Session cache, Rate limiting)           │
├─────────────────────────────────────────────────────┤
│                  EXTERNAL                           │
│  ├── Mayar.id (Payment gateway)                     │
│  ├── OpenRouter (AI API)                            │
│  └── Cloudflare (CDN, Tunnel)                       │
└─────────────────────────────────────────────────────┘
```

### Why Go + HTMX?
| Factor | Go + HTMX | React/Next.js |
|--------|-----------|---------------|
| Bundle size | ~0 KB JS | ~200+ KB |
| First paint | ⚡ instant | ⏳ loading |
| SEO | ✅ server-rendered | ⚠️ needs SSR setup |
| Memory (server) | ~10 MB | ~100+ MB |
| Build time | ~2s | ~30s+ |
| Learning curve | Low (for backend dev) | High |
| Real-time feel | ✅ HTMX OOB | ✅ |

---

## 5. Features Roadmap

### Phase 1 ✅ (COMPLETE)
- [x] Static learning content (10 chapters, 120 lines)
- [x] Audio playback (TTS)
- [x] Listening comprehension quiz
- [x] Reading comprehension quiz
- [x] Vocabulary builder (flashcards + quiz)
- [x] Fill-in-the-blank exercises
- [x] Progress tracking (localStorage)
- [x] XP + Streak + Level system

### Phase 2 ✅ (COMPLETE)
- [x] Speaking module (Web Speech API)
- [x] Speech recognition + scoring
- [x] Free talk mode (30s timer)
- [x] Conversation simulator
- [x] Word-by-word pronunciation feedback

### Phase 3 🔄 (IN PROGRESS)
- [ ] Go + HTMX migration
- [ ] User authentication (register/login)
- [ ] PostgreSQL database
- [ ] Progress sync across devices
- [ ] Content management (admin panel)

### Phase 4 📅 (NEXT)
- [ ] Payment integration (Mayar.id)
- [ ] Premium features gating
- [ ] Writing module (AI-graded)
- [ ] AI feedback for speaking
- [ ] Certificate of completion

### Phase 5 📅 (FUTURE)
- [ ] Mobile PWA (installable)
- [ ] Daily challenge (push notification)
- [ ] Leaderboard (global)
- [ ] Community features
- [ ] Course bundle marketplace

---

## 6. SEO Strategy

### Target Keywords
| Keyword | Volume/Bulan | Difficulty |
|---------|-------------|------------|
| belajar bahasa inggris untuk programmer | 2,400 | Low |
| english for developers | 1,900 | Medium |
| bahasa inggris teknologi | 1,600 | Low |
| remote developer english | 880 | Low |
| interview bahasa inggris programmer | 720 | Low |
| belajar speaking inggris online | 3,600 | Medium |
| english for remote work | 1,200 | Low |

### On-Page SEO
```html
<!-- Meta tags -->
<title>English for Remote Worker - Belajar Bahasa Inggris untuk Developer</title>
<meta name="description" content="Platform belajar bahasa Inggris khusus full-stack developer. Listening, speaking, reading, writing untuk remote work. Gratis!">
<meta name="keywords" content="english developer, bahasa inggris programmer, remote work english">

<!-- Open Graph -->
<meta property="og:title" content="English for Remote Worker">
<meta property="og:description" content="Master English for interviews, meetings, and remote work">
<meta property="og:image" content="/og-image.png">
<meta property="og:url" content="https://english.ypc.my.id">

<!-- Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "English for Remote Worker",
  "url": "https://english.ypc.my.id",
  "applicationCategory": "EducationalApplication",
  "operatingSystem": "Web",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "IDR"
  }
}
</script>
```

### Technical SEO
- [ ] Server-side rendering (Go templates)
- [ ] Clean URLs (`/chapter/self-introduction`)
- [ ] Sitemap.xml auto-generated
- [ ] Robots.txt
- [ ] Page speed < 2s (Lighthouse 90+)
- [ ] Mobile responsive (Core Web Vitals)
- [ ] Canonical URLs
- [ ] Breadcrumb navigation

### Content SEO
- [ ] Blog section: "Tips English untuk Developer"
- [ ] Landing pages per chapter
- [ ] FAQ section
- [ ] Testimonial section
- [ ] Case studies (developer sukses remote)

### Off-Page SEO
- [ ] Backlink dari komunitas developer Indonesia
- [ ] Guest post di dev.to, medium.com
- [ ] Share di Twitter/X, LinkedIn
- [ ] YouTube: "English for Developer" series
- [ ] TikTok: Short English tips

### Expected Traffic
| Month | Organic Traffic | Source |
|-------|----------------|--------|
| Month 1 | 500 | Direct + Social |
| Month 3 | 2,000 | SEO starting |
| Month 6 | 10,000 | SEO + Content |
| Month 12 | 30,000+ | Full SEO |

---

## 7. Monetization

### Model: Freemium + Course Bundle

#### Free Tier (Lead Magnet)
| Feature | Limit |
|---------|-------|
| Chapters | 3 of 10 |
| Listening quiz | ✅ |
| Reading quiz | ✅ |
| Vocabulary | 10 words |
| Speaking | 5 practices/hari |
| Writing | ❌ |
| Progress sync | ❌ |

#### Premium (Rp 99.000/bulan)
| Feature | Limit |
|---------|-------|
| Chapters | All 10 |
| Listening quiz | Unlimited |
| Reading quiz | Unlimited |
| Vocabulary | All 44+ words |
| Speaking | Unlimited |
| Writing (AI-graded) | 20/hari |
| Progress sync | ✅ |
| Certificate | ✅ |
| Priority support | ✅ |

#### Lifetime (Rp 399.000)
- Same as Premium
- One-time payment
- All future updates included

#### Course Bundle (Rp 499.000)
- Premium access (lifetime)
- 4x group coaching (Zoom)
- WhatsApp group access
- 1x 1-on-1 speaking practice
- Certificate

### Revenue Projections
| Month | Free Users | Premium | Revenue |
|-------|-----------|---------|---------|
| Month 3 | 2,000 | 20 (1%) | Rp 2jt |
| Month 6 | 8,000 | 80 (1%) | Rp 8jt |
| Month 12 | 30,000 | 450 (1.5%) | Rp 45jt |
| Month 24 | 100,000 | 2,000 (2%) | Rp 200jt |

### Pricing Strategy
- **Rp 99.000/bulan** = less than 1 jam freelance rate
- **Rp 399.000 lifetime** = 4 bulan premium = value
- **Rp 499.000 course** = 1/10 of bootcamp price

---

## 8. Payment Integration (Mayar.id)

### Why Mayar.id?
- ✅ Indonesian payment gateway
- ✅ Support: VA, QRIS, E-Wallet, Credit Card
- ✅ Easy API (REST)
- ✅ Low fees (1.5-2%)
- ✅ Webhook support
- ✅ No monthly fee (pay per transaction)

### Integration Flow

```
User clicks "Upgrade to Premium"
        ↓
Frontend → POST /api/checkout
        ↓
Go Server → Create invoice via Mayar.id API
        ↓
Mayar.id → Return payment URL
        ↓
User → Redirect to Mayar.id payment page
        ↓
User completes payment
        ↓
Mayar.id → Webhook POST /api/webhook/mayar
        ↓
Go Server → Verify signature → Update user plan
        ↓
User sees "Premium Active" 🎉
```

### API Integration

#### 1. Create Invoice
```go
// POST https://api.mayar.id/v1/invoice
// Headers: Authorization: Bearer {API_KEY}

type MayarInvoice struct {
    Name        string `json:"name"`
    Email       string `json:"email"`
    Phone       string `json:"phone"`
    Amount      int    `json:"amount"`
    Description string `json:"description"`
    ExpiredAt   string `json:"expired_at"`
    RedirectURL string `json:"redirect_url"`
    CallbackURL string `json:"callback_url"`
    Items       []Item `json:"items"`
}

type Item struct {
    Name     string `json:"name"`
    Quantity int    `json:"quantity"`
    Price    int    `json:"price"`
    URL      string `json:"url,omitempty"`
}
```

#### 2. Webhook Handler
```go
// POST /api/webhook/mayar
// Mayar.id sends payment status updates

func HandleMayarWebhook(c echo.Context) error {
    var payload MayarWebhook
    if err := c.Bind(&payload); err != nil {
        return err
    }
    
    // Verify signature
    if !VerifyMayarSignature(payload) {
        return echo.ErrUnauthorized
    }
    
    // Update user premium status
    switch payload.Status {
    case "paid":
        ActivatePremium(payload.UserID, payload.PlanType)
    case "expired":
        HandleExpiredInvoice(payload.InvoiceID)
    }
    
    return c.JSON(200, map[string]string{"status": "ok"})
}
```

#### 3. Payment Methods
| Method | Fee | Settle Time |
|--------|-----|-------------|
| VA (BCA, BRI, Mandiri) | 1.5% | Instant |
| QRIS | 1.5% | Instant |
| GoPay | 2% | Instant |
| OVO | 2% | Instant |
| Credit Card | 2.9% + Rp 2,000 | 2 days |

### Database Tables
```sql
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    mayar_invoice_id VARCHAR(100),
    amount INTEGER NOT NULL,
    currency VARCHAR(3) DEFAULT 'IDR',
    plan_type VARCHAR(20) NOT NULL, -- 'monthly', 'lifetime', 'course'
    payment_method VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pending', -- pending, paid, failed, expired
    paid_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    plan_type VARCHAR(20) NOT NULL,
    starts_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP,
    payment_id UUID REFERENCES payments(id),
    status VARCHAR(20) DEFAULT 'active', -- active, expired, cancelled
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 9. AI Token Usage

### Use Cases
| Feature | Model | Input Tokens | Output Tokens | Cost/Call |
|---------|-------|-------------|---------------|-----------|
| Writing grading | Claude Haiku | ~500 | ~200 | $0.0004 |
| Grammar check | MiMo v2.5 | ~300 | ~150 | Free |
| Speaking feedback | MiMo v2.5 | ~400 | ~200 | Free |
| Vocabulary example | MiMo v2.5 | ~200 | ~100 | Free |

### Cost Optimization Strategy

#### Tier 1: Free (MiMo v2.5)
- ✅ Grammar check
- ✅ Simple vocabulary examples
- ✅ Speaking pronunciation feedback
- **Cost: $0**

#### Tier 2: Premium (Claude Haiku)
- ✅ Writing essay grading (complex)
- ✅ Detailed writing feedback
- ✅ Grammar correction with explanation
- **Cost: ~$0.001/call**

### Budget Projection (1000 Active Users)
| Scenario | AI Calls/Day | Cost/Day | Cost/Month |
|----------|-------------|----------|------------|
| Light use (500 users) | 1,000 | $0.50 | $15 |
| Medium use (500 users) | 3,000 | $1.50 | $45 |
| Heavy use (500 users) | 5,000 | $2.50 | $75 |

### Rate Limits
```go
const (
    FreeDailyLimit    = 0    // No AI for free users
    PremiumDailyLimit = 20   // 20 AI calls per day
    PremiumHourLimit  = 5    // 5 per hour max
)
```

### Prompt Templates

#### Writing Grading
```go
const writingGradingPrompt = `You are an English teacher for Indonesian developers.
Grade this writing exercise:

Topic: {{.Topic}}
User's writing: {{.Writing}}
Expected answer (if applicable): {{.Expected}}

Provide:
1. Score (0-100)
2. Grammar corrections (if any)
3. Vocabulary suggestions
4. Fluency feedback
5. Improved version

Respond in JSON format.`
```

#### Speaking Feedback
```go
const speakingFeedbackPrompt = `You are a pronunciation coach.
The user said: "{{.Transcribed}}"
Expected: "{{.Expected}}"
Similarity score: {{.Score}}%

Provide brief feedback on:
1. Pronunciation accuracy
2. Suggested improvements
3. Common mistakes to avoid

Keep response under 100 words.`
```

---

## 10. Database Schema

### Complete Schema

```sql
-- =============================================
-- USERS
-- =============================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    avatar_url VARCHAR(500),
    plan VARCHAR(20) DEFAULT 'free', -- free, premium, lifetime
    plan_expires_at TIMESTAMP,
    streak_count INTEGER DEFAULT 0,
    last_active_at TIMESTAMP,
    total_xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);

-- =============================================
-- USER PROGRESS
-- =============================================
CREATE TABLE user_progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    chapter VARCHAR(100) NOT NULL,
    skill_type VARCHAR(20) NOT NULL, -- listening, reading, speaking, writing, vocabulary
    score INTEGER DEFAULT 0,
    total_attempts INTEGER DEFAULT 0,
    best_score INTEGER DEFAULT 0,
    completed BOOLEAN DEFAULT FALSE,
    last_practiced_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, chapter, skill_type)
);

CREATE INDEX idx_progress_user ON user_progress(user_id);

-- =============================================
-- WRITING EXERCISES
-- =============================================
CREATE TABLE writing_exercises (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    chapter VARCHAR(100) NOT NULL,
    topic TEXT NOT NULL,
    user_input TEXT NOT NULL,
    ai_score INTEGER, -- 0-100
    ai_feedback JSONB, -- {grammar: [], vocabulary: [], improved: ""}
    ai_model VARCHAR(50), -- which model was used
    tokens_used INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_writing_user ON writing_exercises(user_id);

-- =============================================
-- SPEAKING PRACTICES
-- =============================================
CREATE TABLE speaking_practices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    chapter VARCHAR(100) NOT NULL,
    script_num_id INTEGER, -- reference to scripts.json
    mode VARCHAR(20) NOT NULL, -- practice, freetalk, conversation
    expected_text TEXT,
    transcribed_text TEXT,
    similarity_score INTEGER, -- 0-100
    audio_url VARCHAR(500), -- stored recording (optional)
    duration_seconds INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_speaking_user ON speaking_practices(user_id);

-- =============================================
-- PAYMENTS
-- =============================================
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    mayar_invoice_id VARCHAR(100),
    mayar_transaction_id VARCHAR(100),
    amount INTEGER NOT NULL, -- in Rupiah
    currency VARCHAR(3) DEFAULT 'IDR',
    plan_type VARCHAR(20) NOT NULL, -- monthly, lifetime, course
    payment_method VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pending', -- pending, paid, failed, refunded, expired
    paid_at TIMESTAMP,
    expires_at TIMESTAMP, -- for monthly plan
    metadata JSONB, -- extra data
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_payments_user ON payments(user_id);
CREATE INDEX idx_payments_mayar ON payments(mayar_invoice_id);

-- =============================================
-- SUBSCRIPTIONS
-- =============================================
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    plan_type VARCHAR(20) NOT NULL,
    starts_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP, -- NULL for lifetime
    payment_id UUID REFERENCES payments(id),
    status VARCHAR(20) DEFAULT 'active', -- active, expired, cancelled
    cancelled_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_subs_user ON subscriptions(user_id);
CREATE INDEX idx_subs_status ON subscriptions(status);

-- =============================================
-- DAILY AI USAGE (rate limiting)
-- =============================================
CREATE TABLE ai_usage (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    feature VARCHAR(20) NOT NULL, -- writing, speaking, vocabulary
    tokens_input INTEGER DEFAULT 0,
    tokens_output INTEGER DEFAULT 0,
    model VARCHAR(50),
    cost_cents INTEGER DEFAULT 0, -- cost in cents of dollar
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_ai_usage_user_date ON ai_usage(user_id, created_at);

-- =============================================
-- LEADERBOARD (materialized view for speed)
-- =============================================
CREATE MATERIALIZED VIEW leaderboard AS
SELECT 
    u.id,
    u.name,
    u.total_xp,
    u.level,
    u.streak_count,
    RANK() OVER (ORDER BY u.total_xp DESC) as rank
FROM users u
WHERE u.total_xp > 0;

CREATE UNIQUE INDEX idx_leaderboard_rank ON leaderboard(id, rank);
```

---

## 11. Technical Specifications

### Go Project Structure
```
english-learning/
├── cmd/
│   └── server/
│       └── main.go              # Entry point
├── internal/
│   ├── handler/                  # HTTP handlers
│   │   ├── auth.go
│   │   ├── quiz.go
│   │   ├── progress.go
│   │   ├── payment.go
│   │   └── api.go
│   ├── middleware/
│   │   ├── auth.go              # JWT middleware
│   │   ├── rate.go              # Rate limiting
│   │   └── cors.go
│   ├── model/
│   │   ├── user.go
│   │   ├── progress.go
│   │   └── payment.go
│   ├── service/
│   │   ├── auth.go              # Auth logic
│   │   ├── ai.go                # AI integration
│   │   ├── payment.go           # Mayar.id
│   │   └── progress.go
│   ├── repository/
│   │   ├── user.go
│   │   ├── progress.go
│   │   └── payment.go
│   └── template/
│       ├── layout.html
│       ├── index.html
│       ├── quiz.html
│       ├── auth/
│       └── partials/            # HTMX partials
├── web/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── audio/
│   └── template/
├── migrations/
│   └── 001_initial.sql
├── config/
│   └── config.go
├── go.mod
├── go.sum
├── Dockerfile
└── docker-compose.yml
```

### Dependencies
```go
// go.mod
module english-learning

go 1.22

require (
    github.com/labstack/echo/v4 v4.12.0    // HTTP framework
    github.com/golang-jwt/jwt/v5 v5.2.1     // JWT auth
    github.com/jackc/pgx/v5 v5.6.0          // PostgreSQL
    github.com/redis/go-redis/v9 v9.7.0     // Redis
    github.com/go-playground/validator/v10  // Validation
    golang.org/x/crypto v0.25.0             // Password hashing
)
```

### Environment Variables
```bash
# Database
DATABASE_URL=postgres://user:pass@localhost:5432/english_learning
REDIS_URL=redis://localhost:6379

# Auth
JWT_SECRET=your-secret-key
JWT_EXPIRY=24h

# Mayar.id
MAYAR_API_KEY=your-api-key
MAYAR_WEBHOOK_SECRET=your-webhook-secret

# AI
OPENROUTER_API_KEY=your-key
AI_MODEL_FREE=xiaomi/mimo-v2.5
AI_MODEL_PREMIUM=anthropic/claude-3-haiku

# Server
PORT=3000
ENV=production
```

### API Endpoints
```
# Auth
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/logout
POST   /api/auth/refresh

# Progress
GET    /api/progress
PUT    /api/progress
GET    /api/leaderboard

# Quiz (HTMX)
GET    /chapter/{slug}
POST   /quiz/listening/submit
POST   /quiz/reading/submit
POST   /quiz/vocabulary/submit
POST   /quiz/fillblank/submit

# Speaking (HTMX)
POST   /speaking/submit
POST   /speaking/freetalk/submit

# Writing (HTMX)
GET    /writing/{chapter}
POST   /writing/submit
GET    /writing/ai-feedback

# Payment
POST   /api/checkout
POST   /api/webhook/mayar
GET    /api/subscription/status

# Content
GET    /api/scripts.json
GET    /api/chapters
```

---

## 12. Deployment

### Docker Compose
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3002:3000"
    environment:
      - DATABASE_URL=postgres://english:pass@db:5432/english_learning
      - REDIS_URL=redis://cache:6379
    depends_on:
      - db
      - cache
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./migrations:/docker-entrypoint-initdb.d
    environment:
      - POSTGRES_DB=english_learning
      - POSTGRES_USER=english
      - POSTGRES_PASSWORD=pass
    restart: unless-stopped

  cache:
    image: redis:7-alpine
    restart: unless-stopped

volumes:
  pgdata:
```

### Cloudflare Tunnel Config
```yaml
# /etc/cloudflared/config.yml
tunnel: f6fb19b8-cb9e-47b5-a134-b77045459cff
credentials-file: /root/.cloudflared/f6fb19b8-cb9e-47b5-a134-b77045459cff.json

ingress:
  - hostname: english.tool.biz.id
    service: http://localhost:3002
  - service: http_status:404
```

### CI/CD Pipeline
```yaml
# GitHub Actions
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build Docker image
        run: docker build -t english-learning .
      
      - name: Deploy to YPC
        run: |
          docker save english-learning | ssh ypc "docker load"
          ssh ypc "cd /path/to/project && docker-compose up -d"
```

---

## 13. Timeline

### Phase 3: Fullstack Migration (Week 1-3)
| Week | Task | Deliverable |
|------|------|-------------|
| Week 1 | Go project setup, DB schema, Auth | Register/Login working |
| Week 2 | HTMX integration, Quiz migration | All quizzes working with auth |
| Week 3 | Progress sync, Testing | Phase 3 complete |

### Phase 4: Monetization (Week 4-6)
| Week | Task | Deliverable |
|------|------|-------------|
| Week 4 | Mayar.id integration | Payment flow working |
| Week 5 | Premium gating, Writing module | AI writing grading |
| Week 6 | Admin dashboard, Testing | Phase 4 complete |

### Phase 5: Growth (Week 7-10)
| Week | Task | Deliverable |
|------|------|-------------|
| Week 7 | PWA setup, Push notifications | Installable app |
| Week 8 | SEO optimization, Blog | Organic traffic |
| Week 9 | Community features | Leaderboard, sharing |
| Week 10 | Launch preparation | Phase 5 complete |

---

## 14. Success Metrics

### KPIs
| Metric | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|----------|
| Registered Users | 2,000 | 8,000 | 30,000 |
| Daily Active Users | 200 | 1,000 | 5,000 |
| Premium Conversion | 1% | 1.5% | 2% |
| Monthly Revenue | Rp 2jt | Rp 8jt | Rp 45jt |
| Retention (D7) | 30% | 40% | 50% |
| NPS Score | 30 | 40 | 50 |

### Technical Metrics
| Metric | Target |
|--------|--------|
| Page Load Time | < 2s |
| Lighthouse Score | > 90 |
| API Response Time | < 200ms |
| Uptime | 99.9% |
| Error Rate | < 0.1% |

### Business Metrics
| Metric | Target |
|--------|--------|
| CAC (Customer Acquisition Cost) | < Rp 10,000 |
| LTV (Lifetime Value) | > Rp 300,000 |
| LTV:CAC Ratio | > 30:1 |
| Payback Period | < 3 months |

---

## Appendix

### A. Content Structure (scripts.json)
```json
{
  "chapters": [
    {
      "id": 1,
      "title": "Self-Introduction",
      "icon": "👋",
      "lines": 17,
      "scripts": [
        {
          "num_id": 1,
          "type": "phrase",
          "role": "you",
          "en": "Hi, I'm [Name] — a full-stack developer...",
          "translation": "Hai, saya [Nama] — full-stack developer..."
        }
      ]
    }
  ]
}
```

### B. Vocabulary List (Phase 1)
44+ developer-specific terms including:
- full-stack, scalable, deploy, automate, pipeline
- architecture, refactor, bottleneck, over-engineering
- end-to-end, ship fast, test coverage, code review
- pull request, merge conflict, hotfix, rollback

### C. Free Talk Topics
1. Introduce yourself as a full-stack developer
2. Describe your best project
3. Explain a technical concept to a non-technical person
4. Describe your ideal remote work setup
5. Talk about a challenge you solved recently
6. Discuss the future of AI in software development

---

*Document created by Cecep Saeful Azhar Hidaya, ST*
*FathForce Academy — 2026*
