import {useState, useEffect} from "react"
import {useNavigate} from "react-router-dom";
import axios from "axios";
import ThemeInput from "./ThemeInput.jsx";
import LoadingStatus from "./LoadingStatus.jsx";
import {API_BASE_URL} from "../util.js";


function StoryGenerator() {
    const navigate = useNavigate()
    const [theme, setTheme] = useState("")
    const [jobId, setJobId] = useState(null)
    const [jobStatus, setJobStatus] = useState(null)
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        let pollInterval;

        if (jobId && (jobStatus === "pending" || jobStatus === "in_progress")) {
            pollInterval = setInterval(() => {
                pollJobStatus(jobId)
            }, 2000) // Poll every 2 seconds for faster updates
        }

        return () => {
            if (pollInterval) {
                clearInterval(pollInterval)
            }
        }
    }, [jobId, jobStatus])

    const generateStory = async (theme) => {
        setLoading(true)
        setError(null)
        setTheme(theme)

        try {
            const response = await axios.post(`${API_BASE_URL}/story/create`, {theme})
            const {job_id, status} = response.data
            setJobId(job_id)
            setJobStatus(status)

            // Start polling immediately
            setTimeout(() => pollJobStatus(job_id), 1000)
        } catch (e) {
            setLoading(false)
            setError(`Failed to generate story: ${e.response?.data?.detail || e.message}`)
        }
    }

    const pollJobStatus = async (id) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/job/${id}`)
            const {status, story_id, error: jobError} = response.data
            console.log('Job status:', status, 'Story ID:', story_id)
            setJobStatus(status)

            if (status === "completed" && story_id) {
                setLoading(false)
                navigate(`/story/${story_id}`)
            } else if (status === "failed" || jobError) {
                setError(jobError || "Failed to generate story")
                setLoading(false)
            }
        } catch (e) {
            console.error('Polling error:', e)
            if (e.response?.status !== 404) {
                setError(`Failed to check story status: ${e.response?.data?.detail || e.message}`)
                setLoading(false)
            }
        }
    }



    const reset = () => {
        setJobId(null)
        setJobStatus(null)
        setError(null)
        setTheme("")
        setLoading(false)
    }

    return <div className="story-generator">
        {error && <div className="error-message animate-bounce">
            <p>🚫 {error}</p>
            <button onClick={reset} className="retry-btn">🔄 Try Again</button>
        </div>}

        {!jobId && !error && !loading && <ThemeInput onSubmit={generateStory}/>}

        {loading && <LoadingStatus theme={theme} />}
    </div>
}

export default StoryGenerator