import { useState } from "react";
import axios from "axios";

function UploadAnnotator() {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFiles = (e) => setFiles([...e.target.files]);

  const handleUpload = async () => {
    setLoading(true);
    const formData = new FormData();
    files.forEach(file => formData.append("files", file));

    const response = await axios.post("http://localhost:8000/annotate",
      formData,
      { responseType: 'blob' }
    );

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'annotations.zip');
    document.body.appendChild(link);
    link.click();

    setLoading(false);
  };

  return (
    <div>
      <h2>Aerial Image Auto-Annotation</h2>
      <input type="file" multiple onChange={handleFiles} />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Annotate Images"}
      </button>
    </div>
  );
}

export default UploadAnnotator;