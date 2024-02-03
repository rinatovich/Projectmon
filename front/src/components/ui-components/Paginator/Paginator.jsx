import style from "./Paginator.module.css";
import {Link} from "react-router-dom";


export default function Paginator(props){
    return(
        <div className={style.center}>
            <div className={style.pagination}>
                {props.currentPage===1?
                    '':<span onClick={(e) => {
                        props.onPageChanged(props.currentPage-1);
                    }}>&laquo;</span>
                }
                {
                    props.pages.map(p => {
                        return <span key={p} className={props.currentPage === p?style.active:''}
                            onClick={(e) => {
                                props.onPageChanged(p);
                            }
                        }>{p}</span>
                    })
                }
                {props.currentPage===props.pages.length?
                    '':<span onClick={(e) => {
                        props.onPageChanged(props.currentPage+1);
                    }}>&raquo;</span>
                }

            </div>
        </div>
    )
}
