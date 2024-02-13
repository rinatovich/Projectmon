import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";
import ErrorPage from "./components/ui-components/Error-page/error-page";
import Projects from "./components/Projects/Projects";
import { Provider } from 'react-redux'
import store from './redux/store'
import PersonsContainer from "./components/Persons/PersonsContainer";
import CreatePerson from "./components/Persons/Person/CreatePerson";
import EmployeesContainer from "./components/Emploees/EmployeesContainer";
import Login from "./components/Auth/Login";

const router = createBrowserRouter([
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
                path: "/projects",
                element: <Projects />
            },
            {
                path: "/person/create",
                element: <CreatePerson />
            },
            {
                path: "/employees",
                element: <EmployeesContainer />
            },
        ],
    },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
      <React.StrictMode>
          <RouterProvider router={router}/>
      </React.StrictMode>
    </Provider>
);


reportWebVitals();
