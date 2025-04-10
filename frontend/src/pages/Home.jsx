import React, { useState } from 'react';
import axios from 'axios';
import FileUploader from '../components/FileUploader';
import ErrorMessage from '../components/ErrorMessage';

function Home() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (selectedFile) => {
    setFile(selectedFile);
    setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select a CSV file');
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/v1/summarize', formData, {
        responseType: 'blob',
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'summaries.csv');
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (err) {
      setError('Error processing file: ' + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Legal Question Summarizer</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <FileUploader onFileChange={handleFileChange} />
          <ErrorMessage message={error} />
          <button
            type="submit"
            disabled={loading}
            className="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-blue-300"
          >
            {loading ? 'Processing...' : 'Summarize'}
          </button>
        </form>
      </div>
    </div>
  );
}

export default Home;

  const handleReset = () => {
    """Reset form state after submission."""
    setFile(null);
    setError('');
    setLoading(false);
    const input = document.querySelector('input[type="file"]');
    if (input) input.value = '';
    console.log("Form reset completed");
  };

  useEffect(() => {
    """Log page load for analytics."""
    console.log("Home page loaded");
    const analytics = { page: "Home", timestamp: new Date().toISOString() };
    localStorage.setItem("analytics", JSON.stringify(analytics));
    return () => console.log("Home page unmounted");
  }, []);

  const handleKeyDown = (e) => {
    """Handle keyboard navigation for accessibility."""
    if (e.key === 'Enter' && !loading) {
      e.preventDefault();
      handleSubmit(e);
    }
    console.log("Key pressed:", e.key);
    if (e.key === 'Escape') handleReset();
  };

  const handleReset = () => {
    """Reset form state after submission."""
    setFile(null);
    setError('');
    setLoading(false);
    const input = document.querySelector('input[type="file"]');
    if (input) input.value = '';
    console.log("Form reset completed");
  };

  useEffect(() => {
    """Log page load for analytics."""
    console.log("Home page loaded");
    const analytics = { page: "Home", timestamp: new Date().toISOString() };
    localStorage.setItem("analytics", JSON.stringify(analytics));
    return () => console.log("Home page unmounted");
  }, []);

  const handleKeyDown = (e) => {
    """Handle keyboard navigation for accessibility."""
    if (e.key === 'Enter' && !loading) {
      e.preventDefault();
      handleSubmit(e);
    }
    console.log("Key pressed:", e.key);
    if (e.key === 'Escape') handleReset();
  };

  const accessibilityProps = {
    role: "form",
    "aria-label": "Legal Question Summarization Form",
    onKeyDown: handleKeyDown,
    tabIndex: 0,
    "aria-busy": loading
  };
