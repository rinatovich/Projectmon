import { useRouteError } from "react-router-dom";
import style from './Errorpage.module.css'

export default function ErrorPage() {
    const error = useRouteError();
    console.error(error);

    return (
        <div id="error-page">
            <div className={style.oopss}>
                <div className={style.errortText}>
                    <img src={"https://cdn.rawgit.com/ahmedhosna95/upload/1731955f/sad404.svg"} alt="404"></img>
                        <span>Ошибка 404</span>
                        <p className="p-a">
                            Страница не найдена
                        </p>
                        <a href='/' className={style.back}>... Вернуться на главную</a>
                        <p>
                            <i>{error.statusText || error.message}</i>
                        </p>
                </div>
            </div>
        </div>
    )
}