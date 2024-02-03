import style from './Projects.module.css'
import Project from "./Project/Project";
import {Link} from "react-router-dom";
import Button from "../ui-components/Buttons/Button";

let projects = [
    {
        id: 1,
        title: 'Project title',
        duration: '24 month',
        lot: '44564123',
    },
    {
        id: 2,
        title: 'Project title',
        duration: '24 month',
        lot: '44564123',
    },
    {
        id: 3,
        title: 'Project title',
        duration: '24 month',
        lot: '44564123',
    },
    {
        id: 4,
        title: 'Project title',
        duration: '24 month',
        lot: '44564123',
    },
]


export default function Projects(){

    let personsWrapper = projects.map((p)=>{
        return <Project key={p.id} title={p.title} duration={p.duration} lot={p.lot} />
    })
    return (
        <div>
            {personsWrapper}
            <Button to={'/'} text={'На главную'} />
        </div>
    )
}