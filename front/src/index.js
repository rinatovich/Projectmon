import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {
    RouterProvider,
} from "react-router-dom";
import { Provider } from 'react-redux'
import store from './redux/store'
import {Router} from "./Router";



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
      <React.StrictMode>
          <RouterProvider router={Router}/>
      </React.StrictMode>
    </Provider>
);


reportWebVitals();
