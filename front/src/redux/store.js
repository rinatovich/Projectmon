import {configureStore} from '@reduxjs/toolkit'
import {personsReducer}  from "./reducers/persons-reducer";
import {authReducer} from "./reducers/Auth-reducer";
import {projectsReducer} from "./reducers/projects-reducer";


let store = configureStore({reducer: {
    personsReducer, authReducer, projectsReducer}});

window.store = store;

export default store;
