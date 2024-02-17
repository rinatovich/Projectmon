import {projectsAPI} from "../../api/api";

const SET_PROJECTS = 'SET_PROJECTS';
const PROJECT_TOGGLE_IS_FETCHING = 'PROJECT_TOGGLE_IS_FETCHING';
const SET_PROJECTS_CURRENT_PAGE = 'SET_PROJECTS_CURRENT_PAGE';
const SET_TOTAL_PROJECTS_COUNT = 'SET_TOTAL_PROJECTS_COUNT';
const SET_PROJECT_DESCRIPTION = 'SET_PROJECT_DESCRIPTION';

let initialState = {
    projects: [
        {
            id: 1,
            title: "Обновление дизайна веб-сайта",
            start_date: "2023-04-03",
            end_date: null,
            created_at: "2023-03-26T00:00:00+05:00",
            status: "suspended"
        },
        {
            id: 2,
            title: "Обновление дизайна веб-сайта",
            start_date: "2023-04-03",
            end_date: null,
            created_at: "2023-03-26T00:00:00+05:00",
            status: "suspended"
        },
    ],
    isFetching: true,
    projectsPageSize: 5,
    totalProjectsCount: 0,
    projectsCurrentPage: 1,
    currentProjectDescription: {
        id: 21,
        stages: [
            {
                id: 1,
                tasks: [
                    {
                        id: 1,
                        documents: [],
                        title: "Task1",
                        description: "213saddcxzczxc",
                        completed: false,
                        stage: 1
                    },
                    {
                        id: 2,
                        documents: [
                            {
                                id: 5,
                                title: "ТЗ",
                                document_type: "word",
                                file: "http://127.0.0.1:8000/media/documents/%D0%9F%D0%B8%D1%81%D1%8C%D0%BC%D0%BE__StartSoft_xukC3Su.docx",
                                user: 1,
                                project: 21,
                                task: 2
                            }
                        ],
                        title: "Task 2",
                        description: "фывыфвыфвыфв",
                        completed: false,
                        stage: 1
                    }
                ],
                title: "Этап 1",
                order: 1,
                start_date: "2024-02-16",
                end_date: "2024-04-12",
                created_at: "2024-02-16",
                progress: "0.00%",
                status: "in_progress",
                project: 21
            },
            {
                id: 2,
                tasks: [
                    {
                        id: 3,
                        documents: [],
                        title: "фывыфвыфв",
                        description: "чямячсячсяч",
                        completed: false,
                        stage: 2
                    }
                ],
                title: "Этап 2",
                order: 2,
                start_date: "2024-02-16",
                end_date: "2024-05-11",
                created_at: "2024-02-16",
                progress: "0.00%",
                status: "in_progress",
                project: 21
            }
        ],
        title: "Внедрение CRM системы",
        start_date: "2023-03-03",
        end_date: "2023-08-06",
        created_at: "2024-02-14T19:31:14.120689+05:00",
        status: "in_progress"
    }
};

export const projectsReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_PROJECTS: {
            return {...state, projects: action.projects}
        }
        case PROJECT_TOGGLE_IS_FETCHING: {
            return {...state, isFetching: action.isFetching}
        }
        case SET_PROJECTS_CURRENT_PAGE: {
            return {...state, projectsCurrentPage: action.currentPage}
        }
        case SET_TOTAL_PROJECTS_COUNT: {
            return {...state, totalProjectsCount: action.count}
        }
        case SET_PROJECT_DESCRIPTION: {
            return {...state, currentProjectDescription: action.project}
        }
        default:
            return state;
    }
}

export const setProjects = (projects) => ({type: SET_PROJECTS, projects})
export const toggleIsFetching = (isFetching) => ({type: PROJECT_TOGGLE_IS_FETCHING, isFetching})
export const setProjectsCurrentPage = (currentPage) => ({type: SET_PROJECTS_CURRENT_PAGE, currentPage})
export const setTotalProjectsCount = (count) => ({type: SET_TOTAL_PROJECTS_COUNT, count})
export const setProjectDescription = (project) => ({type: SET_PROJECT_DESCRIPTION, project})


export const requestProjects = (page, pageSize) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        dispatch(setProjectsCurrentPage(page));
        projectsAPI.getProjects(page, pageSize).then(data => {
            dispatch(setProjects(data));
            dispatch(toggleIsFetching(false));
            dispatch(setTotalProjectsCount(data.count));
        });
    }
}

export const requestProjectDescription = (id) => {
    return (dispatch) => {
        dispatch(toggleIsFetching(true));
        projectsAPI.getProjectDescription(id).then(data => {
            dispatch(setProjectDescription(data));
            dispatch(toggleIsFetching(false));
        });
    }
}