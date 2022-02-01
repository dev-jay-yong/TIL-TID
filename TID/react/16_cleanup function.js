import {useState, useEffect} from "react";

function App(){
    const [showing, setShowing] = useState(false);
    const onClick = () => setShowing((prev) => !prev);

    function CelanUpFunction(){
        console.log("destroyed (:")
    }

    function Hello(){
        function biFn(){
            console.log("bye :(")
        }
        function hiFn(){
            console.log("created :)");
            return biFn;
        }
        useEffect (()=> {
            console.log("created :)");
            return () => {
                console.log("buy :(")
            }
        })

        // useEffect(hiFn, [])
        
        return <h1>Hello</h1>
    }

    return (
        <div>
            <button onClick={onClick}>
                {showing ? "Hide" : "Show"}
            </button>
            {showing ? <Hello />: null}
        </div>
    )

}

export default App
