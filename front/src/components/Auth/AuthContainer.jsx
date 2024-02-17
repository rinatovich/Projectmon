import React from 'react';
import {connect} from 'react-redux';
import {compose} from "redux";
import {requestUserAuth} from "../../redux/reducers/Auth-reducer";
import PreloaderInpage from "../ui-components/Preloader/Preloader-inpage";
import Auth from "../Auth/Auth";


class AuthContainer extends React.Component {
    componentDidMount() {}
    onPageChanged = () => {}
    render (){
        return (
            <div>
                {
                    this.props.isFetching ? <PreloaderInpage/> :
                        <Auth
                            requestUserAuth={this.props.authUser}
                        />
                }
            </div>
        )
    }
}


let mapStateToProps = (state) => {
    let s = state.authReducer;
    return {
        username: s.username,
        isFetching: s.isFetching,
        password: s.password,
    }
}


export default compose(
    connect(mapStateToProps,{authUser: requestUserAuth})
)(AuthContainer)
