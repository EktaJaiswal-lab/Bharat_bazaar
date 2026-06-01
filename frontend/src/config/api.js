import axios from 'axios';

export const API_URL =
  import.meta.env.VITE_API_URL ||
  (import.meta.env.DEV
    ? 'http://localhost:8000'
    : 'https://bharat-bazaar-vcva.onrender.com');

export const api = axios.create({
  baseURL: API_URL,
});
