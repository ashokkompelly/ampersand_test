import { useEffect, useState } from "react";
import API from "./services/api";
import "./App.css";

import UploadForm from "./components/UploadForm";
import PnlTable from "./components/PnlTable";

function App() {
  const [pnlData, setPnlData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const loadPnl = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await API.get("/pnl");
      setPnlData(response.data);
    } catch (err) {
      setPnlData([]);
      setError("Upload a CSV file first or start the backend server.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadPnl();
  }, []);

  const totalPnl = pnlData.reduce((total, row) => total + Number(row.pnl), 0);
  const totalStrategies = pnlData.length;

  return (
    <div className="app-shell">
      <header className="hero-card">
        <div className="hero-copy">
          <p className="eyebrow">Trade P&L Dashboard</p>
          <h1>Track strategy profit and loss</h1>
          <p>
            Upload your trades CSV to display a clean, card-based summary of
            strategy P&L and performance metrics.
          </p>
        </div>

        <div className="hero-actions">
          <UploadForm onUploadSuccess={loadPnl} />
        </div>
      </header>

      <section className="stats-grid">
        <div className="metric-card">
          <p className="metric-label">Strategies</p>
          <p className="metric-value">{totalStrategies}</p>
        </div>
        <div className="metric-card">
          <p className="metric-label">Total P&L</p>
          <p className="metric-value">{totalPnl.toFixed(2)}</p>
        </div>
        <div className="metric-card">
          <p className="metric-label">Last updated</p>
          <p className="metric-value">{new Date().toLocaleTimeString()}</p>
        </div>
      </section>

      <main className="panel-card">
        <div className="panel-header">
          <div>
            <h2>Strategy summary</h2>
            <p>Results refresh automatically after each upload.</p>
          </div>
        </div>

        {loading ? (
          <div className="info-message">Loading results…</div>
        ) : error ? (
          <div className="info-message">{error}</div>
        ) : pnlData && pnlData.length > 0 ? (
          <PnlTable data={pnlData} />
        ) : (
          <div className="info-message">
            No results yet. Upload a CSV file to display strategy P&L.
          </div>
        )}
      </main>
    </div>
  );
}

export default App;