import {personsAPI, projectsAPI} from "../../api/api";
import {setProjectDescription} from "./projects-reducer";

const SET_PERSONS = 'SET_PERSONS';
const TOGGLE_IS_FETCHING = 'TOGGLE_IS_FETCHING';
const SET_CURRENT_PAGE = 'SET_CURRENT_PAGE';
const SET_TOTAL_PERSONS_COUNT = 'SET_TOTAL_PERSONS_COUNT';
const SET_PERSON_DESCRIPTION = 'SET_PERSON_DESCRIPTION';

let initialState = {
    persons: [
        {
            id: 2,
            first_name: "Петр",
            last_name: "Степанов",
            middle_name: "Олеговна",
            date_of_birth: "1983-11-27"
        },
    ],
    isFetching: true,
    pageSize: 5,
    totalPersonsCount: 0,
    currentPage: 1,
    currentPersonDescription: {
        id: 2,
        first_name: "Петр",
        last_name: "Степанов",
        middle_name: "Олеговна",
        date_of_birth: "1983-11-27"
    }
};

export const personsReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_PERSONS: {
            return {...state, persons: action.persons}
        }
        case TOGGLE_IS_FETCHING: {
            return {...state, isFetching: action.isFetching}
        }
        case SET_CURRENT_PAGE: {
            return {...state, currentPage: action.currentPage}
        }
        case SET_TOTAL_PERSONS_COUNT: {
            return {...state, totalPersonsCount: action.count}
        }
        case SET_PERSON_DESCRIPTION: {
            return {...state,currentPersonDescription: action.person }
        }
        default:
            return state;
    }
}

export const setPersons = (persons) => ({type: SET_PERSONS, persons})
export const toggleIsFetching = (isFetching) => ({type: TOGGLE_IS_FETCHING, isFetching})
export const setCurrentPage = (currentPage) => ({type: SET_CURRENT_PAGE, currentPage})
export const setTotalPersonsCount = (totalPersonsCount) => ({type: SET_TOTAL_PERSONS_COUNT, totalPersonsCount})
export const setCurrentPersonDescription = (person) => ({type: SET_PERSON_DESCRIPTION, person})

export const requestPersons = (page, pageSize) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        dispatch(setCurrentPage(page));
        personsAPI.getPersons(page, pageSize).then(data => {
            dispatch(setPersons(data));
            dispatch(toggleIsFetching(false));
            dispatch(setTotalPersonsCount(data.count));
        });
    }
}


export const requestPersonDescription = (id) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        personsAPI.getPersonDescription(id).then(data => {
            dispatch(setCurrentPersonDescription(data));
            dispatch(toggleIsFetching(false));
        });
    }
}