# 🏰 Adventure Story Generator 🐉

An AI-powered interactive story generator that creates unique choose-your-own-adventure stories with beautiful animations and customizable gameplay options.

![Adventure Story Generator](https://img.shields.io/badge/Adventure-Story%20Generator-brightgreen) ![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-blue) ![React](https://img.shields.io/badge/React-18.2.0-61dafb) ![AI](https://img.shields.io/badge/AI-Groq%20LLaMA-orange)

## 🌟 Features

### 🎮 Interactive Storytelling
- **AI-Generated Stories**: Powered by Groq LLaMA 3.1 for unique narratives
- **Branching Paths**: Every choice leads to different outcomes
- **Multiple Endings**: Win, lose, or discover secret paths
- **Real-time Generation**: Stories created on-demand, not pre-written

### 🎨 Customization Options
- **🎲 Random Theme Generator**: 12+ epic adventure themes
- **🧙♂️ Character Creation**: Customize your protagonist
- **🎯 Difficulty Levels**: Easy → Nightmare mode
- **📜 Story Length**: Quick adventures → Epic journeys
- **⚙️ Advanced Settings**: Fine-tune your experience

### 🌈 Beautiful UI/UX
- **Colorful Animations**: Gradient backgrounds and smooth transitions
- **Adventure Theme**: Emojis and medieval/fantasy styling
- **Mobile Responsive**: Works on all devices
- **Interactive Elements**: Hover effects and loading animations

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- Groq API Key ([Get one here](https://console.groq.com/))

### Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
echo "DATABASE_URL=sqlite:///./database.db
API_PREFIX=/api
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
GROQ_API_KEY=your_groq_api_key_here" > .env

# Start the server
python main.py
```

### Frontend Setup
```bash
cd fronted
npm install
npm run dev
```

Visit `http://localhost:5173` to start creating adventures! 🎆

## 🏗️ Architecture

### Backend (FastAPI)
```
backend/
├── core/           # Configuration and AI adapter
├── models/         # SQLAlchemy database models
├── routers/        # API endpoints
├── schemas/        # Pydantic models
└── db/            # Database configuration
```

### Frontend (React)
```
fronted/
├── src/
│   ├── components/    # React components
│   ├── App.jsx       # Main application
│   └── util.js       # API configuration
└── public/           # Static assets
```

## 🎯 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/story/create` | Generate new adventure story |
| `GET` | `/api/job/{job_id}` | Check story generation status |
| `GET` | `/api/story/{story_id}/completed` | Get complete story with all paths |

## 🎨 Theme Examples

- 🏴☠️ **Pirates**: Treasure hunts and sea battles
- 🚀 **Space**: Galactic exploration and alien encounters  
- ⚔️ **Medieval**: Knights, dragons, and castle sieges
- 🌊 **Ocean**: Underwater cities and sea creatures
- 🧟 **Zombies**: Apocalypse survival adventures
- ⏰ **Time Travel**: Paradoxes and historical adventures

## 🛠️ Tech Stack

**Backend:**
- **FastAPI** - High-performance Python web framework
- **SQLAlchemy** - Database ORM
- **Groq LLaMA 3.1** - Advanced AI language model
- **SQLite** - Lightweight database
- **Pydantic** - Data validation

**Frontend:**
- **React** - Modern UI library
- **Axios** - HTTP client
- **CSS3** - Advanced styling with gradients and animations
- **Responsive Design** - Mobile-first approach

## 🎮 How It Works

1. **Choose Theme** 🎨 → Select your adventure world
2. **Customize Settings** ⚙️ → Set difficulty, length, character
3. **AI Generation** 🤖 → LLaMA creates branching story
4. **Interactive Play** 🎯 → Make choices that shape the narrative
5. **Multiple Endings** 🏆 → Discover different outcomes

## 🔧 Configuration

### Environment Variables
```env
DATABASE_URL=sqlite:///./database.db
API_PREFIX=/api
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
GROQ_API_KEY=your_groq_api_key_here
```

## 📱 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/800x400/667eea/ffffff?text=Epic+Adventure+Generator)

### Story Generation
![Story Generation](https://via.placeholder.com/800x400/764ba2/ffffff?text=AI+Story+Creation)

### Interactive Gameplay
![Interactive Gameplay](https://via.placeholder.com/800x400/48cae4/ffffff?text=Choose+Your+Path)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing fast AI inference
- **FastAPI** for the excellent web framework
- **React** community for amazing tools
- **Adventure game** enthusiasts for inspiration

## 🐛 Troubleshooting

**Frontend Connection Issues**
```bash
# Verify API URL in fronted/src/util.js
export const API_BASE_URL = "http://localhost:8000/api"
```
