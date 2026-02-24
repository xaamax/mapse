import { ReactNode } from "react"
import { Separator } from "@/components/ui/separator"

interface Props {
  title: string
  desc: string
  children?: ReactNode
}

export function PageSectionLayout({ title, desc, children }: Props) {
  return (
    <div className="flex flex-1 flex-col">
      <div className="flex-none">
        <h3 className="text-lg font-medium">{title}</h3>
        <p className="text-sm text-muted-foreground">{desc}</p>
      </div>

      <Separator className="my-4 flex-none" />

      <div className="faded-bottom flex-1 overflow-y-auto scroll-smooth md:pb-16">
        <div className="w-full">
          {children}
        </div>
      </div>
    </div>
  )
}