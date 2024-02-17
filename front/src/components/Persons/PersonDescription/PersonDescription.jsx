import React from 'react';
const PersonDescription = (props) => {
    return (
        <div>
            <h2>Person description</h2>
            <div>first_name: {props.person.first_name},
                <br/>
            last_name: {props.person.last_name}, <br/>
            middle_name: {props.person.middle_name}, <br/>
            date_of_birth: {props.person.date_of_birth}
            </div>
        </div>
    );
};

export default PersonDescription;

