import style from './Projects.module.css'
import Project from "./Project/Project";
import Button from "../ui-components/Buttons/Button";
import Paginator from "../ui-components/Paginator/Paginator";

export default function Projects(props){
    let projectsList;
    let pagesCount = Math.ceil(props.totalProjectsCount / props.pageSize);
    let pages = [];
    for (let i = 1; i <= pagesCount; i++) {
        pages.push(i);
    }
    projectsList = props.projects.results.map((p) => {
            return (
                <Project
                    key={p.id}
                    project={p}
                />
            );
        });
    return (
        <div>
            <div className={style.persons}>
                {projectsList}
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