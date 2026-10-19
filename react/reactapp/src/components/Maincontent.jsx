
import reactlogo from '../assets/reactimg.png'
import MyCard from "./MyCard"

export default function Maincontent()  {
    const styles = {
        backgroundColor: 'white',
        color: 'blue',
        padding: '10px 30px',
        border: 'none',
        outline: 'none',
        borderRadius: '20px',
        marginTop: '20px',
        fontSize: '20px'
    }
    const styles2 = {
        backgroundColor: 'white',
        color: 'red',
        padding: '10px 30px',
        border: 'none',
        outline: 'none',
        borderRadius: '20px',
        marginTop: '20px',
        fontSize: '20px'
    }
    return (
        <div className="main grid grid-cols-2 gap-10 p-10 h-[500px]">
            <div className="content w-[400px] h-[400px] bg-sky-800 p-10"> 
                {/* <h1 className="text-2xl border border-white border-b-5 m-b-5">Main</h1> */}
                <img src={reactlogo} alt="" className='' />
                {/* <p>This section is for image to be displayed</p> */}
                {/* <button onClick={function(){alert('Welcome to ReactJs Website')} } type="button" style={styles}>Get Started</button> */}
            </div>
            {/* <div className="content" style={styles} > */}
            {/* above style is using internal css */}

            {/* below is inline css */}
            
            {/* <div className="content" style={{backgroundColor: 'orange', color:'white'}}>
                <h1 className="text-2xl border border-white border-b-5 m-b-5" > Content</h1>
                <p>This section is for details about the content</p>
                <button onClick={ () => alert('Signup to ReactJs Website for informations') } type="button" style={styles2}>Sign up</button>
            </div> */}
            <MyCard /> 
            
        </div>
    )
}