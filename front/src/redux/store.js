import {configureStore} from '@reduxjs/toolkit'
import {personsReducer, employeeReducer}  from "./persons-reducer";


let store = configureStore({reducer: {
    personsReducer, employeeReducer}});

window.store = store;

export default store;
