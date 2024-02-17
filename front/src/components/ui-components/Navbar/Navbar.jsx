import style from './Navbar.module.css'
import {NavLink} from "react-router-dom";


let routes = [
    {
        id: 1,
        title: "Login",
        link: "/login",
    },
]

export default function Navbar(props){
    let links_array = routes.map((route) => {
        return (
            <li key={route.id}>
                <NavLink to={route.link} className={({ isActive, isPending }) =>
                    isPending ? "pending" : isActive ? style.activeLink : ""
                }>
                    {route.title}
                </NavLink>
            </li>
        );
    });
    return (
        <nav className={style.navbar}>
            <div className={style.brand}>
            </div>
            <ul className={style.navList}>
                {links_array}
            </ul>
        </nav>
    )}