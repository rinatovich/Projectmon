import style from './Sidebar.module.css'
import {NavLink} from "react-router-dom";

export default function Sidebar(props){
    const sidebarMenu = [
        {
            id: 1,
            title: 'Entities',
            link: '/persons'
        },
        {
            id: 2,
            title: 'Projects',
            link: '/projects'
        },
        {
            id: 3,
            title: 'Emploees',
            link: '/employees'
        },
    ]
    return (
        <aside className={style.sidebar}>
            <ul className={style.sidebarList}>
                {sidebarMenu.map((s)=>{
                    return (
                        <li key={s.id}>
                            <NavLink className={({ isActive, isPending }) =>
                                isPending ? "pending" : isActive ? style.active : ""
                            } to={s.link}>
                                {s.title}
                            </NavLink>
                        </li>
                    )
                })}
            </ul>
        </aside>
    )}