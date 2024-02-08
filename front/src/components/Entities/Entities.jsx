import style from './Entities.module.css'
import Entity from "./Entity/Entity";
import Button from "../ui-components/Buttons/Button";
import Paginator from "../ui-components/Paginator/Paginator";

export default function Entities(props){
    let personsList;
    let pagesCount = Math.ceil(props.persons.count / props.pageSize);
    let pages = [];
    for (let i = 1; i <= pagesCount; i++) {
        pages.push(i);
    }
    personsList = props.persons.results.map((p) => {
            return (
                <Entity
                    key={p.id}
                    person={p}
                />
            );
        });
    return (
        <div>
            <div className={style.persons}>
                {personsList}
            </div>
            <div className={style.paginatorGroup}>
                <Paginator currentPage={props.currentPage} pages={pages} onPageChanged={props.onPageChanged}/>
            </div>
            <div className={style.buttonGroup}>
                <Button to={'/person/create'} text={'Создать новую персону'} />
                <Button to={'/'} text={'На главную'} />
            </div>
        </div>
    )
}