import {employeeAPI, personsAPI} from "../api/api";

const SET_ENTITIES = 'SET_ENTITIES';
const TOGGLE_IS_FETCHING = 'TOGGLE_IS_FETCHING';
const SET_CURRENT_PAGE = 'SET_CURRENT_PAGE';
const SET_TOTAL_ENTITIES_COUNT = 'SET_TOTAL_ENTTIES_COUNT';

let initialState = {
    entities: [
        {
            id: 1,
            details: {
                id: 1
            },
            ownershipForm: {
                id: 1,
                shortForm: "ООО",
                longForm: "Общество с ограниченной ответственностью"
            },
            address: {
                id: 1,
                country: "Узбекистан",
                city: "Ташкент",
                district: null,
                street: "Айбек",
                house: "20",
                flat: null,
                postal_code: "100015"
            },
            name: "VALSTATEX",
            phoneNumber: "+998712371966",
            websiteUrl: "https://valstatex.uz/",
            logo: "http://127.0.0.1:8000/media/organizations/logos/VALSTATEX_LOGO.png"
        },
        {
            id: 2,
            details: {
                id: 2
            },
            ownershipForm: {
                id: 2,
                shortForm: "АИКБ",
                longForm: "Акционерный Инновационный коммерческий банк"
            },
            address: {
                id: 2,
                country: "Узбекистан",
                city: "Ташкент",
                district: null,
                street: "Абдулла Кадыри",
                house: "2",
                flat: null,
                postal_code: "100017"
            },
            name: "IPAK YULI",
            phoneNumber: null,
            websiteUrl: "https://ru.ipakyulibank.uz",
            logo: "http://127.0.0.1:8000/media/organizations/logos/ipak_en.png"
        },
        {
            id: 3,
            details: {
                id: 3
            },
            ownershipForm: {
                id: 3,
                shortForm: "АКБ",
                longForm: "Акционерный коммерческий банк"
            },
            address: {
                id: 3,
                country: "Узбекистан",
                city: "Ташкент",
                district: null,
                street: "Лутфий",
                house: "14",
                flat: null,
                postal_code: "100096"
            },
            name: "Микрокредитбанк",
            phoneNumber: "+998712029999",
            websiteUrl: "https://mkbank.uz/ru",
            logo: "http://127.0.0.1:8000/media/organizations/logos/logo.png"
        }
    ],
    entitiesCount: 0,
};

export const entitiesReducer = (state = initialState, action) => {
    // debugger;
    switch(action.type) {
        case SET_ENTITIES: {
            return { ...state, entities: action.entities }
        }
        case TOGGLE_IS_FETCHING: {
            return { ...state, isFetching: action.isFetching}
        }
        case SET_CURRENT_PAGE: {
            return { ...state, currentPage: action.currentPage}
        }
        case SET_TOTAL_ENTITIES_COUNT: {
            return { ...state, entitiesCount: action.count}
        }
        default:
            return state;
    }
}

export const setEntities = (entities) => ({type: SET_ENTITIES, entities })
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