import {createSelector} from "reselect";

const getPersonsSelector = (state) => {
    return state.persons;
}

export const getPersonel = createSelector(getPersonsSelector,
    (persons) => {
        return persons;
    })

export const getTotalUsersCount = (state) => {
    return state.totalUsersCount;
}

export const getCurrentPage = (state) => {
    return state.currentPage;
}

export const getTotalEmployeesCount = (state) => {
    return state.totalEmployeesCount;
}
