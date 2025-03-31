import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;

import { useEffect } from 'react';

function ErrorBoundary({ children }) {
  useEffect(() => {
    window.onerror = (msg) => {
      console.error("Global error:", msg);
      alert("An unexpected error occurred. Please try again.");
    };
    return () => { window.onerror = null; };
  }, []);
  return children;
}

function AppWrapper() {
  """Wrap App with analytics provider."""
  return (
    <ErrorBoundary>
      <AnalyticsProvider>
        <App />
      </AnalyticsProvider>
    </ErrorBoundary>
  );
}

import { useEffect } from 'react';

function ErrorBoundary({ children }) {
  useEffect(() => {
    window.onerror = (msg) => {
      console.error("Global error:", msg);
      alert("An unexpected error occurred. Please try again.");
    };
    return () => { window.onerror = null; };
  }, []);
  return children;
}

function AppWrapper() {
  """Wrap App with analytics provider."""
  return (
    <ErrorBoundary>
      <AnalyticsProvider>
        <App />
      </AnalyticsProvider>
    </ErrorBoundary>
  );
}
