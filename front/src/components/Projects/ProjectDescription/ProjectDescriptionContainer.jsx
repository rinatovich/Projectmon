import React, {useEffect} from 'react';
import {connect} from 'react-redux';
import {compose} from "redux";
import ProjectsDescription from "./ProjectDescription";
import PreloaderInpage from "../../ui-components/Preloader/Preloader-inpage";
import {requestProjectDescription} from "../../../redux/reducers/projects-reducer";
import {useParams} from "react-router-dom";


const ProjectDescriptionContainer = ({project, isFetching, getProjectDescription,}) => {
    const { id } = useParams();
    useEffect(() => {
        getProjectDescription(id); // Передайте id вместо this.props.match.params.id
    }, [])

    return (<div>
            {isFetching ? <PreloaderInpage/> : <ProjectsDescription project={project}/>}
        </div>);
};

const mapStateToProps = (state) => {
    const s = state.projectsReducer;
    return {
        project: s.currentProjectDescription, isFetching: s.isFetching,
    };
};

export default compose(connect(mapStateToProps, {getProjectDescription: requestProjectDescription}))(ProjectDescriptionContainer);