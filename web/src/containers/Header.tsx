export function Header(){
    return (
        <div className="flex flex-col items-center">
            <h1 className="text-4xl font-semibold text-slate-800 mt-5">
                ResumeFlex AI
            </h1>
            <p className="text-center text-slate-600 mt-3 text-sm">
                Envie um email para <a className="text-blue-600 font-medium" href="mailto:gabriel053jesus@gmail.com">gabriel053jesus@gmail.com</a> <br/> com o assunto "Currículo", seu currículo em .pdf anexado e ele aparecerá aqui!
            </p>
        </div>
    )
}