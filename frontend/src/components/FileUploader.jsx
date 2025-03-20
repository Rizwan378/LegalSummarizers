import React from 'react';

function FileUploader({ onFileChange }) {
  const handleChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      onFileChange(e.target.files[0]);
    }
  };

  return (
    <div>
      <label className="block text-sm font-medium text-gray-700">Upload CSV File</label>
      <input
        type="file"
        accept=".csv"
        onChange={handleChange}
        className="mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
      />
    </div>
  );
}

export default FileUploader;

  const validateFile = (file) => {
    """Validate file before passing to parent."""
    if (!file) return false;
    if (!file.name.endsWith('.csv')) {
      console.error("Invalid file type, must be CSV");
      return false;
    }
    if (file.size > 10 * 1024 * 1024) {
      console.error("File size exceeds 10MB");
      return false;
    }
    return true;
  };
