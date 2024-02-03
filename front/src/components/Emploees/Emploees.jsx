import style from './Employees.module.css'
import Employee from "./Person/Employee";
import Button from "../ui-components/Buttons/Button";
import Paginator from "../ui-components/Paginator/Paginator";

export default function Emploees(props){
    let employeesList;
    let pagesCount = Math.ceil(props.totalUsersCount / props.pageSize);
    let pages = [];
    for (let i = 1; i <= pagesCount; i++) {
        pages.push(i);
    }
    employeesList = props.persons.map((p) => {
            return (
                <Employee
                    key={p.id}
                    person={p}
                />
            );
        });
    return (
        <div>
            <div className={style.persons}>
                {employeesList}
            </div>
            <div className={style.paginatorGroup}>
                <Paginator currentPage={props.currentPage} pages={pages} onPageChanged={props.onPageChanged}/>
            </div>
            <div className={style.buttonGroup}>
                <Button to={'/employees/create'} text={'Создать новую персону'} />
                <Button to={'/'} text={'На главную'} />
            </div>
        </div>
    )
}