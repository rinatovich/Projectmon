import {authAPI} from "../../api/api";
import {toggleIsFetching} from "./persons-reducer";

const SET_USER_DATA = 'SET_USER_DATA';

let initialState = {
    username: "",
    password: "",
};

export const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_USER_DATA: {
            return {...state, userName: action.userName}
        }
        default:
            return state;
    }
}

export const setUserData = (userName) => ({type: SET_USER_DATA, userName})


export const requestUserAuth = (userName, userPassword) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        authAPI.setUser(userName, userPassword).then(data => {
            dispatch(setUserData(data));
            dispatch(toggleIsFetching(false));
        });
    }
}
