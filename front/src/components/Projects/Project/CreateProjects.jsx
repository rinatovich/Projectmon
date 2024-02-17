import { useForm } from "react-hook-form"
import React from 'react';
import style from './Project.module.css'
import {personsAPI} from "../../../api/api";
import {redirect, useNavigate} from "react-router-dom";


function CreatePersonForm() {
    const navigate = useNavigate();
    const {
        register,
        formState:{
            errors,
            isValid,
        },
        handleSubmit,
    } = useForm({
        mode: "onBlur",
    });

    const onSubmit = (data)=>{
        console.log(data);
        personsAPI.postPerson(data).then((r)=> {
            debugger;
                if (r === true) {
                    return  navigate('/persons');
                }
            }
        )
    }
    return(
        <form className={style.formGroup} onSubmit={handleSubmit(onSubmit)}>
            <div className={style.formFieldGroup}>
                <label>
                    <span>Фамилия:</span>
                    <input
                        {...register('first_name', {
                            required: 'Фамилия является объязательным полем',
                            minLength: {
                                value: 2,
                                message: 'Минимум 5 символов'
                            },
                        })}
                    />
                </label>
                <div className={style.errorMessage}>
                    {errors?.first_name && <p>{errors?.first_name?.message || "Error!"}</p>}
                </div>
            </div>
            <div className={style.formFieldGroup}>
                <label>
                    Имя:
                    <input
                        {...register('last_name', {
                            required: 'Имя является объязательным полем',
                            minLength: {
                                value: 2,
                                message: 'Минимум 5 символов'
                            },
                        })}
                    />
                </label>
                <div className={style.errorMessage}>
                    {errors?.last_name && <p>{errors?.last_name?.message || "Error!"}</p>}
                </div>
            </div>
            <div className={style.formFieldGroup}>
                <label>
                    Отчество:
                    <input
                        {...register('middle_name')}
                    />
                </label>
                <div className={style.errorMessage}>
                    {errors?.last_name && <p>{errors?.last_name?.message || "Error!"}</p>}
                </div>
            </div>
            <div className={style.formFieldGroup}>
                <label>
                    Дата рождения:
                    <input type='date'
                        {...register('date_of_birth')}
                    />
                </label>
                <div className={style.errorMessage}>
                    {errors?.date_of_birth && <p>{errors?.date_of_birth?.message || "Error!"}</p>}
                </div>
            </div>
            <div className={style.formFieldGroup}>
                <label>
                    E-mail:
                    <input type='email'
                        {...register('email')}
                    />
                </label>
                <div className={style.errorMessage}>
                    {errors?.email && <p>{errors?.email?.message || "Error!"}</p>}
                </div>
            </div>
            <div className={style.formFieldGroup}>
                <label>
                    Номер телефона:
                    <input type='tel'
                        {...register('phone_number')}
                    />
                </label>
                <div className={style.errorMessage}>
                    {errors?.phone_number && <p>{errors?.phone_number?.message || "Error!"}</p>}
                </div>
            </div>
                <input value={'Создать персону'} className={style.submit} type="submit" disabled={!isValid}/>

        </form>
    )
}

export default function CreateProjects(props){
    return (
        <div>
            <h1>Создаем персоны</h1>
            <CreatePersonForm/>
        </div>
    )
    }