import style from './Person.module.css'

export default function Person(props){
    return (
        <div className={style.personsContainer}>
            <div className={style.personImageContainer}>
                <img className={style.personImage} src="https://i.pinimg.com/originals/d5/b0/4c/d5b04cc3dcd8c17702549ebc5f1acf1a.png" alt="person"/>
            </div>
            <div>
                <div className="name">
                    <strong>Ф.И.О: </strong>
                    {props.person.first_name? <span>{props.person.first_name} </span> : ''}
                    {props.person.last_name? <span>{props.person.last_name} </span> : ''}
                    {props.person.middle_name? <span>{props.person.middle_name} </span> : ''}
                </div>
                {
                    props.person.date_of_birth ?
                        <div className="dateOfBirth">
                            <strong>Дата рождения: </strong>
                            <sapn>{props.person.date_of_birth}</sapn>
                        </div>: ''
                }
                {
                    props.person.age ?
                        <div className="age">
                            <strong>Возраст: </strong>
                            <sapn>{props.person.age}</sapn>
                        </div>: ''
                }
                <div className="contacts">
                    {
                        props.person.email?
                            <div>
                                <strong>Email: </strong>
                                <span>{props.person.email}</span>
                            </div>:''
                    }
                    {
                        props.person.phone_number?
                            <div>
                                <strong>Телефон: </strong>
                                <span>{props.person.phone_number}</span>
                            </div>:''
                    }
                </div>
            </div>
        </div>
    )
}