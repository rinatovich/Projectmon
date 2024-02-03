import style from "./Button.module.css";
import {Link} from "react-router-dom";


export default function Button(props){
    return(
            <Link className={style.button}  to={props.to}> {props.text}</Link>
    )
}
