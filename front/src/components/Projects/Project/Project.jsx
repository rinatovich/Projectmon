import style from './Project.module.css'

export default function Project(props){
    return (
        <div className={style.projectContainer}>
            <div className={style.projectImgContainer}>
                <img className={style.projectImg} src="https://cdn-icons-png.flaticon.com/512/5234/5234180.png" alt="person"/>
            </div>
            <div>
                <div>{props.title}</div>
                <div>{props.duration}</div>
                <div>{props.lot}</div>
            </div>
        </div>
    )
}