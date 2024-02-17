import React from 'react';
import {connect} from 'react-redux';
import {compose} from "redux";
import Projects from "./Projects";
import PreloaderInpage from "../ui-components/Preloader/Preloader-inpage";
import {requestProjects, setProjectsCurrentPage} from "../../redux/reducers/projects-reducer";


class ProjectsContainer extends React.Component {
    componentDidMount() {
        this.props.getProjects(this.props.currentPage, this.props.projectsPageSize);
    }
    onPageChanged = (pageNumber) => {
        this.props.getProjects(pageNumber, this.props.projectsPageSize);
    }
    render (){
        return (
            <div>
                {
                    this.props.isFetching ? <PreloaderInpage/> :
                        <Projects
                            totalProjectsCount={this.props.totalProjectsCount}
                            currentPage={this.props.currentPage}
                            onPageChanged={this.onPageChanged}
                            pageSize={this.props.projectsPageSize}
                            projects={this.props.projects}
                        />
                }
            </div>
        )
    }
}


let mapStateToProps = (state) => {
    let s = state.projectsReducer;
    return {
        projects: s.projects,
        isFetching: s.isFetching,
        projectsPageSize: s.projectsPageSize,
        totalProjectsCount: s.totalProjectsCount,
        currentPage: s.projectsCurrentPage,
    }
}


export default compose(
    connect(mapStateToProps,{setProjectsCurrentPage, getProjects: requestProjects})
)(ProjectsContainer)