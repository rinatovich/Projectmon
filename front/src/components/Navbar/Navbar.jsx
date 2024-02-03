import style from './Navbar.module.css'
import {Link} from "react-router-dom";

export default function Navbar(props){
    return (
        <nav className={style.navbar}>
            <div className={style.brand}>
                Projectmon
            </div>
            <ul className={style.navList}>
                <li>
                    <Link to={`/persons`}>Persons</Link>
                </li>
                <li>
                    <Link to={`/projects`}>Projects</Link>
                </li>
                <li>
                    <Link to={`/profile`}>Profile</Link>
                </li>
                <li>
                    <Link to={`/about`}>About</Link>
                </li>
            </ul>
        </nav>
    )}