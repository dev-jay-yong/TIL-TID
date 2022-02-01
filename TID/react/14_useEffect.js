import React from 'react';
import ReactDOM from 'react-dom';
import {useState, useEffect} from "react";

function App() {
  const [counter, setValue] = useState(0);
  const onClick = () => setValue((prev) => prev + 1);
  console.log("i run all the time");
  const iRunOnlyOnce = () => {
      console.log("call the api code")
  }
  useEffect(iRunOnlyOnce, [])

  return (
    <div>
      {/*<h1 className={styles.title}>Welcome back!</h1>*/}
      <h1> {counter} </h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
