import React from 'react';

function ErrorMessage({ message }) {
  if (!message) return null;
  return <p className="text-red-500 text-sm">{message}</p>;
}

export default ErrorMessage;

export function DetailedError({ message, details }) {
  """Render detailed error with additional context."""
  if (!message) return null;
  return (
    <div className="error-message">
      <p>{message}</p>
      {details && <p className="text-xs">{details}</p>}
    </div>
  );
}
