import React from 'react';
import {connect} from 'react-redux';
import Persons from "./Persons";
import {compose} from "redux";
import {personsReducer, requestPersons, setCurrentPage} from "../../redux/persons-reducer";
import PreloaderInpage from "../ui-components/Preloader/Preloader-inpage";
import {getCurrentPage, getTotalUsersCount} from "../../redux/persons-selector";


class PersonsContainer extends React.Component {
    componentDidMount() {
        this.props.getPersons(this.props.currentPage, this.props.pageSize);
    }
    onPageChanged = (pageNumber) => {
        this.props.getPersons(pageNumber, this.props.pageSize);
    }
    render (){
        return (
            <div>
                {
                    this.props.isFetching ? <PreloaderInpage/> :
                    <Persons
                        totalUsersCount={this.props.totalUsersCount}
                        currentPage={this.props.currentPage}
                        onPageChanged={this.onPageChanged}
                        pageSize={this.props.pageSize}
                        persons={this.props.persons}
                    />
                }
            </div>
        )
    }
}


let mapStateToProps = (state) => {
    let s = state.personsReducer;
    return {
        persons: s.persons,
        isFetching: s.isFetching,
        pageSize: s.pageSize,
        totalUsersCount: getTotalUsersCount(s),
        currentPage: getCurrentPage(s),
    }
}


export default compose(
    connect(mapStateToProps,{setCurrentPage, getPersons: requestPersons})
)(PersonsContainer)