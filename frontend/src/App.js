import React, { useState } from "react";
import "./App.css";

import ScoreCard from "./components/ScoreCard";
import RadarChartBox from "./components/RadarChartBox";
import InsightBox from "./components/InsightBox";

function App() {
  const [username, setUsername] = useState("");
  const [role, setRole] = useState("frontend");
  const [mode, setMode] = useState("student"); // 🔥 NEW
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeProfile = async () => {
    if (!username) return;

    setLoading(true);
    setData(null);

    try {
      const res = await fetch(
        `http://127.0.0.1:8000/analyze/${username}?role=${role}&mode=${mode}`
      );
      const result = await res.json();
      setData(result);
    } catch (err) {
      console.error(err);
      alert("Error fetching data");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      {/* 🔥 HEADER */}
      <h1>GitHub Recruitability Analyzer</h1>

      {/* 🔍 INPUT SECTION */}
      <div className="input-section">
        <input
          type="text"
          placeholder="Enter GitHub username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        {/* ROLE */}
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="frontend">Frontend</option>
          <option value="backend">Backend</option>
          <option value="fullstack">Fullstack</option>
          <option value="datascience">Data Science</option>
        </select>

        {/* 🔥 MODE SELECT */}
        <select value={mode} onChange={(e) => setMode(e.target.value)}>
          <option value="student">Student Mode</option>
          <option value="recruiter">Recruiter Mode</option>
        </select>

        <button onClick={analyzeProfile}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </div>

      {/* ⏳ LOADING */}
      {loading && <div className="loader"></div>}

      {/* ===================================================== */}
      {/* 👨‍🎓 STUDENT MODE UI */}
      {/* ===================================================== */}
      {data && data.mode === "student" && (
        <div className="dashboard">

          <ScoreCard
            score={data.final_score}
            category={data.category}
          />

          <div className="chart-section">
            <RadarChartBox data={data} />
          </div>

          <div className="grid">
            <div className="card">Quality: {data.quality_score}</div>
            <div className="card">Relevance: {data.relevance_score}</div>
            <div className="card">Depth: {data.depth_score}</div>
            <div className="card">Consistency: {data.consistency_score}</div>
            <div className="card">Authenticity: {data.authenticity_score}</div>
          </div>

          <InsightBox data={data} />

          <div className="insights-container">
            <div className="strengths">
              <h3>Strengths</h3>
              {data.strengths.map((s, i) => (
                <p key={i}>✅ {s}</p>
              ))}
            </div>

            <div className="weaknesses">
              <h3>Weaknesses</h3>
              {data.weaknesses.map((w, i) => (
                <p key={i}>❌ {w}</p>
              ))}
            </div>
          </div>

        </div>
      )}

      {/* ===================================================== */}
      {/* 🧑‍💼 RECRUITER MODE UI */}
      {/* ===================================================== */}
      {data && data.mode === "recruiter" && (
        <div className="dashboard recruiter-dashboard">

          <h2 className="recruiter-score">{data.final_score}</h2>
          <p className="recruiter-category">{data.category}</p>

          <div className="recruiter-box">
            <p><strong>Hire Decision:</strong> {data.hire_decision}</p>
            <p><strong>Risk Level:</strong> {data.risk_level}</p>
            <p className="summary">{data.summary}</p>
          </div>

        </div>
      )}

    </div>
  );
}

export default App;