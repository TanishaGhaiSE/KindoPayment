School Trip System (Frontend - React)
This is the frontend application for the School Trip Registration & Payment System, built using React. It communicates with a FastAPI backend to manage trips, registrations, and payments.


Tech Stack
React (CRA or Vite)
Axios (API calls)
JavaScript (ES6+)
CSS / Basic styling (Tailwind optional)


Architecture
src/
│
├── api/              # API layer (Axios clients)
├── components/       # Reusable UI components
│   ├── common/
│   ├── registration/
│   ├── payment/
│   ├── trips/
│
├── pages/            # Page-level components
├── App.js
├── index.js

Install Dependencies
npm install

Start Server
npm start

Open Application
http://localhost:3000

Backend Running at 
http://localhost:8000

Update baseURL
src/api/client.js
