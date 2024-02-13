import {configureStore} from '@reduxjs/toolkit'
import {personsReducer, employeeReducer}  from "./persons-reducer";
import {authReducer} from "./auth-reducer";


let store = configureStore({reducer: {
    personsReducer, employeeReducer}});

window.store = store;

export default store;
