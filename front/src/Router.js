import {createBrowserRouter} from "react-router-dom";
import App from "./App";
import ErrorPage from "./components/ui-components/Error-page/error-page";
import PersonsContainer from "./components/Persons/PersonsContainer";
import CreatePerson from "./components/Persons/Person/CreatePerson";
import React from "react";
import AuthContainer from "./components/Auth/AuthContainer";
import ProjectsContainer from "./components/Projects/ProjectsContainer";
import ProjectDescriptionContainer from "./components/Projects/ProjectDescription/ProjectDescriptionContainer";
import PersonDescriptionContainer from "./components/Persons/PersonDescription/PersonDescriptionContainer";

export const Router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "persons",
                element: <PersonsContainer />,
            },
            {
                path: "/person/create",
                element: <CreatePerson />
            },
            {
                path: '/login',
                element: <AuthContainer />
            },
            {
                path: '/projects',
                element: <ProjectsContainer />
            },
            {
                path: '/projects/:id',
                element: <ProjectDescriptionContainer />
            },
            {
                path: '/persons/:id',
                element: <PersonDescriptionContainer />
            }

        ],
    },
]);