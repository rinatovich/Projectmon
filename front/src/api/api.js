import axios from "axios";


const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/1.0/',
    headers:{
        'Authorization': `Bearer ${localStorage.getItem("accessToken")}`
    }

});

export const personsAPI = {
    getPersons(currentPage = 1, pageSize=5) {
        return instance.get(`persons/?page=${currentPage}&page_size=${pageSize}`)
            .then(response => {
                return response.data;
            });
    },
    getPersonDescription(id){
        return instance.get(`persons/${id}`)
            .then(response => {
                return response.data;
            })
    }
}




export const projectsAPI = {
    getProjects(currentPage = 1, pageSize=5) {
        return instance.get(`projects/?page=${currentPage}&page_size=${pageSize}`)
            .then(response => {
                return response.data;
            });
    },
    getProjectDescription(id){
        return instance.get(`projects/${id}`)
            .then(response => {
                return response.data;
            })
    }
}

export const authAPI = {
    setUser(userName, userPassword){
        return instance.post('token/', {username: userName, password: userPassword})
            .then(response =>{
                const { access, refresh } = response.data;
                // Сохранение токенов в локальном хранилище
                localStorage.setItem('accessToken', access);
                localStorage.setItem('refreshToken', refresh);
                return response.data;
            })
    }
}