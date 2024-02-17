import React, {useEffect} from 'react';
import {connect} from 'react-redux';
import {compose} from "redux";
import PreloaderInpage from "../../ui-components/Preloader/Preloader-inpage";
import {useParams} from "react-router-dom";
import PersonDescription from "./PersonDescription";
import {requestPersonDescription} from "../../../redux/reducers/persons-reducer";


const PersonDescriptionContainer = ({person, isFetching, getPersonDescription}) => {
    const { id } = useParams();
    useEffect(() => {
        getPersonDescription(id); // Передайте id вместо this.props.match.params.id
    }, [])

    return (<div>
            {isFetching ? <PreloaderInpage/> : <PersonDescription person ={person}/>}
        </div>);
};

const mapStateToProps = (state) => {
    const s = state.personsReducer;
    return {
        person: s.currentPersonDescription, isFetching: s.isFetching,
    };
};

export default compose(connect(mapStateToProps, {getPersonDescription: requestPersonDescription}))(PersonDescriptionContainer);