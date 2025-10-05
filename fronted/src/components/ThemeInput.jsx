import {useState, useEffect} from "react"

function ThemeInput({onSubmit}) {
    const [theme, setTheme] = useState("");
    const [error, setError] = useState("");
    const [difficulty, setDifficulty] = useState("medium");
    const [storyLength, setStoryLength] = useState("short");
    const [character, setCharacter] = useState("");
    const [isAdvancedMode, setIsAdvancedMode] = useState(false);

    const randomThemes = [
        "🏴☠️ Pirate treasure hunt", "🚀 Space station rescue", "🏰 Medieval dragon quest",
        "🌋 Volcanic island survival", "🧙♂️ Wizard academy mystery", "🦖 Dinosaur time travel",
        "🏜️ Desert oasis adventure", "🌊 Underwater city exploration", "🎪 Magical circus escape",
        "🏔️ Mountain climbing expedition", "🕵️ Detective noir mystery", "🤖 Robot rebellion"
    ];

    const generateRandomTheme = () => {
        const randomTheme = randomThemes[Math.floor(Math.random() * randomThemes.length)];
        setTheme(randomTheme);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!theme.trim()) {
            setError("Please enter a theme name");
            return;
        }

        const storyConfig = {
            theme: theme.trim(),
            difficulty,
            length: storyLength,
            character: character.trim() || "adventurer"
        };

        onSubmit(storyConfig.theme);
    };

    return <div className="theme-input-container">
        <div className="adventure-banner">
            <h2>🏰 Generate Your Epic Adventure 🐉</h2>
            <p>🗺️ Choose your realm and begin your legendary quest! ⚔️</p>
        </div>

        <form onSubmit={handleSubmit}>
            {/* Main Theme Input */}
            <div className="input-group">
                <label className="input-label">🎨 Adventure Theme</label>
                <div className="theme-input-wrapper">
                    <input
                        type="text"
                        value={theme}
                        onChange={(e) => setTheme(e.target.value)}
                        placeholder="Enter your epic adventure theme..."
                        className={error ? 'error' : ''}
                    />
                    <button type="button" className="random-btn" onClick={generateRandomTheme}>
                        🎲 Random
                    </button>
                </div>
                {error && <p className="error-text">⚠️ {error}</p>}
            </div>

            {/* Character Input */}
            <div className="input-group">
                <label className="input-label">🧙♂️ Your Character (Optional)</label>
                <input
                    type="text"
                    value={character}
                    onChange={(e) => setCharacter(e.target.value)}
                    placeholder="knight, wizard, pirate captain, space explorer..."
                    className="character-input"
                />
            </div>

            {/* Advanced Options Toggle */}
            <div className="advanced-toggle">
                <button 
                    type="button" 
                    className="toggle-btn"
                    onClick={() => setIsAdvancedMode(!isAdvancedMode)}
                >
                    ⚙️ {isAdvancedMode ? 'Hide' : 'Show'} Advanced Options
                </button>
            </div>

            {/* Advanced Options */}
            {isAdvancedMode && (
                <div className="advanced-options">
                    <div className="option-row">
                        <div className="option-group">
                            <label className="input-label">🎯 Difficulty Level</label>
                            <select value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
                                <option value="easy">😊 Easy - Simple choices</option>
                                <option value="medium">🤔 Medium - Balanced challenge</option>
                                <option value="hard">😤 Hard - Complex decisions</option>
                                <option value="nightmare">💀 Nightmare - Extreme difficulty</option>
                            </select>
                        </div>
                        
                        <div className="option-group">
                            <label className="input-label">📜 Story Length</label>
                            <select value={storyLength} onChange={(e) => setStoryLength(e.target.value)}>
                                <option value="short">⚡ Short - Quick adventure</option>
                                <option value="medium">🏃 Medium - Standard quest</option>
                                <option value="long">🏔️ Long - Epic journey</option>
                            </select>
                        </div>
                    </div>
                </div>
            )}

            <button type="submit" className='generate-btn'>
                🎆 Generate Epic Story 🎆
            </button>
        </form>
        
        <div className="adventure-examples">
            <h3>🎯 Popular Adventure Themes:</h3>
            <div className="theme-suggestions">
                <span className="theme-tag" onClick={() => setTheme('pirates')}>🏴☠️ Pirates</span>
                <span className="theme-tag" onClick={() => setTheme('space exploration')}>🚀 Space</span>
                <span className="theme-tag" onClick={() => setTheme('medieval fantasy')}>⚔️ Medieval</span>
                <span className="theme-tag" onClick={() => setTheme('jungle adventure')}>🌴 Jungle</span>
                <span className="theme-tag" onClick={() => setTheme('underwater quest')}>🌊 Ocean</span>
                <span className="theme-tag" onClick={() => setTheme('dragon slayer')}>🐉 Dragons</span>
                <span className="theme-tag" onClick={() => setTheme('zombie apocalypse')}>🧟 Zombies</span>
                <span className="theme-tag" onClick={() => setTheme('time travel')}>⏰ Time Travel</span>
            </div>
        </div>

        {/* Story Stats Preview */}
        <div className="story-preview">
            <h4>📊 Your Adventure Preview:</h4>
            <div className="preview-stats">
                <span className="stat">🎨 Theme: {theme || 'Not selected'}</span>
                <span className="stat">🧙♂️ Character: {character || 'Adventurer'}</span>
                {isAdvancedMode && (
                    <>
                        <span className="stat">🎯 Difficulty: {difficulty}</span>
                        <span className="stat">📜 Length: {storyLength}</span>
                    </>
                )}
            </div>
        </div>
    </div>
}

export default ThemeInput;