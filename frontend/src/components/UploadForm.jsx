import { useState } from "react";
import API from "../services/api";

function UploadForm({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    setUploading(true);
    setMessage("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      await API.post("/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage("Upload successful.");
      onUploadSuccess();
    } catch (err) {
      setMessage("Upload failed. Please try again.", err);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="upload-form">
      <label className="file-selector">
        <span>{file ? file.name : "Choose a CSV file"}</span>
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </label>

      <button
        type="button"
        className="button-primary"
        onClick={handleUpload}
        disabled={!file || uploading}
      >
        {uploading ? "Uploading..." : "Upload"}
      </button>

      {message && <div className="upload-message">{message}</div>}
    </div>
  );
}

export default UploadForm;