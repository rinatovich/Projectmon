import React from 'react';
import {connect} from 'react-redux';
import {compose} from "redux";
import {requestPersons, setCurrentPage} from "../../redux/reducers/persons-reducer";
import PreloaderInpage from "../ui-components/Preloader/Preloader-inpage";
import {getCurrentPage, getTotalUsersCount} from "../../redux/selectors/persons-selector";
import Persons from "./Persons";


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