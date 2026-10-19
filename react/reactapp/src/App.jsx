import Header from "./components/Header"
import './App.css'
import MyBanner from "./components/MyBanner"
import Maincontent from "./components/Maincontent"
import OurForms from "./components/OurForms"
import Myfooter from "./components/Myfooter"




function App(){
  return (
    <> 
      <div className="container1">
        <Header />
        <MyBanner />
        <Maincontent />
        <OurForms />
        <Myfooter />
      </div>
      
    </>
  )
}
export default App