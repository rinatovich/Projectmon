import './App.css';
import {Outlet} from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import Sidebar from "./components/Sidebar/Sidebar";


function App() {
  return (
    <div className="App">
        <Navbar />
        <Sidebar />
        <div id="main">
            <Outlet />
        </div>
    </div>
  );
}

export default App;
