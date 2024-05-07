import logo from "../logo.png";

const TopNav = () => {
  return (
    <>
      <div style={{display:"flex", color:"white", marginLeft:"2rem"}}>
        <img src={logo} className="App-logo" alt="logo" />
        <p>NavBar Working!</p>
      </div>
    </>
  );
};

export default TopNav;
