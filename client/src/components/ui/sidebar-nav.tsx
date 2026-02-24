import { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { buttonVariants } from '@/components/ui/button'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { cn } from '@/core/lib/utils'

type SidebarNavProps = React.HTMLAttributes<HTMLElement> & {
  items: {
    target: string
    title: string
    icon: JSX.Element
  }[]
  tabActive?: string
  onSelect?: (target: string) => void
}

export function SidebarNav({
  className,
  items,
  tabActive,
  onSelect,
  ...props
}: SidebarNavProps) {
  const { pathname } = useLocation()
  const navigate = useNavigate()
  const [val, setVal] = useState(pathname ?? '/settings')

  const handleSelect = (e: string | React.SyntheticEvent) => {
    const value = typeof e === "string" ? e : (e.target as any)?.value ?? ""
    setVal(value)
    if (onSelect) return onSelect(value)
    navigate(value)
  }

  return (
    <>
      <div className='p-1 md:hidden'>
        <Select value={val} onValueChange={handleSelect}>
          <SelectTrigger className='h-12 sm:w-48'>
            <SelectValue placeholder='Theme' />
          </SelectTrigger>
          <SelectContent>
            {items.map((item) => (
              <SelectItem key={item.target} value={item.target}>
                <div className='flex gap-x-4 px-2 py-1'>
                  <span className='scale-125'>{item.icon}</span>
                  <span className='text-md'>{item.title}</span>
                </div>
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      <div className='hidden w-full overflow-x-auto bg-background px-1 py-2 md:block'>
        <nav
          className={cn(
            'flex space-x-2 lg:flex-col lg:space-x-0 lg:space-y-1 text-primary',
            className
          )}
          {...props}
        >
            {items.map((item) => {
              if (onSelect) {
                return (
                  <button
                    key={item.target}
                    onClick={() => handleSelect(item.target)}
                    className={cn(
                      buttonVariants({ variant: 'ghost' }),
                      (tabActive ?? pathname) === item.target
                        ? 'bg-muted hover:bg-muted'
                        : 'hover:bg-transparent hover:underline',
                      'justify-start text-left w-full'
                    )}
                  >
                    <span className='mr-2'>{item.icon}</span>
                    {item.title}
                  </button>
                )
              }

              return (
                <Link
                  key={item.target} 
                  to={item.target}
                  className={cn(
                    buttonVariants({ variant: 'ghost' }),
                    pathname === item.target
                      ? 'bg-muted hover:bg-muted'
                      : 'hover:bg-transparent hover:underline',
                    'justify-start'
                  )}
                >
                  <span className='mr-2'>{item.icon}</span>
                  {item.title}
                </Link>
              )
            })}
        </nav>
      </div>
    </>
  )
}
