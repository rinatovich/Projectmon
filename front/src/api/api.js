import axios from "axios";


const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/1.0/',

});

export const personsAPI = {
    getPersons(currentPage = 1, pageSize=5) {
        return instance.get(`persons/?page=${currentPage}&page_size=${pageSize}`)
            .then(response => {
                return response.data;
            });
    },
    postPerson(newPerson){
        return instance.post('persons/',{
            "first_name": newPerson.first_name,
            "last_name": newPerson.last_name,
            "middle_name": newPerson.middle_name===""? null:newPerson.middle_name,
            "date_of_birth": newPerson.date_of_birth===""? null:newPerson.date_of_birth,
            "email": newPerson.email===""? null:newPerson.email,
            "phone_number": newPerson.phone_number===""? null:newPerson.phone_number
        }).then(response => {
                if (response.status == 201) {
                    return true;
        }})
    }
}
export const employeeAPI = {
    getEmployees(currentPage = 1, pageSize=5) {
        return instance.get(`employees/?page=${currentPage}&page_size=${pageSize}`)
            .then(response => {
                return response.data;
            });
    },
    postEmployee(newPerson){
        return instance.post('employee/',{
            "first_name": newPerson.first_name,
            "last_name": newPerson.last_name,
            "middle_name": newPerson.middle_name===""? null:newPerson.middle_name,
            "date_of_birth": newPerson.date_of_birth===""? null:newPerson.date_of_birth,
            "email": newPerson.email===""? null:newPerson.email,
            "phone_number": newPerson.phone_number===""? null:newPerson.phone_number
        }).then(response => {
            if (response.status == 201) {
                return true;
            }})
    }
}
export const projectsAPI = {
    getProjects(currentPage = 1, pageSize=5) {
        return instance.get(`projects/?page=${currentPage}&page_size=${pageSize}`)
            .then(response => {
                return response.data;
            });
    },
}