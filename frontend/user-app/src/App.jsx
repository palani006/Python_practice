import "./App.css";
import Header from "./components/Header";
import StudentList from "./components/StudentList";

export default function App() {
  return (
    <div className="sma-app">
      <Header />
      <main className="sma-main">
        <StudentList />
      </main>
    </div>
  );
}
