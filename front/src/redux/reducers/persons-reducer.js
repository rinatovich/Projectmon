import {employeeAPI, personsAPI} from "../api/api";

const SET_PERSONS = 'SET_PERSONS';
const TOGGLE_IS_FETCHING = 'TOGGLE_IS_FETCHING';
const SET_CURRENT_PAGE = 'SET_CURRENT_PAGE';
const SET_TOTAL_USERS_COUNT = 'SET_TOTAL_USERS_COUNT';
const SET_TOTAL_EMPLOYEES_COUNT = 'SET_TOTAL_EMPLOYEES_COUNT';
const SET_EMPLOYEES = 'SET_EMPLOYEES';

let initialState = {
    persons: [{
        id: 1,
        first_name: 'Valiaxmad',
        last_name: 'Maxamatov',
        age: '24',
        email: 'mvrinatovicso@gmail.com',
        phone_number: '+998 93 560 24 99',
        job_title: 'Project manager',
        company: 'LLC VALSTATEX'
    },
    {
        id: 2,
        first_name: 'Temurbek',
        last_name: 'Toshbekov',
        age: '30',
        email: 'temurbek@gmail.com',
        phone_number: '+998 93 560 24 99',
        job_title: 'Project manager',
        company: 'LLC VALSTATEX'
    },],
    isFetching: true,
    pageSize: 3,
    totalUsersCount: 0,
    totalEmployeesCount:0,
    currentPage: 1,
    employees:[
        {
            id: 1,
            age: 24,
            first_name: "Махаматов",
            last_name: "Валиахмад",
            middle_name: "Ринатович",
            date_of_birth: "1999-12-24",
            email: "mvrinatovicso@gmail.com",
            phone_number: "+998935602499",
            job_email: "v.makhamatov@valstatex.uz",
            jobTitle: "Менеджер проектов",
            company: 1
        },
        {
            id: 2,
            age: 30,
            first_name: "Темурбек",
            last_name: "Тошбеков",
            middle_name: "",
            date_of_birth: "1993-07-20",
            email: "",
            phone_number: "+998901885988",
            job_email: "t.toshbekov@valstatex.uz",
            jobTitle: "Коммерческий директор",
            company: 1
        },
    ]
};

export const personsReducer = (state = initialState, action) => {
    // debugger;
    switch(action.type) {
        case SET_PERSONS: {
            return { ...state, persons: action.persons }
        }
        case TOGGLE_IS_FETCHING: {
            return { ...state, isFetching: action.isFetching}
        }
        case SET_CURRENT_PAGE: {
            return { ...state, currentPage: action.currentPage}
        }
        case SET_TOTAL_USERS_COUNT: {
            return { ...state, totalUsersCount: action.count}
        }
        default:
            return state;
    }
}
export const employeeReducer = (state = initialState, action) => {
    switch(action.type) {
        case SET_EMPLOYEES: {
            return { ...state, employees: action.employees }
        }
        case SET_TOTAL_EMPLOYEES_COUNT: {
            return { ...state, totalEmployeesCount: action.count}
        }
        default:
            return state;
    }
}

export const setPersons = (persons) => ({type: SET_PERSONS, persons })
export const toggleIsFetching = (isFetching) => ({type: TOGGLE_IS_FETCHING, isFetching })
export const setCurrentPage = (currentPage) => ({type: SET_CURRENT_PAGE, currentPage })
export const setTotalUsersCount = (totalUsersCount) => ({type: SET_TOTAL_USERS_COUNT, count: totalUsersCount })

export const setEmployee = (employees) => ({type: SET_EMPLOYEES, employees })
export const setTotalEmployeeCount = (totalEmployeesCount) => ({type: SET_TOTAL_EMPLOYEES_COUNT, count: totalEmployeesCount })

export const requestPersons = (page, pageSize) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        dispatch(setCurrentPage(page));
            personsAPI.getPersons(page, pageSize).then(data => {
                dispatch(setPersons(data));
                dispatch(toggleIsFetching(false));
                dispatch(setTotalUsersCount(data.count));
        });
    }
}
export const requestEmployee = (page, pageSize) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        dispatch(setCurrentPage(page));
        employeeAPI.getEmployees(page, pageSize).then(data => {
            dispatch(setEmployee(data.results));
            dispatch(toggleIsFetching(false));
            dispatch(setTotalEmployeeCount(data.count));
        });
    }
}