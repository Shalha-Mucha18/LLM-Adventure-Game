
function LoadingStatus({theme}) {
    const adventureMessages = [
        "🏰 Crafting your legendary tale...",
        "⚔️ Forging epic adventures...", 
        "🗺️ Mapping uncharted territories...",
        "🐉 Awakening ancient mysteries...",
        "🎆 Weaving magical destinies...",
        "🚀 Launching into the unknown..."
    ];
    
    const randomMessage = adventureMessages[Math.floor(Math.random() * adventureMessages.length)];
    
    return <div className="loading-container">
        <div className="adventure-loading">
            <h2>🎭 Generating Your Epic {theme} Adventure 🎭</h2>
            
            <div className="loading-animation">
                <div className="spinner"></div>
                <div className="adventure-icons-float">
                    <span>🗡️</span>
                    <span>🏰</span>
                    <span>🐉</span>
                    <span>✨</span>
                </div>
            </div>

            <p className="loading-info adventure-message">
                {randomMessage}
            </p>
            
            <div className="progress-dots">
                <span></span><span></span><span></span>
            </div>
        </div>
    </div>
}

export default LoadingStatus;
