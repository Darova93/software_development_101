import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
const scriptTag = document.createElement('script')
const metaTag = document.createElement('meta')
scriptTag.src = "https://apis.google.com/js/platform.js";
scriptTag.async = true;
scriptTag.defer = true;
metaTag.name = "google-signin-client_id";
metaTag.content = "349040231335-se4eve4roq1tmkvoi3k2b0ddkp87mhfg.apps.googleusercontent.com";
document.getElementsByTagName("head")[0].appendChild(scriptTag);
document.getElementsByTagName("head")[0].appendChild(metaTag);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
