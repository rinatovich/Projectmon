import style from './Preloader-inpage.module.css'

export default function PreloaderInpage(){
    return (
        <div className={style.preloaderContainer}>
            <div className={style.container}>
                <div className={style.wrapper}>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                    <div className={style.loader}>
                        <div className={style.dot}></div>
                    </div>
                </div>
                <div className={style.text}>
                    Please wait
                </div>
            </div>
        </div>
    )
}