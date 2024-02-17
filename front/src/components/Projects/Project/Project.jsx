import style from './Project.module.css'
import {NavLink} from "react-router-dom";

export default function Project(props){
    return (
        <div className={style.personsContainer}>
            <div className={style.personImageContainer}>
                <img className={style.personImage} src="https://i.pinimg.com/originals/d5/b0/4c/d5b04cc3dcd8c17702549ebc5f1acf1a.png" alt="person"/>
            </div>
            <div>
                <div className="name">
                    <strong>Название проекта: </strong>
                    {props.project.title? <NavLink to={`/projects/${props.project.id}`}>{props.project.title} </NavLink> : ''}
                </div>
                {
                    props.project.start_date ?
                        <div className="dateOfBirth">
                            <strong>Дата начала: </strong>
                            <sapn>{props.project.start_date}</sapn>
                        </div>: ''
                }
                {
                    props.project.end_date ?
                        <div className="age">
                            <strong>Дата окончания: </strong>
                            <sapn>{props.project.end_date}</sapn>
                        </div> :
                        <div className="age">
                            <strong>Дата окончания: </strong>
                            <sapn>Не определена</sapn>
                        </div>
                }
                <div className="contacts">
                    {
                        props.project.status?
                            <div>
                                <strong>Статус: </strong>
                                <span>{props.project.status}</span>
                            </div>:''
                    }
                </div>
            </div>
        </div>
    )
}