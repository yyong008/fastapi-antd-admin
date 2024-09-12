import "./styles/global.css"
import "./styles/tailwind.css"

import App from './App.tsx'
import { createRoot } from 'react-dom/client'

createRoot(document.getElementById('root')!).render(
  <>
    <App />
  </>,
)
