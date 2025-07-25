import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import Dealers from "./components/Dealers/Dealers";  // ✅ Import Dealers
import Dealer from './components/Dealers/Dealer';

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dealers" element={<Dealers />} />  {/* ✅ Dealers route */}
      <Route path="/dealer/:id" element={<Dealer />} />

    </Routes>
  );
}

export default App;
