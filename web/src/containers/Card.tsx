
interface CardProps {
    children: React.ReactNode;
    className?: string;
    onClick?: () => void
}

export function Card({ children, className, onClick }: CardProps){
    return (
        <div onClick={onClick} className={`bg-white px-5 py-3 rounded-lg transition active:opacity-65 shadow-sm hover:shadow-md ${className && className}`}>
            {children}
        </div>
    )
}