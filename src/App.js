import logo from './logo.svg';
import './App.css';
import TopNav from './component/topNav';
import Content from './component/Content';
import Footer from './component/footer';
function App() {
  return (
    <div className="App">
      <TopNav/>
      <Content/>
      <Footer/>
    </div>
  );
}

export default App;
