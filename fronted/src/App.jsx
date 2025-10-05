import './App.css'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import StoryLoader from "./components/StoryLoader"
import StoryGenerator from "./components/StoryGenerator.jsx";

function App() {
  return (
    <Router>
      <div className="app-container">
        <header>
          <div className="adventure-header">
            <div className="adventure-icons">🗡️⚔️🏰🐉🗺️</div>
            <h1>🌟 Epic Adventure Story Generator 🌟</h1>
            <p className="adventure-subtitle">🚀 Embark on thrilling quests and shape your destiny! 🏆</p>
          </div>
        </header>
        <main>
          <Routes>
            <Route path={"/story/:id"} element={<StoryLoader />} />
            <Route path={"/"} element={<StoryGenerator />}/>
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App