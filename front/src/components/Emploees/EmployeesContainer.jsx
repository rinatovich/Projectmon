import React from 'react';
import {connect} from 'react-redux';
import Emploees from "./Emploees";
import {compose} from "redux";
import {employeeReducer, requestEmployee, requestPersons, setCurrentPage} from "../../redux/persons-reducer";
import PreloaderInpage from "../ui-components/Preloader/Preloader-inpage";
import {getCurrentPage, getTotalEmployeesCount} from "../../redux/persons-selector";


class EmployeesContainer extends React.Component {
    componentDidMount() {
        this.props.getEmployees(this.props.currentPage, this.props.pageSize);
    }
    onPageChanged = (pageNumber) => {
        this.props.getEmployees(pageNumber, this.props.pageSize);
    }
    render (){
        return (
            <div>
                {
                    // this.props.isFetching ? <PreloaderInpage/> :
                    <Emploees
                        totalUsersCount={this.props.totalEmployeesCount}
                        currentPage={this.props.currentPage}
                        onPageChanged={this.onPageChanged}
                        pageSize={this.props.pageSize}
                        persons={this.props.employees}
                    />
                }
            </div>
        )
    }
}


let mapStateToProps = (state) => {
    let s = state.employeeReducer;
    let p = state.personsReducer
    return {
        employees: s.employees,
        isFetching: s.isFetching,
        pageSize: s.pageSize,
        totalEmployeesCount: getTotalEmployeesCount(s),
        currentPage: getCurrentPage(p),
    }
}


export default compose(
    connect(mapStateToProps,{setCurrentPage, getEmployees: requestEmployee})
)(EmployeesContainer)