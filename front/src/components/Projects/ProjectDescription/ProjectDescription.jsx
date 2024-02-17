import React from 'react';
const ProjectsDescription = (props) => {
    return (
        <div>
            <h2>{props.project.title}</h2>
            <h2>{props.project.start_date}</h2>
            <h2>{props.project.end_date}</h2>
            <h2>{props.project.status}</h2>
            <h2>{props.project.end_date}</h2>
            <h2>Этапов: </h2>
            <h2>{props.project.stages.length}</h2>
        </div>
    );
};

export default ProjectsDescription;

